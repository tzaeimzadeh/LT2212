import os, sys, argparse, re, pickle, gzip
import numpy as np
import pandas as pd
from scipy import stats

parser = argparse.ArgumentParser(description="Convert text to features")
parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int, default=0,
                    help="What line of the input data file to start from. Default is 0, the first line.")
parser.add_argument("-E", "--end", metavar="E", dest="endline", type=int, default=None,
                    help="What line of the input data file to end on. Default is None, whatever the last line is.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3,
                    help="The length of ngram to be considered (default 3).")
parser.add_argument("inputfile", type=str, help="The file name containing the text data.")
#parser.add_argument("outputfile", type=str, help="The name of the output file for the feature table.")

args = parser.parse_args()

def get_vocab():
    """

    :return:
    """
    corpus = []
    folder_path = os.listdir(args.inputfile)
    for filename in folder_path:
        file_path = os.path.join(args.inputfile, filename)
        #with open(file_path, 'r') as file:
        with gzip.open(file_path, 'r') as file:
                read_file = file.readline()
                print(read_file)
                normalised_text = re.sub(r"[^\s\w]", " ", read_file.lower())
                corpus.append(normalised_text)
    source, target = [], []
    source+=corpus[0]
    target+=corpus[1]

    print(len(source), len(target))
    #print(source[:100])

get_vocab()