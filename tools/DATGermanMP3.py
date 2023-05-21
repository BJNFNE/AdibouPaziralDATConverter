# This Converter converts the DAT Files (QuickTime Movies) into MP3 Files in German.

import os

path = './Data/'
for filename in os.listdir(path):
    if (filename.endswith(".dat")): #or .avi, .mpeg, whatever.
        os.system(f'ffmpeg -i ./Data/Resource01.dat -c:v libx264 -c:a ac3 -crf 20 -map 0:v:0 -map 0:a:1 -vf fps=fps=25 Resource01de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource02.dat -c:v libx264 -c:a ac3 -crf 20 -map 0:v:0 -vf fps=fps=25 Resource02de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource03.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource03de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource04.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource04de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource05.dat -c:v libx264 -c:a ac3 -crf 20 -map 0:v:0 -map 0:a:1 -vf fps=fps=25 Resource05de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource06.dat -c:v libx264 -c:a ac3 -crf 20 -map 0:v:0 -map 0:a:1 -vf fps=fps=25 Resource06de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource07.dat -c:v libx264 -c:a ac3 -crf 20 -map 0:v:0 -map 0:a:1 -vf fps=fps=25 Resource07de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource08.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource08de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource09.dat -c:v libx264 -c:a ac3 -crf 20 -map 0:v:0 -map 0:a:1 -vf fps=fps=25 Resource09de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource10.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource10de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource11.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource11de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource12.dat -c:v libx264 -c:a ac3 -crf 20 -map 0:v:0 -map 0:a:1 -vf fps=fps=25 Resource12de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource13.dat -c:v libx264 -c:a ac3 -crf 20 -map 0:v:0 -map 0:a:1 -vf fps=fps=25 Resource13de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource14.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource14de.mp3')
        os.system(f'ffmpeg -i ./Data/Resource15.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource15de.mp3')
