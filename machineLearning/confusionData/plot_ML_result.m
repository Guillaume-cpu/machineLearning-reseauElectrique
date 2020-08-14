clear all; close all;
folderNames = { 'alourdi.mat'; '5pourcent/normal.mat'};
labelX = '# jours d''entraînement'; 
labelY = '# Fausses alarmes';
labelYY = '# Non-détections';
modelNames = {'kNN','SVC','NN','RF'};
Srow = 2; Scol = 2; % for subplot
width = 700; large = width-350;
fs = 8;
scenario = 'normal';
      
for i = 2
    %% Load file and calcul de ratio F/Fth
    load(folderNames{i});
    
    figure(1)
    tiledlayout( Srow, Scol)
%     subplot( Srow, Scol, i);
    for i = 1:4
        nexttile
        plot( injection(1,9:end), injection(2*i,9:end),'*')
        ylabel(labelY, 'fontsize', fs);ylim([0 350]);
        yyaxis right;
        plot( injection(1,9:end), injection(2*i+1,9:end), 'x');
        xlabel(labelX, 'fontsize', fs); ylabel(labelYY, 'fontsize', fs); title(modelNames{i});
         ylim([0 70]); % 10 ou 70 
    end
    
    figure(2)
    tiledlayout( Srow, Scol)
%     subplot( Srow, Scol, i);
    for i = 1:4
        nexttile
        plot( charge(1,9:end), charge(2*i,9:end),'*')
        ylabel(labelY, 'fontsize', fs);ylim([0 350]);
        yyaxis right;
        plot( charge(1,9:end), charge(2*i+1,9:end), 'x');
        xlabel(labelX, 'fontsize', fs); ylabel(labelYY, 'fontsize', fs); title(modelNames{i});
         ylim([0 70]); % 10 ou 70 
    end
    figure(3)
    tiledlayout( Srow, Scol)
%     subplot( Srow, Scol, i);
    for i = 1:4
        nexttile
        plot( production(1,9:end), production(2*i,9:end),'*')
        ylabel(labelY, 'fontsize', fs);ylim([0 350]);
        yyaxis right;
        plot( production(1,9:end), production(2*i+1,9:end), 'x');
        xlabel(labelX, 'fontsize', fs); ylabel(labelYY, 'fontsize', fs); title(modelNames{i});
         ylim([0 70]); % 10 ou 150
    end
end
set(figure(1), 'Position',  [100, 100, 100+width, 100+large])
set(figure(2), 'Position',  [100, 100, 100+width, 100+large])
set(figure(3), 'Position',  [100, 100, 100+width, 100+large])
saveas(figure(1),[ scenario,'_inj.png']);
saveas(figure(2),[ scenario,'_load.png']);
saveas(figure(3),[ scenario,'_gen.png']);
% set(figure(2), 'Position',  [100, 100, 100+width, 100+large])
