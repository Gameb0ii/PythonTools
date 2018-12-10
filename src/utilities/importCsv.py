#!/usr/bin/python3

import os
import xml.etree.ElementTree as ET
from datetime import datetime
import hashlib
import pandas as pd
import csv
import sys

#get import file
input = str(sys.argv[len(sys.argv)-1])
print(f'file: ', input)

#read in csv & print rows
cwd = os.getcwd()
print(cwd)
with open(cwd+'/'+input) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} , {row[1]} , {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
