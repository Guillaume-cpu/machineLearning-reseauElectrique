function JAC = jacobian(LF,Y,busdata)
nbus=size(busdata,1);
G=real(Y); B=imag(Y);
H = zeros(nbus,nbus);
N = H; J = H; L = H;

for m=1:nbus
    for n=1:nbus
        if m==n
            H(m,m)=-LF(m,3)-B(m,m)*busdata(m,5)*busdata(m,5);
            N(m,m)= LF(m,2)+G(m,m)*busdata(m,5)*busdata(m,5);
            J(m,m)= LF(m,2)-G(m,m)*busdata(m,5)*busdata(m,5);
            L(m,m)= LF(m,3)-B(m,m)*busdata(m,5)*busdata(m,5);
        else
            H(m,n)= busdata(m,5)*busdata(n,5)*(G(m,n)*sin(busdata(m,6)-busdata(n,6))-B(m,n)*cos(busdata(m,6)-busdata(n,6)));
            N(m,n)= busdata(m,5)*busdata(n,5)*(G(m,n)*cos(busdata(m,6)-busdata(n,6))+B(m,n)*sin(busdata(m,6)-busdata(n,6)));
            J(m,n)=-busdata(m,5)*busdata(n,5)*(G(m,n)*cos(busdata(m,6)-busdata(n,6))+B(m,n)*sin(busdata(m,6)-busdata(n,6)));
            L(m,n)= busdata(m,5)*busdata(n,5)*(G(m,n)*sin(busdata(m,6)-busdata(n,6))-B(m,n)*cos(busdata(m,6)-busdata(n,6)));
        end %if 
    end %for n 
end % for m

slack_bus=1;
%bus 1 
PU_bus = busdata(busdata(:,2)==1,1);
% Remove row and column corresponding to slack bus
H(slack_bus,:)=[ ]; H(:,slack_bus)=[ ]; 
% Remove row corresponding to slack bus 
N(slack_bus,:)=[ ];
% Remove columns corresponding to slack bus and PU-buses
N(:,sort([slack_bus;PU_bus]))=[ ]; 
% Remove rows corresponding to slack bus and PU-buses 
J(sort([slack_bus;PU_bus]),:)=[ ]; 
% Remove column corresponding to slack bus
J(:,slack_bus)=[ ];
%Remove rows and columns corresponding to slack bus and PU-buses
L(sort([slack_bus;PU_bus]),:)=[ ]; L(:,sort([slack_bus;PU_bus]))=[ ];

JAC=[H N ; J L];