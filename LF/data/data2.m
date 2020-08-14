function [busdata, gendata, linedata] = data2
% Donnée des noeuds de charge, de produtcion et des lignes
% busdata = [bus_i type   P     Q       U   Theta]
busdata =   [
                1   0   0.2     0.02    1   0;
                2   1   2       0.2     1   0;  
            ];

% gendata = [ bus_i P   Q   U ]
gendata =   [
                2   1   .405255    1;
            ];
               
% line data = [ startBus stopBus R X ]
linedata = [ 
                1 2     0.02    0.2;               
           ];

       
       