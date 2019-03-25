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

def preprocess_file():
    """
    Opens files and normalises text files, by lower casing, tokenising and removing empty strings. Compares each line and truncates
    the longer line to match the shortest sentence length.
    :return:
        source_lang = list of lists, with each sublist representing a line in the source language file (French)
        target_lang = list of lists, with each sublist representing a line in the target language file (English)
    """

    source_lang = []
    target_lang = []

    folder_path = os.listdir(args.inputfile)    #get file names from the source folder
    with open(os.path.join(args.inputfile, folder_path[0]), 'r') as target_file, \
            open(os.path.join(args.inputfile, folder_path[1]), 'r') as source_file:
        for s_line, t_line in zip(source_file, target_file):                    #https://stackoverflow.com/questions/19007383/compare-two-different-files-line-by-line-in-python
            preprocess_source = re.sub(r"[^\s\w]", " ", s_line.lower()).split(" ")
            preprocess_target = re.sub(r"[^\s\w]", " ", t_line.lower()).split(" ")
            preprocess_source = [x for x in preprocess_source if x]             #remove empty strings: https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
            preprocess_target = [x for x in preprocess_target if x]
            shortest = min(len(preprocess_source), len(preprocess_target))
            truncated_source = preprocess_source[:shortest]
            truncated_target = preprocess_target[:shortest]
            source_lang.append(truncated_source)
            target_lang.append(truncated_target)

    smaller_source_lang = source_lang[args.startline:args.endline]
    smaller_target_lang = target_lang[args.startline:args.endline]

    with open("source-language-".format(args.outputfile)) as source, open("target-language-".format(args.outputfile)) as target:
        source.write(smaller_source_lang)
        target.write(smaller_target_lang)

    return source_lang, target_lang


preprocess_file()
