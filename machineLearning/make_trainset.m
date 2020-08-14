clear all; close all; addpath('function');
warning('off','MATLAB:illConditionedMatrix');
warning('off','MATLAB:singularMatrix');

% Load the bus, generator and line data
load('gridData/grid_ex');
my_mpc = loadcase( 'case57');

% Initialisation 
yearS = 96 * 365; load_X = NaN * ones(yearS, 57);
gen_X = NaN * ones(yearS, 7); securityN1 = NaN * ones(80, 1);
secuN_Y = NaN * ones ( yearS, 1); secuN1_Y = NaN * ones( yearS, 1);

m = (30*96+1);
for i = 1:yearS
    if mod(i,m)==0
        month = i/m
    end
    
    % Données des bus au temps i
    my_mpc.bus(:,3) = rand(57,1) .* grid.ratioP ./ 1.45 ; % Pload 
    my_mpc.bus(:,4) = my_mpc.bus(:,3) .* grid.ratioQ; % Qload
    load_X(i,:) = my_mpc.bus(:,3)'/100;
    
    % Répartition des charges sur les noeuds PU
    P = sum(my_mpc.bus(:,3)); my_mpc.gen(:,2) = P * grid.gendata(:,4);
    Q = sum(my_mpc.bus(:,4)); my_mpc.gen(:,3) = Q * grid.gendata(:,5);
    gen_X(i,:) = my_mpc.gen(:,2)'/100;
    
    %% N security
    % Calcul de load flow au temps i
    PF = runpf(my_mpc); PF.branch(:,14) = abs(PF.branch(:,14))/100 ;
    
    % Contrôle de sécurité N
    secuN_Y(i,1) = any(PF.branch(:,14) > grid.thLimit);
    
%     %% N-1 security
%     for j = 1:size( my_mpc.branch, 1)
%         % Suprimer 1 ligne
%         my_mpcN = my_mpc; my_mpcN.branch(j,:) = [];
%         thLimitN = grid.thLimit; thLimitN(j,:) = [];
%         
%         % Calcul de load flow au temps i
%         PFN = runpf(my_mpcN);
%         PFN.branch(:,14) = abs(PFN.branch(:,14))/100 ;
%     
%         % Contrôle de sécurité N
%         securityN1(j,1) = any(PFN.branch(:,14) > thLimitN);
%     end
%     secuN1_Y(i,1) = any(securityN1(:,1) > 0);
    
end

%% Save the dataset 
folderName = 'train'; path = [ 'dataset/' folderName '/5pourcent/dataset145_d'];
injected_X = [load_X gen_X]; thLimit = grid.thLimit;
save(path,'injected_X', 'load_X',   'gen_X', ...
          'secuN_Y');
      
warning('on','MATLAB:illConditionedMatrix');
warning('on','MATLAB:singularMatrix');