import sys
import re, os
from inputParser import parseInputs

printlineNos = False
pattern = None
fromFile = False

argv = sys.argv[1:]
args, optionsMap = parseInputs(argv, 'qe:')

if "-q" in optionsMap:
    printlineNos = True

if "-e" not in optionsMap:
    print("Insufficient inputs: Regex pattern needed") 
    sys.exit(1)

pattern = optionsMap["-e"]

if args:
    fromFile = True
    filepaths = args

def printFromFile(filepaths):
    for filepath in filepaths:
        
        if not os.path.exists(filepath):
            print("Unexpected inputs: Invalid Path")
            sys.exit(1)
        
        file = open(filepath, "r")
        count = 0
        for line in file:
            count += 1
            if re.search(pattern, line):
                if printlineNos:
                    output = 'line no: %(number)s, %(line)s' % {"number": count, "line": line }
                else:
                    output = '%(line)s' % {"line": line }
                print(output)

def printFromStdIn():
    count = 0
    for line in sys.stdin:
        count += 1
        if re.search(pattern, line):
            if printlineNos:
                output = 'line no: %(number)s, %(line)s' % {"number": count, "line": line }
            else:
                output = '%(line)s' % {"line": line }
            print(output)

 
if fromFile:
    # process from filepath
    printFromFile(filepaths)
else:
    # process from std input
    printFromStdIn()