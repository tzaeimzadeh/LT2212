import argparse, collections, re, os, pandas
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import TruncatedSVD


parser = argparse.ArgumentParser()
parser.add_argument('f', metavar='filename', help='takes the name of the file to be opened')
parser.add_argument('o', metavar='outputfile', help='takes the name of the output file for the matrix')
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
    #len(vocab_dict) = 11222
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
    Uses argparse parser to create a vector with only the n most frequent words, perform tf-idf transformation on the n-most-frequent vector
    and transform the tf-idf vector using Truncated SVD operation with dimensionality m (to reduce its dimensionality), which is then written to a csv file
    :param vocab: dictionary with the keys as the vocab, and values set to 0
    :param counts: dictionary with the keys as the filenames, and the values as a dictionary of vocab frequency
    :return top_vector: sorted dataframe vector of the n most frequent words
    """

    vector = pandas.DataFrame(data=counts.values(), columns=vocab.keys(), index=counts.keys())
    #doc_vectors = vector.drop_duplicates()
    #print(vector)
    #print("Duplicated files to be dropped:", vector[0].duplicated().index.tolist())
    vector.loc['Total'] = vector.sum(axis=0)

    if args.top:
        sorted_vector = vector.sort_values(by="Total", axis=1, ascending=False)
        top_vector = sorted_vector.drop(sorted_vector.columns[args.top:], axis=1)
        #print(top_vector)

    if args.tfidf:
        tfidf_vector = TfidfTransformer().fit_transform(X=top_vector[:-1]).toarray()    #can not use args.tfidf without calling args.top first
        #print(tfidf_vector)

    if args.svd:
        svd_vector = pandas.DataFrame(TruncatedSVD(n_components=args.svd).fit_transform(X=tfidf_vector), index=counts.keys()).to_csv(path_or_buf=args.o)
        #print(svd_vector)

    return top_vector


vectorise(generate_vocab(), generate_counts())
