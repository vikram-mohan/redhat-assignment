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
    for dirpath, _ , _  in os.walk(filepath):
        
        stats = os.stat(dirpath)
        print('Path Name ({}):'.format(dirpath))
        print('Owner', pwd.getpwuid(stats.st_uid).pw_name)
        print('Permissions:', oct(stats.st_mode)[-3:])
        print('Last modified:', time.ctime(stats.st_mtime))
        
        if not includeSubfolders:
            break