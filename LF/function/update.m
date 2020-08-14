function busdata = update( LF, JAC, busdata)
%Step 4 - Calculer les différences 
% dP pour PU-bus et PQ-bus
% dQ seulement pour PQ-bus
% Slack bus non-compris
dP = LF(2:end,4);
dQ = LF(busdata(:,2)==2,5);
DX = JAC \ [dP;dQ];

%Step 5 - Mise à jour des tensions et des angles
k = size(dP,1)+1;

for i = 2:size(LF,1)
    if busdata(LF(i,1),2)==1
        % PU-BUS, Seulement dP, donc delta Theta
        busdata(LF(i,1),6) = busdata(LF(i,1),6) + DX(i-1);

    elseif busdata(LF(i,1),2)==2
        % PQ-BUS, dP et dQ, delta Theta et U
        busdata(LF(i,1),6) = busdata(LF(i,1),6) + DX(i-1);
        
        busdata(LF(i,1),5) = busdata(LF(i,1),5)*(1+DX(k)/busdata(LF(i,1),5));
        k = k+1;
    end % if bus type
end % for LF 