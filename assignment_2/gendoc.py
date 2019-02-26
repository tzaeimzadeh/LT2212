import argparse, collections, re, os, pandas, numpy
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import TruncatedSVD


parser = argparse.ArgumentParser()
parser.add_argument('f', metavar='filename', help='takes the name of the file to be opened')
#parser.add_argument('o', metavar='outputfile', help='takes the name of the output file for the matrix')
parser.add_argument('-B', '--basevocab', dest='top', type=int,
                    help='specifies the number of most frequent words to be used (requires an integer)')
parser.add_argument('-T', '--tfidf', dest='tfidf', action="store_true",
                    help='loaded raw counts are transformed into tf-idf values')
parser.add_argument('-S', '--svd', dest='svd', type=int,
                    help='term-document matrix transformed into a document matrix with a feature space of dimensionality n (requires an integer)')

args = parser.parse_args()


def generate_vocab():
    """
    Opens folder and reads the files from the subfolders, performs simple normalisation on the files and creates a dictionary of the vocabulary
    :return vocab_dict: dictionary
        keys are the vocabulary, and values are set to 0
    """

    vocab_dict = {}
    folder_path = os.listdir(args.f)
    for subfolder in folder_path:
        subfolder_path = os.path.join(args.f, subfolder)
        for filename in os.listdir(subfolder_path):
            with open(os.path.join(subfolder_path, filename), 'r') as file:
                read_file = file.read()
                normalised_text = re.sub(r"[^\s\w]", " ", read_file.lower())
                vocab = normalised_text.split()     #.split() creates a list of strings
                vocab_dict.update({i: 0 for i in vocab})
    return vocab_dict


def generate_counts():
    """
    Opens folder and reads the files from the subfolders, performs simple normalisation on the files
    and creates a dictionary of frequency of words in the vocabulary, whilst keeping tack of the file names
    :return counts_dict: dictionary
        keys = "file/subfolder/filename", values = dictionary of vocabulary frequencies per file
    """

    counts_dict = {}
    folder_path = os.listdir(args.f)
    for subfolder in folder_path:
        subfolder_path = os.path.join(args.f, subfolder)
        for filename in os.listdir(subfolder_path):
            doc_path = os.path.join(subfolder_path, filename)
            with open(doc_path, 'r') as file:
                read_file = file.read()
                normalised_text = re.sub(r"[^\s\w]", " ", read_file.lower())
                counts_dict.update({doc_path: collections.Counter(normalised_text.split())})
    #print(counts_dict.get('file/crude/article560.txt'))

    vocab = generate_vocab()
    for value in counts_dict.values():
        for k in vocab.keys():
            if k not in value.items():
                value.update({k: 0})

    #print(counts_dict.get('file/crude/article560.txt'))
    return counts_dict


def vectorise(vocab, counts):
    """
    Creates a dataframe from the vocabulary and the frequencies
    :param vocab: dictionary with the keys as the vocab, and values set to 0
    :param counts: dictionary with the keys as the filenames, and the values as a dictionary of vocab frequency
    :return sorted_vector: sorted dataframe vector of the vocabulary (not including the last row, which was an added row of Total values of each column)
            1160 files, 11222 words
    """

    vector = pandas.DataFrame(data=counts.values(), columns=vocab.keys(), index=counts.keys())
    #doc_vectors = vector.drop_duplicates()
    #print("Duplicated files to be dropped:", vector[0].duplicated().index.tolist())
    vector.loc['Total'] = vector.sum(axis=0)
    sorted_vector = vector.sort_values(by="Total", axis=1, ascending=False)

    return sorted_vector[:-1]


def most_frequent(vector):
    """
    drops the infrequent words from the vector matrix
    :param vector: sorted vector matrix of the vocabulary
    :return top_vector: vector matrix of the most n frequent words
    """

    top_vector = vector.drop(vector.columns[args.top:], axis=1)
    return top_vector


def tfidf_transform(vector):
    """
    performs tf-idf transformation on a vector matrix
    :param vector: sorted vector matrix of the vocabulary
    :return tfidf_vector: dataframe of the tf-idf transformed vector matrix
    """

    tfidf_vector = pandas.DataFrame(TfidfTransformer().fit_transform(X=vector), index=indexes.keys()) #.toarray()
    return tfidf_vector


def svd_transform(vector, indexes):
    """
    transforms a vector matrix using Truncated SVD operation with dimensionality m (to reduce its dimensionality)
    :param vector: sorted vector matrix of the vocabulary
    :param indexes: dictionary keys containing the filenames and their file-path
    :return svd_vector: dataframe of the reduced vector matrix using truncatedSVD transformation
    """

    svd_vector = pandas.DataFrame(TruncatedSVD(n_components=args.svd).fit_transform(X=vector), index=indexes.keys())     #.to_csv(path_or_buf=args.o)
    return svd_vector


def output():
    """
    uses the argeparse arguments/parser to write csv files based on which arguments are specified when running the file
    """

    if args.top and not args.tfidf and not args.svd:
        most_frequent(vector).to_csv(path_or_buf="top{}_vectorfile.csv".format(args.top))

    elif args.top and args.tfidf and not args.svd:
        tfidf_transform(most_frequent(vector)).to_csv(path_or_buf="tfidf_top{}.csv".format(args.top))

    elif args.top and args.tfidf and args.svd:
        svd_transform(tfidf_transform(most_frequent(vector)), indexes).to_csv(path_or_buf="svd{}_tfidf_topn.csv".format(args.svd))

    elif args.tfidf and not args.top and not args.svd:
        tfidf_transform(vector).to_csv(path_or_buf="tfidf.csv")

    elif args.svd and not args.top and not args.tfidf:
        svd_transform(vector, indexes).to_csv(path_or_buf="svd{}_vector.csv".format(args.svd))

    elif args.tfidf and args.svd and not args.top:
        svd_transform(tfidf_transform(vector), indexes).to_csv(path_or_buf="svd{}_tfidf.csv".format(args.svd))

    else:
        vector.to_csv(path_or_buf="vectorfile.csv")


if __name__ == '__main__':
    vector = vectorise(generate_vocab(), generate_counts())
    indexes = generate_counts()

    output()