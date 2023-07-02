#
#
# Simple script to make a txt file with all the songs from a folder.
# Made it because JMusicBot can play local files but needs a .txt file with all the paths to said files
#
#

import os

directory = input('Input path to folder with music:\n')

def make_playlist(dir,playlist_file,mode):
    try:
        playlist = open(f'{playlist_file}.txt',f'{mode}',encoding='utf-8')
        for filename in os.listdir(dir):
                file = os.path.join(dir, filename)
                if os.path.isfile(file):
                    playlist.write(f'{file}\n')
        print('Succsessfuly made a playlist file!')
    except:
        print('Something went wrong ...')

def get_filename(dir):
    dir = directory.split('/')
    if dir[-1]:
        filename = dir[-1]
    else:
        filename = dir[-2]
    return filename

try:
    filename = get_filename(directory)
    f = open(f'{filename}.txt','x')
    f.close()
    make_playlist(directory,filename,'a')
except:
    filename = get_filename(directory)
    choice = input('File alredy exsist, do you want to override it? Y/N \n')
    if choice.lower() == 'y':
        make_playlist(directory,filename,'w')
    else:
        print('No changes were made')
