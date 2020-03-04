import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-bs", help="path to bash executable script containing commands")
args = parser.parse_args()
script = args.bs

with open(script, 'r') as file:
    keyDict={}
    for line in file: 
        os.system(line) 