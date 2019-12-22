import sys, os, time, platform, argparse
from colorama import Fore, Style
from os import listdir
from os.path import isfile, join
import shutil, logging, __main__ as main

start_time = time.time()

# Define File Categories
COMPRESSED = "Compressed"
EXECUTABLE = "Executables"
IMAGE = "Images"
VIDEO = "Videos"
AUDIO = "Audio"
MISC = "misc"
SCRIPTS = "scripts"
NOTES = "notes"

# Color for fancy printing
white = '\033[97m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
end = '\033[0m'
back = '\033[7;91m'
info = '\033[93m[!]\033[0m'
que = '\033[94m[?]\033[0m'
bad = '\033[91m[-]\033[0m'
good = '\033[92m[+]\033[0m'
run = '\033[97m[~]\033[0m'

# Define File Types
executables = ["exe", "jar", "msi"]
scripts = ["py", "c", "asm", "cs", "php", "java", "class"]
imgTypes = ["gif", "png", "jpg", "jpeg", "bmp", "svg"]
videoTypes = ["mp4", "mpeg", "avi"]
audioTypes = ["mp3", "wav"]

# determine os for colors
color = True
machine = sys.platform # Detecting the os of current system
checkplatform = platform.platform() # Get current version of OS
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    color = False
if checkplatform.startswith('Windows-10') and int(platform.version().split(".")[2]) >= 10586:
    color = True
    os.system('') # Enables ANSI
if not color:
    end = red = white = green = yellow = run = bad = good = info = que = ''

# fancy banner
print(''' %s

██╗          █████╗     ███████╗    ██╗   ██╗            ███████╗     ██████╗     ██████╗     ████████╗
██║         ██╔══██╗    ╚══███╔╝    ╚██╗ ██╔╝            ██╔════╝    ██╔═══██╗    ██╔══██╗    ╚══██╔══╝
██║         ███████║      ███╔╝      ╚████╔╝             ███████╗    ██║   ██║    ██████╔╝       ██║   
██║         ██╔══██║     ███╔╝        ╚██╔╝              ╚════██║    ██║   ██║    ██╔══██╗       ██║   
███████╗    ██║  ██║    ███████╗       ██║               ███████║    ╚██████╔╝    ██║  ██║       ██║   
╚══════╝    ╚═╝  ╚═╝    ╚══════╝       ╚═╝               ╚══════╝     ╚═════╝     ╚═╝  ╚═╝       ╚═╝   
                                                                                                       
%s ''' % (green, end))
print('\t'*9 + '%s v1.0 %s'% (red, end))

# logging stuff
def log(msg):
    print("[" + green + "+" + white + "]MOVED : "+msg)

def log_exec_time():
    time_elapsed = time.time() - start_time
    if time_elapsed < 1:
        time_elapsed *= 1000
        print("[" + yellow + "*" + white + "]Exec Time : "+ str(round(time_elapsed, 2)) + 'ms')
    else:
        print("[" + yellow + "*" + white + "]Exec Time : "+ str(round(time.time() - start_time, 4)) + 's')

def info(msg):
    print("[" + red + "x" + white + "]RESULT : "+ msg)

def print_line():
    print(red + '-'*44 + white)
    print()

# Processing Command Line Arguments
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='A simple python script to sort the files to the same-file category folders.')
parser.add_argument('-d', const=0, nargs='?', type=float, dest='delay', help= 'put delay second while moving files (default: 0)')
args = parser.parse_args()

if args.delay:
    delay = abs(args.delay)

count = 0
# list all file names
files = [f for f in listdir('.') if isfile(join('.', f))]
# print(files)

# Classify Files
for f in files:
    f_name = f.split(".")[0]
    if not f == main.__file__:
        f_type = f.split(".")[-1].lower()
        
        if f_type == "zip":
            folderType = COMPRESSED
        elif f_type in executables:
            folderType = EXECUTABLE
        elif f_type in imgTypes:
            folderType = IMAGE
        elif f_type in videoTypes:
            folderType = VIDEO
        elif f_type in audioTypes:
            folderType = AUDIO
        elif f_type in scripts:
            folderType = SCRIPTS
        elif f_type == "txt":
            folderType = NOTES
        else:
            folderType = MISC

        # Check if FOLDER exists
        if not os.path.exists(folderType):
            os.makedirs(folderType)
        
        # Move
        try:
            dest = shutil.move('./' + f, './' + folderType + "/")
            log( f + " --> " + dest + '\r')
            # check here after argparse < Dev >
            if not delay < 0:
                time.sleep(delay)
        except:
            continue
        count += 1

print_line()
info("Moved "+ str(count) + " files")
log_exec_time()
