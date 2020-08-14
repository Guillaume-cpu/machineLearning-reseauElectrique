%% Fonction permettant d'�tablir la matrice d'admittance
% Entr�e : Un tableau comportant [ startBus stopBus R X ]
% Sortie : Matrice d'admittance correspondante

function ymat = yMatrix(linedata)

    nbus = max( max(linedata(:,1:2)) ); % La maximum des 2 premi�res col.
    ymat = zeros(nbus,nbus); % Initialisation de la Y-mat. n x n 

    for i=1:nbus
        for k=1:nbus
            if  k == i 
                %% Diagonale
                % Somme des admittances connect�es au noeud i

                % Index des lignes connect�es au noeud i
                index = or( linedata(:,1)==i, linedata(:,2)==i) ;

                % Si une/des lignes sont trouv�es
                if any(index)

                    % R�cup�ration des lignes connect�es
                    line(:,1:2) = linedata(index,3:4);

                    % Somme des admittences
                    y = 0;
                    for l = 1:size(line,1)
                        z = line(l,1) + 1i * line(l,2);
                        y = y + 1/z;
                    end
                    clear line            
                    ymat(i,k) = y ;

                else 
                    % Si aucune ligne connect�e au noeud i
                    ymat(i,k) = 0;

                end % end if

            else
                % Hors diagionale
                % Somme chang�e de signe des admittances
                % qui connenctent le noeud 'i' au 'k'

                % Index des lignes connect�es au noeud i
                index_a = and( linedata(:,1)==i, linedata(:,2)==k);
                index_b = and( linedata(:,1)==k, linedata(:,2)==i);
                index = or( index_a, index_b);

                % Si une/des lignes sont trouv�es
                if any(index)

                    % R�cup�ration des lignes connect�es
                    line(:,1:2) = linedata(index,3:4);

                    % Somme des admittences
                    y = 0;
                    for l = 1:size(line,1)
                        z = line(l,1) + 1i * line(l,2);
                        y = y + 1/z;
                    end
                    clear line
                    ymat(i,k) = -y ;

                else 
                    % Si aucune ligne connecte le noeud i au noeud k
                    ymat(i,k) = 0;

                end % if any()  
            end % if i==k     
        end %for n 
    end % for m
end % function yMatrix



 