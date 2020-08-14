clear all; close all;
folderNames = { 'alourdi.mat'; '5pourcent/normal.mat'};
labelX = 'Jours d''entraînement'; 
labelY = 'Fausse alarme';
labelYY = 'Non-détection';
modelNames = {'kNN','SVC','NN','RF'};
Srow = 1; Scol = 2; % for subplot
width = 700; large = 250;
fs = 10;
scenario = 'alourdi';
      
for i = 1
    %% Load file and calcul de ratio F/Fth
    load(folderNames{i});
    
    figure(1)
    tiledlayout( Srow, Scol)
%     subplot( Srow, Scol, i);

    nexttile
    h = plot( injection(1,9:end), injection(4,9:end),'o')
    set(h, 'MarkerFaceColor', get(h,'Color')); 
    ylabel(labelY, 'fontsize', fs);ylim([0 250]);
    yyaxis right;
    h = plot( injection(1,9:end), injection(5,9:end), 'o');
    set(h, 'MarkerFaceColor', get(h,'Color')); 
    xlabel(labelX, 'fontsize', fs); ylabel(labelYY, 'fontsize', fs);
    ylim([0 10]); % 10 ou 70
    legend('Fausse alarme', 'Non-détection');
    
    nexttile
    h = plot( injection(1,9:end), injection(6,9:end),'o')
    set(h, 'MarkerFaceColor', get(h,'Color')); 
    ylabel(labelY, 'fontsize', fs);ylim([0 250]);
    yyaxis right;
    h = plot( injection(1,9:end), injection(7,9:end), 'o');
    set(h, 'MarkerFaceColor', get(h,'Color')); 
    xlabel(labelX, 'fontsize', fs); ylabel(labelYY, 'fontsize', fs);
    ylim([0 10]); % 10 ou 70
    

end
set(figure(1), 'Position',  [100, 100, 100+width, 100+large])
fig = gcf;
fig.PaperPositionMode = 'auto';
print('result_resume','-dpng','-r0')