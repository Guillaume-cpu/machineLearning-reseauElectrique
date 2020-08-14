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
[busdata, gendata, linedata, Y] = data44;
% [busdata, gendata, linedata] = dataBook;
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
LF = busdata(:,1); LF(1) = 0; % 0 for detecting slack bus
% LF = [ bus_id P Q dP dQ Pg Qg]
LF = loadFlow(LF, Y, busdata);

% Delta entre la Pprod Pinj dans chaque bus
% Slack bus non-compris
LF(NP(:,1),4) = NP(:,2)-LF(NP(:,1),2); % dP = NP - Lf(:,2)
LF(NP(:,1),5) = NP(:,3)-LF(NP(:,1),3); % dQ = NP - LF(:,3)

% Condition de convergence
while all(abs([ LF(2:end,4) ; LF(2:end,4) ])> tole)
    
    % Step 2
    % 2a) Pinj/bus Calcule des valeurs connues
    % P et Q si bus PQ, P si bus PU
    LF = loadFlow(LF,Y,busdata);

    %2b - Delta entre la Pprod Pinj dans chaque bus
    % Ces valeurs doivent respectés la convergence(S-bus non-compris)
    LF(NP(:,1),4) = NP(:,2)-LF(NP(:,1),2);
    LF(NP(:,1),5) = NP(:,3)-LF(NP(:,1),3);

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