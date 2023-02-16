import glob
import sys
import pandas

class single_data_collector:
    def __init__(self):
        format = None

    def read(self, Filename, format):
        files=glob.glob('*.py', recursive=True)
        for x in files:
            if(x.endswith(format + '.py')):
                sys.argv = [Filename]
                return exec(open(x).read())