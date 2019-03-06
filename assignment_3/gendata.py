import os, sys, argparse, pickle, argparse, re
import numpy as np
import pandas as pd


parser = argparse.ArgumentParser(description="Convert text to features")
parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int, default=0,
                    help="What line of the input data file to start from. Default is 0, the first line.")
parser.add_argument("-E", "--end", metavar="E", dest="endline", type=int, default=None,
                    help="What line of the input data file to end on. Default is None, whatever the last line is.")
parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3,
                    help="The length of ngram to be considered (default 3).")
parser.add_argument("inputfile", type=str, help="The file name containing the text data.")
parser.add_argument("outputfile", type=str, help="The name of the output file for the feature table.")

args = parser.parse_args()


def get_vocab():
    """
    opens file and creates a list of vocabulary. The vocabulary is then indexed in a dictionary
    :return:
    word_to_index: dictionary where keys are the words of the vocab, and the values are their index
    index_to_word: dictionary where the keys are the indexes of the words of the vocab, and the values are the corresponding words
    vocab: a list of the vocabulary of the corpus (no duplicates)
    corpus: a comma separates list of the words in the input file
    """
    corpus = []
    vocab=[]
    folder_path = os.listdir(args.inputfile)
    for filename in folder_path:
        file_path = os.path.join(args.inputfile, filename)
        with open(file_path, 'r') as file:
                read_file = file.readlines()
                normalised_text = re.sub(r"/[^\s]+", '', "".join(read_file))
                corpus=normalised_text.split()
                vocab=set(normalised_text.split())  #Total: 180163 words, set to remove duplicates len = 17179

    word_to_index, index_to_word = {}, {}
    word_to_index.update({word: index for index, word in enumerate(vocab)})
    index_to_word.update({index: word for index, word in enumerate(vocab)})

    return word_to_index, index_to_word, vocab, corpus


def encode_corpus():
    """
    creates a smaller corpus using command line input, and uses this corpus to create a list of index encoding
    corresponding to the indexes of the vocabulary items.
    :return:
    corpus_encoding: a comma separated list containing the index encodings associated with each word of the corpus
    """
    smaller_corpus = corpus[args.startline:args.endline]

    corpus_encoding = []
    for word in smaller_corpus:
        corpus_encoding.append(word_to_index[word])

    return corpus_encoding


def one_hot_encoding():
    """
    creates a list of binary one-hot encodings representing the corpus
    :return:
    one_hot_corpus: a list containing lists of binary one-hot encoding, each of which corresponds to each word of the corpus
    """
    one_hot_corpus = []

    for encoding in corpus_encoding:
        onehot_words = [0 for x in range(len(vocab))]  # create a list of zeros the length of the vocab
        onehot_words[encoding] = 1
        one_hot_corpus.append(onehot_words)

    return one_hot_corpus


def onehot_ngram(corpus, n):
    """
    turns one-hot encodings representing a corpus into a list of ngrams. The n-1 representations are concatenated, whilst the
    last word (n) is swapped for the actual word instead of its one-hot encoding
    :return:
    onehot_ngram_word: a comma separated list containing the concatenated n-1 representation of the ngrams with the nth value
    being the actual word rather than its one-hot representation -> [ [n-2+n-1, "n"] , [0,0,0,1,0,0,"n"] ]

    onehot_ngram_dataframe: a pandas dataframe where each row is an ngram, represented as one hot vectors, with the last column
    containing the actual word rather than its one-hot representation
    """
    one_hot_ngram =[]
    for onehot in range(len(corpus)-n+1):
        one_hot_ngram.append(corpus[onehot:onehot+n])

    onehot_ngram_word = []
    for ohngram in one_hot_ngram:
        index = ohngram[-1].index(1)
        ohngram[0]+=ohngram[1]      #need to edit this to be n not hard coded numbers #ohngram[1] still there, don't use full ohngram
        i_to_w = index_to_word[index]
        ohngram[0].append(i_to_w)   #the one hot vectors each have an individual column, rather than be in a list in one column
        onehot_ngram_word.append(ohngram[0])

    onehot_ngram_dataframe = pd.DataFrame(onehot_ngram_word).to_pickle(path=args.outputfile)

    return onehot_ngram_word


if __name__ == '__main__':
    word_to_index, index_to_word, vocab, corpus = get_vocab()
    corpus_encoding = encode_corpus()
    onehot_ngram(one_hot_encoding(), args.ngram)

    print("Loading data from file {}.".format(args.inputfile))
    print("Starting from line {}.".format(args.startline))
    if args.endline:
        print("Ending at line {}.".format(args.endline))
    else:
        print("Ending at last line of file.")

    print("Constructing {}-gram model.".format(args.ngram))
    print("Writing table to {}.".format(args.outputfile))
    # THERE ARE SOME CORNER CASES YOU HAVE TO DEAL WITH GIVEN THE INPUT

