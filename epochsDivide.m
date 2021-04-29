%This function returns two matrices whose dimensions correspond to:
%[#epochs, #channels, time points], divided by right(dx) and left(sx)
%tasks. The inputs are the EEG recording and the trigger vector.

function [Dx, Sx]=epochsDivide(M,trigger) %M is the EEG recording matrix [#channels, time points]
% tasks counter
dxcount=sum(trigger.type=='D');
sxcount=sum(trigger.type=='S');
%epochs counter
id=1;
is=1;
% epochs' matrices= [#epochs, #channels, time points]
% ** Actually it's set for acquiring the first 2 seconds after the start
% command (2 secs after the trigger): change below the number of time
% points if you want to change the epoch duration **
Dx=zeros(dxcount,size(M,1),max(trigger.duration)-(6*256));
Sx=zeros(sxcount,size(M,1),max(trigger.duration)-(6*256));
% ** Actually it's set for acquiring the first 2 seconds after the start
% command (2 secs after the trigger): change below the ending time point if 
% you want to change the epoch duration **
for i=1:length(trigger.latency)
    % if right trigger starts, put epoch in Dx
    if trigger.type(i)=='D'
        Dx(id,:,:)=M(:,trigger.latency(i)+(2*256):trigger.latency(i)+trigger.duration(i)-(4*256)-1);
        id=id+1; %update counter
    % if left trigger starts, put epoch in Sx
    elseif trigger.type(i)=='S'
        Sx(is,:,:)=M(:,trigger.latency(i)+(2*256):trigger.latency(i)+trigger.duration(i)-(4*256)-1);
        is=is+1; %update counter
    end
end
