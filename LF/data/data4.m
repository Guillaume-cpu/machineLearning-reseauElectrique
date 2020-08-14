function [busdata, gendata, linedata, Ymat] = data4
% Donnée des noeuds de charge, de produtcion et des lignes
% busdata = [bus_i type   P     Q       U   Theta]
busdata =   [
                1   0   0.1     0.02    1   0;
                2   2   0.9     0.1     1   0;
                3   2   0.8     0.1     1   0;
                4   2   0.5     0.1     1   0;
            ];

% gendata = [ bus_i P   Q   U ]
gendata=[ 2 0 0];

%%%%%%%%%%%% Line data %%%%%%%%%%%%
Sb=100; Ub=220; Zb=Ub^2/Sb;

% line data = [ startBus stopBus R X ]
linedata =   [
             1 2    5/Zb    65/Zb
             1 3    4/Zb    60/Zb
             2 3    5/Zb    66/Zb
             3 4    3/Zb    30/Zb 
            ];

Z12=(5+j*65)/Zb;bsh12=0.0002*Zb;
Z13=(4+j*60)/Zb;bsh13=0.0002*Zb;
Z23=(5+j*68)/Zb;bsh23=0.0002*Zb;
Z34=(3+j*30)/Zb;bsh34=0;

%%%%%%%%%%%%%% % YBUS matrix %%%%%%%%%%%%%% 
y11=1/Z12+1/Z13+j*bsh12+j*bsh13; y12=-1/Z12; y13=-1/Z13; y14=0;%
y21=-1/Z12; y22=1/Z12+1/Z23+j*bsh12+j*bsh23; y23=-1/Z23; y24=0;%
y31=-1/Z13; y32=-1/Z23; y33=1/Z13+1/Z23+1/Z34+j*bsh13+j*bsh23; y34=-1/Z34;%
y41=0; y42=0; y43=-1/Z34; y44=1/Z34;%
Ymat=[y11 y12 y13 y14; y21 y22 y23 y24; y31 y32 y33 y34; y41 y42 y43 y44];%