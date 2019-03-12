import os, sys, argparse, pickle
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression


parser = argparse.ArgumentParser(description="Test a maximum entropy model.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
parser.add_argument("datafile", type=str, help="The file name containing the features in the test data.")
parser.add_argument("modelfile", type=str, help="The name of the saved model file.")

args = parser.parse_args()

def testing():
    """
    opens a datafile and splits it into one-hot vector ngrams and class labels
    opens a modelfile and uses that as the trained file to run against the datafile and calculate the predicted probability, the predicted
    log probability and the perplexity
    :return:
    model_accuracy: accuracy of the trained model in predicting the class labels of the datafile
    model_perplexity: perplexity value of the trained model in predicting the class labels of the datafile
    """

    data_file = pd.read_pickle(args.datafile)
    class_label = data_file.iloc[:, -1].values.tolist()
    onehotngram = data_file.iloc[:, :-1]

    trained_model = pickle.load(open(args.modelfile, 'rb'))

    predicted_prob = trained_model.predict_proba(onehotngram)   #list of lists containing the probs [[0.03 0.05..],[]]
    predicted_log_prob = trained_model.predict_log_proba(onehotngram)
    model_accuracy = trained_model.score(onehotngram, class_label)

    max_prob = []
    for i in predicted_prob:
        max = np.max(i)
        max_prob.append(max)

    normalised_entropy = (-1/len(predicted_prob))*stats.entropy(max_prob)
    model_perplexity=2**normalised_entropy


    return model_accuracy, model_perplexity


if __name__ == '__main__':
    model_accuracy, model_perplexity = testing()

    testing()

    print("Loading data from file {}.".format(args.datafile))
    print("Loading model from file {}.".format(args.modelfile))
    #print("Testing {}-gram model.".format(args.ngram))
    print("Accuracy is:", model_accuracy)
    print("Perplexity is:", model_perplexity)
