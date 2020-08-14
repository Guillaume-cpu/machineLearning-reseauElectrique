function LF = unknowPower( LF, Sb, Y, busdata)
% Calculer les puissances générées avec les nouvelles données
% Pg et Qg Slack bus & Qg des PU bus ( Les puissance inconnues) 
% LF = [ bus_id P Q dP dQ Pg Qg]

for i = 1:size(busdata,1)
    if busdata(i,2) == 0 % Slack bus
        % Calcule de Pg & Qg
        sumP = 0; sumQ = 0; % Initialisation pour la SUM 
        for k = 1:size(busdata,1)
            % SUM
            % Pi = Ui * SUM(Yik * Uk * cos(Tik+Tk-Ti))
            p = abs(Y(i,k)) * busdata(k,5) * ...
                cos(angle(Y(i,k)) + busdata(k,6) - busdata(i,6));
            sumP = sumP + p;
            % Qi = Ui * SUM(Yik * Uk * cos(Tik+Tk-Ti))
            q = abs(Y(i,k)) * busdata(k,5) *...
                sin(angle(Y(i,k)) + busdata(k,6) - busdata(i,6));
            sumQ= sumQ + q;
        end
        LF(i,1) = 1; % Slack bus id
        LF(i,2) = busdata(i,5) * sumP; % Slack bus P 
        LF(i,3) = -busdata(i,5) * sumQ; % Slack bus Q 
        
        % QG1=(Q1+QLD1)*Sb;
        LF(i,6) = (LF(i,2) + busdata(i,3))*Sb; % Slack bus Pgen 
        % QG1=(Q1+QLD1)*Sb;
        LF(i,7) = (LF(i,3) + busdata(i,4))*Sb; % Slack bus Pgen
    
    elseif busdata(i,2) == 1 % PU bus
        % Calcule de Qg
        % Qi = Ui * SUM(Yik * Uk * sin(Tik+Tk-Ti))
        
        sum = 0; % Initiale value for sum
        for k = 1:size(busdata,1) % SUM
            q = abs(Y(i,k)) * busdata(k,5) *...
                sin(angle(Y(i,k)) + busdata(k,6) - busdata(i,6));
            sum = sum + q;
        end
        
        LF(i,3) = busdata(i,5) * sum; % Q
        % QG=(Q+QLD)*Sb;
        LF(i,7) = (LF(i,3) + busdata(LF(i,1),4))*Sb; % Qgen
    end % if   
end % For i LF