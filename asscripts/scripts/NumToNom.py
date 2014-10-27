'''
Created on 20 oct. 2014

@author: gwlemoul
'''
from os.path import sys

from DigitWord import toWord


def main(args):
    inpath = args[1]
    outpath = args[2]
    firstline = True
    inputfile = open(inpath, 'r')
    outputfile = open(outpath, 'w')
    for line in inputfile:
        if firstline:
            firstline = False
            outputfile.write(line + '\n')
        else:
            values = line.split(',')
            processed_values = map((lambda x : x.strip()), values)
            if len(processed_values) is 17:
                processed_values[16] = toWord(processed_values[16])
                newline = ','.join(processed_values)
                outputfile.write(newline + '\n')
    outputfile.close()
    inputfile.close()
    

if __name__ == '__main__':
    main(sys.argv)