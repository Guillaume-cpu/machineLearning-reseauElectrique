function NP = netProduction(gendata,busdata)
% Production net 
% Seulement les noeuds où il y a de la production ?
% Non tous sauf le slack
% NP = [ bus_id   NP  NQ ]
NP = zeros(size(busdata,1)-1,3);
for i = 2:size(busdata,1)
    % Bus id % i-1 car slack bus
    id = busdata(i,1);
    NP(i-1,1) = id;
    
    if busdata(i,2) == 1 % PU-bus
        % Puissance Active - NetP = Pg - Pl
        NP(i-1,2) = gendata(gendata(:,1)==id,2)...
                    - busdata(i,3);
        %NP(i-1,2) = NaN;
    else % PQ-bus
        % Puissance Active - NetP = Pg - Pl
        NP(i-1,2) = 0 - busdata(i,3);
        % Puissance Réactive - NetQ = Qg - Ql
        NP(i-1,3) = 0 - busdata(i,4);
    end
end % for i