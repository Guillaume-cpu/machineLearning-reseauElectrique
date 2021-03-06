function linedata = powerFlow( linedata, Y, busdata)
% % Calculer les flux de puissance
% linedata = [ sB eB r x Pik Pki Qik Qki ]
G = real(Y); B = imag(Y);
g = -G     ; b = -B;

for n = 1:size(linedata,1)
    k = linedata(n,1);
    j = linedata(n,2);
    % Pkj = gkj Uk^2 ?Uk Uj [gkj cos(?kj) + bkj sin(?kj)]
    linedata(n,5) = g(k,j)*busdata(k,5)^2 - busdata(k,5) *...
                    busdata(j,5) * ( g(k,j) * cos(busdata(k,6)-busdata(j,6))...
                    + b(k,j) * sin(busdata(k,6)-busdata(j,6)));
    linedata(n,6) = g(j,k)*busdata(j,5)^2 - busdata(j,5) *...
                    busdata(k,5) * ( g(j,k) * cos(busdata(j,6)-busdata(k,6))...
                    + b(j,k) * sin(busdata(j,6)-busdata(k,6)));
    % Qkj = ? bkj Uk^2 ? Uk Uj [gkj sin(?kj)?bkj cos(?k
    linedata(n,7) = -b(k,j)*busdata(k,5)^2 - busdata(k,5) *...
                    busdata(j,5) * ( g(k,j) * sin(busdata(k,6)-busdata(j,6))...
                    + b(k,j) * cos(busdata(k,6)-busdata(j,6)));
    linedata(n,8) = -b(j,k)*busdata(j,5)^2 - busdata(k,5) *...
                    busdata(k,5) * ( g(j,k) * sin(busdata(j,6)-busdata(k,6))...
                    + b(j,k) * cos(busdata(j,6)-busdata(k,6)));
end