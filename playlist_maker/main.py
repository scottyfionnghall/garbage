#
#
# Simple script to make a txt file with all the songs from a folder.
# Made it because JMusicBot can play local files but needs a .txt file with all the paths to said files
#
#

import os
import pathlib
import platform
directory = input('Input path to folder with music:\n').strip()
exten = ['.flac','.mp3','.m4a','.wav','.wma','.wmc']
# make_playlist opens created file and goes through a designated folder to add all the songs path to said file
# also, it checks to add only audio files by comparing file extention to exten variable which contains popular audio file extention
def make_playlist(dir,playlist_file,mode):
    try:
        playlist = open(f'{playlist_file}.txt',f'{mode}',encoding='utf-8')
        for filename in os.listdir(dir):
                file = os.path.join(dir, filename)
                if os.path.isfile(file) and pathlib.Path(filename).suffix in exten:
                    playlist.write(f'{file}\n')
        print('Succsessfuly made a playlist file!')
    except:
        print('Something went wrong ...')
# get_filename get's a folder name to use it as a playlist file name
# it checks what OS user is running to split inputed folder path into a list
# then we get the last element of the list which is a folder name with all the songs
# if user used a slash at the end of the path, we get second last element because last element will be empty
def get_filename(dir):
    if platform.system() == 'Linux':
        dir = directory.split('/')
    else:
        dir = directory.split('\\')
    if dir[-1]:
        filename = dir[-1]
    else:
        filename = dir[-2]
    return filename
# we try to create a file, 'x' flag will give an error if file alredy exists
# using that, we can assertain that if we get an error then file already exists and we ask user does they want to override it
# if file is created we pass 'a' flag to append files to the file, if file already existted we pass 'w' flag to override everything in the file
try:
    filename = get_filename(directory)
    f = open(f'{filename}.txt','x')
    f.close()
    make_playlist(directory,filename,'a')
except:
    choice = input('File alredy exsist, do you want to override it? Y/N \n')
    if choice.lower() == 'y':
        filename = get_filename(directory)
        make_playlist(directory,filename,'w')
    else:
        print('No changes were made')
