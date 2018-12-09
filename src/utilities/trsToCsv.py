#!/usr/bin/python3

import os
import xml.etree.ElementTree as ET
from datetime import datetime
import hashlib
import pandas as pd

#step 1
TRANSCRIPT_FOLDER = "src/test/resources/mcd/trs/"

#step 2
REPLACEMENTS = {
    "\n": ""
}

#step 3
def documentKey(timestamp,doc):
    timePart = datetime.fromtimestamp(timestamp).strftime("%Y%m%d")
    hashPart = hashlib.md5(doc.encode('utf-8')).hexdigest()[-6:]
    return timePart + "-" + hashPart

#step 4
documents = []
allelements = []
for file in os.listdir(TRANSCRIPT_FOLDER):
    try:
        path = TRANSCRIPT_FOLDER + "/" + file
        tree = ET.parse(path)
        root = tree.getroot()
        elements = []
        for text in root.itertext():
            if not text.isspace():
                for rep,new in REPLACEMENTS.items():
                    text = text.replace(rep, new)
                elements.append(text)
                allelements.append(text)
        doc = ", ".join(elements)
        timestamp = os.path.getmtime(path)
        key = file # documentKey(timestamp, doc)
        documents.append([key,doc])
    except Exception as e:
        print(f"Error parsing {file}. Skipping.")
        continue

#step 5
print(documents)

#step 6
documents

df = pd.DataFrame(documents)

#import csv

#with open("/tmp/180911-transcripts.csv", 'w') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    wr.writerow(documents)

#step 7
# this captures all utterances in an order

df = pd.DataFrame.from_records(documents)
df.to_csv("allorders.csv", index=None, header=None)

#step 9
# this captures

#print(allelements)

import csv

with open("ref-txtonly.csv", 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(allelements)

