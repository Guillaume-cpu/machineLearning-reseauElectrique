clear all; close all;
addpath('function')
warning('off','MATLAB:illConditionedMatrix');
warning('off','MATLAB:singularMatrix');


% Load the dataset
load('loadData/dataset/initialSet');
dataset = set;

% Load the bus, generator and line data
load('gridData/grid_ex'); 

% Initialisation 
security = NaN * ones(size(dataset,1),2);
linePower = NaN * ones(size(grid.linedata,1), ...
                        size(grid.linedata,1)+1, size(dataset,1));
load_X = NaN * ones(size(dataset,1), 56);
gen_X = NaN * ones(size(dataset,1), 6);

% Parcour les lignes du dataset 
% for i = 1:size(dataset,1)
% for i = 1:96 % 1 jour

pas = 1; dividePower = 180;
for i = 1:pas:size(dataset,1)
% for i = 1:pas:1
    if mod(i,97)==0
        jour = i/97
    end
    % Données des bus au temps i
    busdata = grid.busdata; 
    busdata(2:end,3) = dataset(i,:)'.*grid.ratioP/dividePower; % Pload 
    busdata(2:end,4) = busdata(2:end,3).*grid.ratioQ; % Qload
    load_X(i,:) = busdata(2:end,3)';
    
    
    % Répartition des charges sur les noeuds PU
    gendata = loadDistribution(busdata, grid.gendata);
    gen_X(i,:) = gendata(2:end,2)';
    
    % Calcul de load flow au temps i 
    linePower(:,:,i) = N1( grid.linedata, gendata, busdata);
    
    % Contrôle de sécurité N et N-1 au temps i 
    security(i,1) = any(linePower(:,1,i) > grid.thLimit);
    %% prendre que le worst case !
    security(i,2) = securityN1( linePower(:,2:end,i), grid.thLimit);
    
end

warning('on','MATLAB:illConditionedMatrix');
warning('on','MATLAB:singularMatrix');

%% Save the dataset 
folderName = ['dp' num2str(dividePower)];
path = [ 'machineLearning/dataset/' folderName '/dataset'];
injected_X = [load_X gen_X]; thLimit = grid.thLimit;
secuN_Y = security(:,1); secuN1_Y = security(:,2);
save(path,'injected_X', 'load_X', 'gen_X', ...
     'secuN_Y', 'secuN1_Y', 'linePower', 'thLimit');

%% Function 
function secu = securityN1( linePower, thLimit)
    line = linePower ./ thLimit;
    secu = any(any(line > 1));
end

function gendata = loadDistribution( busdata, gendata)
    P = sum(busdata(2:end,3));
    Q = sum(busdata(2:end,4));
    gendata(2:end,2) = P * gendata(2:end,4);
    gendata(2:end,3) = Q * gendata(2:end,5);
end
