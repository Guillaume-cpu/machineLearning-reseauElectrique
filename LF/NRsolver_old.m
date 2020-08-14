clear all
close all

%% PATH for function and data 
addpath('./function')
addpath('./data')

%% Initialisation 
% Grandeur de base
Sb=100; Ub=220; deg=180/pi;

% Critère de convergence N-R
tole=1e-6;

% Donnée des noeuds de charge, de produtcion
% et des lignes
[busdata, gendata, linedata, Y] = data4;
% [busdata, gendata, linedata] = data2;
% 
% % Matrice d'admittance
% Y = yMatrix(linedata);

%% Newton - Raphson 
% Production net 
% NetP = [ bus_1 P Q]
NP = netProduction(gendata,busdata);

% Valeurs initiales des incunnues pour N-R
% Directement dans le tableau busdata


% Première itération
% Puissance injectée dans chaque bus, calcul des variables
% connues --> P et Q si PQ-bus, P si PU-bus
LF = zeros(size(busdata,1),1);
for i = 2:size(busdata,1)
    LF(i,1) = busdata(i,1); % Bus_id
end

% LF = [ bus_id P Q dP dQ Pg Qg]
LF = loadFlow(LF, Y, busdata);

% Delta entre la Pprod Pinj dans chaque bus
% Slack bus non-compris
for i = 1:size(NP,1)
    % dp = NP-Lf(:,4)
    LF(NP(i,1),4) = NP(i,2)-LF(NP(i,1),2);
    LF(NP(i,1),5) = NP(i,3)-LF(NP(i,1),3);
end

% Condition de convergence
while all(abs([ LF(2:end,4) ; LF(2:end,4) ])> tole)
    
    %Step 2
    % 2a) Pinj/bus Calcule des valeurs connues
    % P et Q si bus PQ, P si bus PU
    LF = loadFlow(LF,Y,busdata);
        
    %2b - Delta entre la Pprod Pinj dans chaque bus
    % Ces valeurs doivent respectés la convergence
    % Slack bus non-compris
    for i = 1:size(NP,1)
        LF(NP(i,1),4) = NP(i,2)-LF(NP(i,1),2);
        LF(NP(i,1),5) = NP(i,3)-LF(NP(i,1),3);
    end
    
    %Step 3 - Jacobian
    JAC = jacobian(LF,Y,busdata);
    
    %Step 4 - Calculer les différences et MàJ
    busdata = update( LF, JAC, busdata);
    
end % While convergence

%% Step final

% Calculer des puissances inconnues
% Pg et Qg Slack bus & Qg des PU bus
LF = unknowPower( LF, Sb, Y, busdata);

% % Calculer les flux de puissance
linedata = powerFlow( linedata, Y, busdata);

ANG = busdata(:,6)*deg;
VOLT = busdata(:,5)*Ub;