import os
import subprocess
from moviepy.editor import *
from pydub import AudioSegment
#from pydub.playback import play

def insert_audio(detected, video_file='output/halfmin.mp4', audio_path='audios/', fps=30):

    #Each second, play audio for most frequent object in previous time period
    audio_files = []
    alert_cls = []
    sec = 0
    for i in range(0, len(detected), fps):
        names_dict = dict()
        if i > 0:
             new_sec = i / fps
             print('second :', new_sec)
             #silence = AudioSegment.silent(duration= 1000 * (new_sec - sec))
             prev = detected[i - fps: i]

             #Check detected objects among previous frames
             for frame in prev:
                 if frame is not None:
                     if frame not in names_dict:
                         names_dict[frame] = 0
                     else:
                         names_dict[frame] += 1

             #If there's any detected objects,
             if bool(names_dict):
                 cls = max(names_dict, key=names_dict.get)
                 

                 if len(alert_cls) < 3:
                     alert_cls.append(cls)
                     print('Detected cls :', cls)
                     audio_files.append(AudioSegment.silent(duration= 1000 * (new_sec - sec)))
                     audio_files.append(AudioSegment.from_mp3('audios/{}.mp3'.format(cls.strip())))
                     sec = new_sec


                 else:
                     if cls in alert_cls:
                         continue
                     else:
                         audio_files.append(AudioSegment.silent(duration= 1000 * (new_sec - sec)))
                         audio_files.append(AudioSegment.from_mp3('audios/{}.mp3'.format(cls.strip())))
                     alert_cls.pop(0)
                     alert_cls.append(cls)
             else:
                 alert_cls.append(None)
                 
    
    for i, audio in enumerate(audio_files):
        out = audio if i == 0 else out + audio
    out.export('concat.mp3', format='mp3')

    compo = AudioFileClip('concat.mp3')
    video = VideoFileClip(video_file)
    video = video.set_audio(compo)
    output = video.write_videofile('output.mp4')




                 #subprocess.check_output(['ffmpeg', '-y', '-i', '{}'.format(video_file), '-ss', '{}'.format(sec), '-i', 'audios/{}.mp3'.format(cls), '-map', '0:0', '-map', '1:0', '-c:v', 'copy', '-strict', '-2', 'output/halfmin.mp4'])

