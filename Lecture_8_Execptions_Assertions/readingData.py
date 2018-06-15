# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:36:46 2016

@author: WELG
"""

data44 = []

file_name = input("Provide the name of a file of data ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannotTT open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')  # remove trailing \n
            data44.append(addIt)
finally:
    fh.close()  # close file even if fail
