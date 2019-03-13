import os, sys, argparse, pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


parser = argparse.ArgumentParser(description="Train a maximum entropy model.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("datafile", type=str, help="The file name containing the features.")
parser.add_argument("modelfile", type=str, help="The name of the file to which you write the trained model.")

args = parser.parse_args()

def train_logisticreg():
    """
    opens datafile, and seperates it into a dataframe consisting of the one-hot vector representations of the ngram (Wn-1), and a list consisting
    of the word representing the class label of the ngram. Runs the logistic regression module and fits the ngrams to the labels,
    and uses the pickle module to maintain the fitted model for future use
    """

    data_file = pd.read_pickle(args.datafile)
    data_file = data_file[data_file.iloc[:,-1].notnull()]   #there are class labels with value None which the Logistic Regression function can't handle
    class_label= data_file.iloc[:,-1].values.tolist()
    onehotngram = data_file.iloc[:,:-1]
    fitted_log_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs').fit(X=onehotngram, y=class_label)
    pickled_logreg = pickle.dump(fitted_log_reg, open(args.modelfile, 'wb'))


train_logisticreg()


print("Loading data from file {}.".format(args.datafile))
print("Training {}-gram model.".format(args.ngram))
print("Writing table to {}.".format(args.modelfile))
