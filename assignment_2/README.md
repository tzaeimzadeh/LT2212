# LT2212 V19 Assignment 2

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Tala Zaeimzadeh

## Additional instructions

Document here additional command-line instructions or other details you want us to know about running your code.

## File naming convention

The output file naming convention is the name of the transformation carried out on it. if multiple transformations carried out, then the later transformation is first followed by the earlier transformation (e.g. if no vocabulary restriction was imposed, but tf-idf was applied, with truncated SVD to 100 dimensions, then the file would be called "svd100_tfidf.csv"). if no transformation carried out, the file is called "vectorfile.csv"

## Results and discussion

coming soon :(

### Vocabulary restriction.

I chose a vocabulary restriction of 20, as although it contains a lot of stop words, it does also contain some very telling other words. (also my poor laptop was really struggling with higher numbers)

### Result table

|                        | Grain | Crude | Grain-Crude | Crude-Grain |
|------------------------|-------|-------|-------------|-------------|
| No transformation      | 0.873 | 0.885 | 0.877       | 0.877       |
| Vocab restriction n=20 | 0.873 | 0.885 | 0.877       | 0.877       |
| Tf-idf transformation  | 0.872 | 0.884 | 0.876       | 0.876       |
| Vocab n=20 & tf-idf    | 0.872 | 0.884 | 0.876       | 0.876       |
| TruncatedSVD m=100     | 0.905 | 0.939 | 0.923       | 0.923       |
| TruncatedSVD m=1000    | 0.905 | 0.939 | 0.923       | 0.923       |
| Tf-idf & SVD m=100     | 0.894 | 0.887 | 0.707       | 0.707       |
| Tf-idf & SVD m=1000    | 0.894 | 0.887 | 0.707       | 0.707       |


### The hypothesis in your own words

I think this assignemt aimed to inform us on how the way we treat/process the data can affect the results of statistical operations carried out on the data. Whilst, of course, the way the actual strings are processed has an affect (normalisation, removing stop words etc), but also the statistical operations used to 'prep' the data can also skew the outputs. For example, whether raw counts are used or whether the counts are transformed, whether the dimensionality of the data matrix is reduced, whether smoothing is used, whether normalisation is used, and so on. This in turn affects other processes that may be carried out on this data, for example, as seen in the differences in the average cosine-similarity values both within topics and between topics. 

### Discussion of trends in results in light of the hypothesis

coming soon :(

## Bonus answers

maybe coming soon !
