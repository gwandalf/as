'''
Created on 26 oct. 2014

@author: gwendal
'''
import re
import sys

from DigitWord import toWord


def main(args):
    inpath = args[1]
    outpath = args[2]
    inputfile = open(inpath, 'r')
    outputfile = open(outpath, 'w')
    process(inputfile, outputfile)
    inputfile.close()
    outputfile.close()
    
    
def process(infile, outfile):
    '''
    Scans infile to print data in csv format in outfile.
    '''
    first_pass = True
    point_array = []
    cur_digit = None
    outfile.write("X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5, X6, Y6, X7, Y7, X8, Y8, C\n")
    for line in infile:
        if ".SEGMENT DIGIT" in line:
            if not first_pass:
                writeDataRow(point_array, cur_digit, outfile)
                point_array = []
            # new digit to be recorded
            line_tab = line.split()
            cur_digit = toWord(line_tab[len(line_tab)-1])
            first_pass = False
        point_line = re.match("^\s*[0-9]+\s+[0-9]+\s*$", line)
        if point_line is not None:
            point_tab = line.split()
            point_array.append(point_tab)
    writeDataRow(point_array, cur_digit, outfile)
            
            
def writeDataRow(points, digit, outfile):
    '''
    Writes the point list related to the digit in the output file.
    '''
    data_row = sample(points)
    data_row.append(digit)
    csv_line = ','.join(data_row)
    outfile.write(csv_line + '\n')
            
            
def sample(points):
    '''
    Retrieves 8 points and normalizes them.
    '''
    sampled = []
    res = []
    min_x = points[0][0]
    min_y = points[0][1]
    max_x = 0
    max_y = 0
    base_index = len(points)/8
    for index in range(0, 8):
        point = points[base_index * index]
        point[0] = int(point[0])
        point[1] = int(point[1])
        sampled.append(point)
        if min_x > point[0]:
            min_x = point[0]
        if min_y > point[1]:
            min_y = point[1]
        if max_x < point[0]:
            max_x = point[0]
        if max_y < point[1]:
            max_y = point[1]
    for point in sampled:
        point[0] = 100*(point[0]-min_x)/(max_x-min_x)
        point[1] = 100*(point[1]-min_y)/(max_y-min_y)
        res.append(str(point[0]))
        res.append(str(point[1]))
    return res
    

if __name__ == '__main__':
    main(sys.argv)