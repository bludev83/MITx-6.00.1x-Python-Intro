# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:36:46 2016

@author: WELG
"""
import os
curr_dir = os.path.dirname(os.path.realpath(__file__))  # gets the path of the script
os.chdir(curr_dir)  # changes the current path to the path of the script
data449 = []

file_name = input("Provide the name of a file of data ")

try:
    fh1 = open(file_name, 'r')
except IOError:
    print('CAN-NOT open', file_name)
else:
    for new in fh1:
        if new != '\n':
            addIt = new[:-1].split(',')  # remove trailing \n
            data449.append(addIt)
finally:
    fh1.close()  # close file even if fail
