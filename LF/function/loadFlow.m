function LF = loadFlow(LF,Y,busdata)
% Puissance injectée dans chaque bus
% Calcule des variables que l'on connait
% P et Q si bus PQ, P si bus PU

for i = 2:size(busdata,1)
    if busdata(i,2) == 1 % PU bus
        % Calcule de Pi
        % LFI = Ui * SUM(Yik * Uk * cos(Tik+Tk-Ti))
        sum = 0;
        for k = 1:size(busdata,1) % SUM
            p = abs(Y(i,k)) * busdata(k,5) * cos(angle(Y(i,k)) + busdata(k,6) - busdata(i,6));
            sum = sum + p;
        end
        LF(i,2) = busdata(i,5) * sum;
    elseif busdata(i,2) == 2 % PQ bus
        % Calcule de Pi & Qi
        % SUM
        sumP = 0; sumQ = 0;
        for k = 1:size(busdata,1)
            % LFI = Ui * SUM(Yik * Uk * cos(Tik+Tk-Ti))
            p = abs(Y(i,k)) * busdata(k,5) * ...
                cos(angle(Y(i,k)) + busdata(k,6) - busdata(i,6));
            sumP = sumP + p;
            q = abs(Y(i,k)) * busdata(k,5) *...
                sin(angle(Y(i,k)) + busdata(k,6) - busdata(i,6));
            sumQ= sumQ + q;
        end
        LF(i,2) = busdata(i,5) * sumP; 
        LF(i,3) = -busdata(i,5) * sumQ;
    end % if   
end % For i LF