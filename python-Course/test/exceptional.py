import sys
def  convert(s):
    '''convert to an integer'''
    try :
       return int(s)
    except (ValueError, TypeError) as e:
        print("conversion error: {}".format(str(e)),
            file=sys.stderr)
        raise

from math import log 
def string_log(s):
    v = convert(s)
    return log(v)