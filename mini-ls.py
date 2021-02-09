import sys, getopt
import os, time, pwd
from inputParser import parseInputs

includeSubfolders = False
filepaths = []

argv = sys.argv[1:]
args, optionsMap = parseInputs(argv, 'r')

if args:
    filepaths = args

if not filepaths:
    filepaths.append(os.getcwd()) 

if "-r" in optionsMap:
    includeSubfolders = True

for filepath in filepaths:
    
    if not os.path.exists(filepath):
        print("Unexpected inputs: Invalid Path")
        sys.exit(1)
    
    for dirpath, _ , _  in os.walk(filepath):
        
        dirpath = os.path.abspath(dirpath)
        stats = os.stat(dirpath)
        print('Path: ({}):'.format(dirpath))
        print('Owner', pwd.getpwuid(stats.st_uid).pw_name)
        print('Permissions:', oct(stats.st_mode)[-3:])
        print('Last modified:', time.ctime(stats.st_mtime))
        print('\n')

        if not includeSubfolders:
            break