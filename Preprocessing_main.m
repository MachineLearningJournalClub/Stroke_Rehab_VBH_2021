% This script loads the given datasets and applies two steps of
% pre-processing: BP filtering (alpha and beta rythms) and epoch division.
% Every dataset should contain an EEG recording (y), a trigger vector(trig)
% and the sampling frequency (fs).
% The outputs are the filtered and unfiltered epochs, divided by right and
% left (respectiverly Dx and Sx), and a vector that indicates the order of
% the tasks. All these are saved in the 'Risultati' Folder.

%The epoch duration has to be modified inside the epochDivide function

clc
close all
clear all

%Create results folder
mkdir('Risultati');
%List of given datasets
S=dir(fullfile('Dati','*.mat'));


for c=1:size(S)
    %% File Loading
    filename=S(c).name;
    load(filename);
    
    filename
    
    %% Variable Initialization
    %Nyquist frequency
    fN=fs/2;
    %time vector
    t=(1:size(y,1))/fs;
    
    %variable initialization
    latency=[];
    type=[];
    duration=[];
    
    %% Trigger Vector 
    for i=2:length(trig)-1
        if trig(i)==1 && trig(i-1)==0
            latency=[latency;i];
            type=[type;'S'];
        elseif trig(i)==0 && trig(i-1)==1
            duration=[duration;(i-latency(end))];
        elseif trig(i)==-1 && trig(i-1)==0
            latency=[latency;i];
            type=[type;'D'];
        elseif trig(i)==0 && trig(i-1)==-1
            duration=[duration;(i-latency(end))];
        end
        
    end
    % removal of first chunk of recording, where tasks aren't actually
    % executed - up to 1s before start
    start=latency(1)-fs;
    y=y(start:end,:);
    
    % trigger vector
    latency=latency(1:length(duration))-start;
    type=type(1:length(duration));
    trigger=table(type,latency,duration);
    
    tr=zeros(1,length(type));
    tr(find(type=='S'))=1;
    tr(find(type=='D'))=-1;

%     %raw plot
%     figure,
%     for i=1:size(y,2)
%         plot(t(trigger.latency(1)-fs:end),y(trigger.latency(1)-fs:end,i)/max(y(trigger.latency(1)-fs:end,i))+i-1),hold on;
%     end
%     
    %% raw epochs division
    [DxRaw, SxRaw]=epochsDivide(y',trigger);
    
    %% BP filtering - [8 30]Hz
    
    % bandpass filtering for alpha-beta rythms, 8th order, butterworth
    [b,a]=butter(8,[8 30]/fN, 'bandpass');
%     figure,
%     freqz(b,a); %frequency response plot

    % actual filtering
    Y=filtfilt(b,a,y);
    
    %filtered plot
%     figure,
%     for i=1:size(Y,2)
%         plot(t(trigger.latency(1)-fs:end),Y(trigger.latency(1)-fs:end,i)/max(Y(trigger.latency(1)-fs:end,i))+i-1),hold on;
%     end
%     
    %% Filtered data epochs division
    [DxFilt, SxFilt]=epochsDivide(Y',trigger);
    
    %% Output saving
    save(fullfile(pwd,'Risultati',strcat('Processed_',filename)),'tr','DxRaw','SxRaw','DxFilt','SxFilt');
    
end  
    
