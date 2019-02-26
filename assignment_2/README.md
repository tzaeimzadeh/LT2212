# LT2212 V19 Assignment 2

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Tala Zaeimzadeh

## Additional instructions

I have an option for providing an output file name as an argument when calling the gendoc.py file; however, it's commented out as I have a method that produces specific output file names based on which transformation arguments are called on the file.


## File naming convention

The output file naming convention is the name of the transformation carried out on it. if multiple transformations carried out, then the later transformation is first followed by the earlier transformation (e.g. if no vocabulary restriction was imposed, but tf-idf was applied, with truncated SVD to 100 dimensions, then the file would be called "svd100_tfidf.csv"). if no transformation carried out, the file is called "vectorfile.csv".

## Results and discussion

Based on the average cosine-similarites values, especially for the similarity values between the topic subjects (grain and crude), I believe that there must be an error somewhere in my code, as these values seem very high. This could be for a number of reasons. Firstly, I did not remove duplicate files, nor did I filter out stop words, both of which could have contributed to higher values, as there would be more similar counts between the two topic files. Furthermore, I am unsure about the method I used to get the cosine similarity values. The sklearn cosine similarity function did not work on my data, due to rejecting the shape of the input arrays. Therefore, I used numpy to calculate the average cosine-similarities more manually. Additionally, I have an if condition to avoid values of zero, and considering that the majority of counts were 0, it is likely that this had a huge effect on my results; however, I was unsure whether I was allowed to use smoothing. If my results are incorrect, this is where I suspect the problem to be. 


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

I think this assignemt aimed to inform us on how the way we treat/process the data can affect the results of statistical operations carried out on the data. Whilst, of course, the way the actual strings are processed has an affect (normalisation, removing stop words etc), but also the statistical operations used to 'prep' the data can also skew the outputs. For example, whether raw counts are used or whether the counts are transformed, whether the dimensionality of the data matrix is reduced, whether smoothing is used, whether normalisation is used, and so on. This in turn affects other processes that may be carried out on this data, for example, as seen in the differences in the average cosine-similarity values both within topics and between topics. Additionally, I believe the assignment aimed to show us the different processes data needs to go through, both in pre-processing and in the operations leading to the final output. 

### Discussion of trends in results in light of the hypothesis

Although the results may be incorrect, there is still a trend that conforms to the hypothesis that processing the data differently can have an affect on the outcome. The results are different based on the type of transofrmation carried out on the data. Furthermore, the results of the cosine-similarity carried out on truncated SVD values are the highest. This could be because reducing the dimensionality to 100 or 1000 from more than 10000 is likely to lead to consisternly higher values and maybe over-fitting. 

### Bonus answers

#Flaws

A flaw of the assignment (for me personally) was that it was rather confusing, as I felt unsure what the point was. I originally thought that the assignment was meant to give us a first-hand experience of what we learnt in the NLP module about similarities within related documents (and of course, to some extent, this assignment did provide that); however, I felt like I spent much more time trying to understand what the assignment was asking of me. In retrospect, I feel disappointed that I didn't use this assignment as a chance to experiment with processing the data and carrying out different statistical methods (and specifically, I wish I had used smoothing rather than ignoring counts of 0); however, I feel like I was constantly trying to just work out what the instructions meant that little time was left.

#Applying other measures

Another method that could have been used to compare the similarity of the topics is latent semantic analysis (LSA), which uses contextual information (in what context a word tends to appear) to determine the similarity of words (and therefore documents/topics). The TruncatedSVD-transformed values could have been used for this. Other methods could have also been used, for example in the creation of the vocabulary, instead of taking all the words, a bag-of-words approach could have been used instead where random selections of words were used.
A better technique I could have used personally was to pre-process my data better, such as remove stop words and use a more precise regex to normalise the text.
