# This Converter converts the DAT Files (QuickTime Movies) into MP3 Files in French.

import os

path = './Data/'
for filename in os.listdir(path):
    if (filename.endswith(".dat")): # Only use for DAT Files.
        os.system(f'ffmpeg -i ./Data/Resource01.dat -c:v libx264 -c:a ac3 -crf 20  -vf fps=fps=25 Resource01.mp3')
        os.system(f'ffmpeg -i ./Data/Resource02.dat -c:v libx264 -c:a ac3 -crf 20  -vf fps=fps=25 Resource02.mp3')
        os.system(f'ffmpeg -i ./Data/Resource03.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource03.mp3')
        os.system(f'ffmpeg -i ./Data/Resource04.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource04.mp3')
        os.system(f'ffmpeg -i ./Data/Resource05.dat -c:v libx264 -c:a ac3 -crf 20  -vf fps=fps=25 Resource05.mp3')
        os.system(f'ffmpeg -i ./Data/Resource06.dat -c:v libx264 -c:a ac3 -crf 20  -vf fps=fps=25 Resource06.mp3')
        os.system(f'ffmpeg -i ./Data/Resource07.dat -c:v libx264 -c:a ac3 -crf 20  -vf fps=fps=25 Resource07.mp3')
        os.system(f'ffmpeg -i ./Data/Resource08.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource08.mp3')
        os.system(f'ffmpeg -i ./Data/Resource09.dat -c:v libx264 -c:a ac3 -crf 20  -vf fps=fps=25 Resource09.mp3')
        os.system(f'ffmpeg -i ./Data/Resource10.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource10.mp3')
        os.system(f'ffmpeg -i ./Data/Resource11.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource11.mp3')
        os.system(f'ffmpeg -i ./Data/Resource12.dat -c:v libx264 -c:a ac3 -crf 20  -vf fps=fps=25 Resource12.mp3')
        os.system(f'ffmpeg -i ./Data/Resource13.dat -c:v libx264 -c:a ac3 -crf 20  -vf fps=fps=25 Resource13.mp3')
        os.system(f'ffmpeg -i ./Data/Resource14.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource14.mp3')
        os.system(f'ffmpeg -i ./Data/Resource15.dat -c:v libx264 -c:a ac3 -crf 20 -vf fps=fps=25  Resource15.mp3')
