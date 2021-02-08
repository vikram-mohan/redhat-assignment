import sys, getopt
import os, shutil
from inputParser import parseInputs

prettyPrint = False
filepaths = []

argv = sys.argv[1:]
args, optionsMap = parseInputs(argv, 'h')

if args:
    filepaths = args

if not filepaths:
    filepaths.append(os.getcwd()) 

if "-h" in optionsMap:
    prettyPrint = True

def convert(size):
       return size/(1024*1024)

units = {'units': 'BYTES'}

for filepath in filepaths:
    for dirpath, _ , _  in os.walk(filepath):

        total, used, free = shutil.disk_usage(filepath)
        args = {'arg1':total, 'arg2':used, 'arg3':free}
        
        if prettyPrint:
            args = {'arg1':convert(total), 'arg2':convert(used), 'arg3':convert(free)}
            units['units'] =  'MB'
        
        output = '''
        Total Space: {arg1} {units}
        Used Space: {arg2} {units}
        Free Space: {arg3} {units}'''.format(**args, **units)
    
        print(output)
        break


