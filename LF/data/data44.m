function [busdata, gendata, linedata] = data44
% Donnée des noeuds de charge, de produtcion et des lignes
% busdata = [bus_i type   P     Q       U   Theta]
busdata =   [
                1   0   0.1     0.02    1   0;
                2   1   0.9     0.1     1   0;
                3   1   0.8     0.1     1   0;
                4   2   0.5     0.1     1   0;
            ];

% gendata = [ bus_i P   Q]
gendata =   [
             2 0.1 0.05;
             3 0.1 0.05
            ];
               
%%%%%%%%%%%% % Line data %%%%%%%%%%%%
Sb=100; Ub=220; Zb=Ub^2/Sb;

% line data = [ startBus stopBus R X ]
linedata =   [
             1 2    5/Zb    65/Zb
             1 3    4/Zb    60/Zb
             2 3    5/Zb    66/Zb
             3 4    3/Zb    30/Zb 
            ];