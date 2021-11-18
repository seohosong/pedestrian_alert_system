# Pedestrian Alert System

This repository includes codes and details for the project "Pedestrian Alert System" at YBIGTA, Yonsei University in South Korea.
The system alerts with audio especially for the blind when any pre-defined danger is approaching.

## Object detection

We implemented our system based on public yolov3 implementation. We used a public sidewalk walking video dataset from AiHub <https://aihub.or.kr/aidata/136>. 
The dataset provides 350K images during walking with human-annotated object labels.

## Audio alert

We obtained audio files for each object class with Google Cloud's TTS service in advance. Each audio file is played when it is considered as a danger.
In this project, for simplicity, we only applied our system on pre-recorded sidewalk walking video. However, with new devices with improved processing capacity, our system can easily be applied real-time.

## Defining dangerous situation

We assume the system is applied on a device hung on the user's neck. Without any sensor (e.g., ranging sensors like LIDAR), we define an object in below area in sight as a dangerous object approaching. When an object appears on the area longer than our predefined time, the system alerts with corresponding sound. 

<img src="https://github.com/seohosong/pedestrian_alert_system/blob/main/area.png" width="40%" height="30%" title="Alert Area" alt="Alert Area"></img>


## Links
[Model checkpoint] <https://drive.google.com/file/d/1hbtdXHNmXPMrA61jAN6F3FIjo1YTiCbn/view?usp=sharing>

[Demo Video] <https://drive.google.com/file/d/1SeUHLNBfOonhAly86W5Fi3baVF7mmh1A/view?usp=sharing>
