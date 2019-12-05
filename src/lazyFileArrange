import sys, os, colorama, time
from colorama import Fore, Style
from os import listdir
from os.path import isfile, join
import shutil
import logging
import __main__ as main

start_time = time.time()

COMPRESSED = "Compressed"
EXECUTABLE = "Executables"
IMAGE = "Images"
VIDEO = "Videos"
AUDIO = "Audio"
MISC = "misc"
SCRIPTS = "scripts"
NOTES = "notes"

executables = ["exe", "jar", "msi"]
scripts = ["py", "c", "asm", "cs", "php", "java", "class"]
imgTypes = ["gif", "png", "jpg", "jpeg", "bmp", "svg"]
videoTypes = ["mp4", "mpeg", "avi"]
audioTypes = ["mp3", "wav"]

def log(msg):
    print("[" + Fore.GREEN + "+" + Style.RESET_ALL + "]MOVED : "+msg)

def log_exec_time():
    print("[" + Fore.CYAN + "*" + Style.RESET_ALL + "]Exec Time : "+ str(time.time() - start_time))

def info(msg):
    print("[" + Fore.RED + "x" + Style.RESET_ALL + "]RESULT : "+msg)

# determine os
if not os.name == 'posix': colorama.init()

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
            log( f + " --> " + dest)
        except:
            continue

        count += 1
print("-"*35)
info("Moved "+ str(count) + " files")
log_exec_time()
