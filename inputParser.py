import getopt
import sys

def parseInputs(arguments, pattern):
    
    optionsMap = {}
    
    try:
        opts, args = getopt.getopt(arguments, pattern)
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        optionsMap[opt] = arg
    
    return args, optionsMap