function [busdata, gendata, linedata] = dataBook
% Donnée des noeuds de charge, de produtcion et des lignes
% busdata = [bus_i type   P     Q       U   Theta]
busdata =   [
                1   3   0       0       1       0;
                2   2   0.9     0.1     1.05    0;
                3   1   2.8653  1.2244  1       0;
            ];

% gendata = [ bus_i P   Q   U ]
gendata=[
            2   0.6661 0
    ];

% line data = [ startBus stopBus R X B]
linedata =   [
             1 2    0    0.1 0.01
             1 3    0    0.1 0.01
             2 3    0    0.1 0.01
            ];