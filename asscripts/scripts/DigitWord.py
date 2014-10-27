'''
Created on 27 oct. 2014

@author: gwendal
'''
import re


digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def toWord(digit):
    m = re.search('[0-9]', digit)
    return digits[int(m.group(0))]
