import os

path = './Data/'
for filename in os.listdir(path):
    if (filename.endswith(".dat")): #or .avi, .mpeg, whatever.
        os.system(f'ffmpeg -i ./Data/Resource01.dat -vf fps=fps=25 Resource01.mp4')
        os.system(f'ffmpeg -i ./Data/Resource02.dat -vf fps=fps=25 Resource02.mp4')
        os.system(f'ffmpeg -i ./Data/Resource03.dat -vf fps=fps=25 Resource03.mp4')
        os.system(f'ffmpeg -i ./Data/Resource04.dat -vf fps=fps=25 Resource04.mp4')
        os.system(f'ffmpeg -i ./Data/Resource05.dat -vf fps=fps=25 Resource05.mp4')
        os.system(f'ffmpeg -i ./Data/Resource06.dat -vf fps=fps=25 Resource06.mp4')
        os.system(f'ffmpeg -i ./Data/Resource07.dat -vf fps=fps=25 Resource07.mp4')
        os.system(f'ffmpeg -i ./Data/Resource08.dat -vf fps=fps=25 Resource08.mp4')
        os.system(f'ffmpeg -i ./Data/Resource09.dat -vf fps=fps=25 Resource09.mp4')
        os.system(f'ffmpeg -i ./Data/Resource10.dat -vf fps=fps=25 Resource10.mp4')
        os.system(f'ffmpeg -i ./Data/Resource11.dat -vf fps=fps=25 Resource11.mp4')
        os.system(f'ffmpeg -i ./Data/Resource12.dat -vf fps=fps=25 Resource12.mp4')
        os.system(f'ffmpeg -i ./Data/Resource13.dat -vf fps=fps=25 Resource13.mp4')
        os.system(f'ffmpeg -i ./Data/Resource14.dat -vf fps=fps=25 Resource14.mp4')
        os.system(f'ffmpeg -i ./Data/Resource15.dat -vf fps=fps=25 Resource15.mp4')
