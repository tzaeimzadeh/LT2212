# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Tala Zaeimzadeh

## Additional instructions

In the command line (for train.py and test.py), please input datafile name first and then modelfile name.

Currently the code is limited to 2, 3 and 4-grams (to be fixed).

## Reporting for Part 4

### 3-grams

Training a model on 300 lines

The accuracy was highest for the model run against the smaller datafile (300 lines), whilst the datafile of 1000 lines 
produced better results than the datafile of 500 lines. The perplexity values are all very close together, which I think is 
might be due to a mistake in the code, nonetheless, it was the highest for the datafile of 1000 lines. 
When the model file was run against the same datafile used to train the modelfile, it produced the highest accuracy rate, but 
it was still a lower value than I was expecting (0.4). Additionally, I expected the perplexity value to be lowest here; 
however, it was not as low as the when the modelfile was run against another datafile of 300 lines. 

Training a model on 1000 lines

The results from a trained model of 1000 lines are almost identical to the results from the model trained on 300 lines. There 
are slight differences in the perplexity scores, which follow the pattern of the values mentioned above. When the model was 
tested against the datafile used to train it, it produced a lower accuracy value (0.3) and a higher perplexity value than the 
smaller modelfile (300 lines) did when it was tested against itself.

### 2-grams

The pattern of results for the bigrams were similar to the trigrams, with a higher accuracy rate for the smaller datafiles 
(300 lines), however, the model trained on 1000 lines produced higher results than the model trained on 300 lines. Perplexity 
values were again all very similar. 
When each model was tested against the datafile it was trained on, the both produced lower results than the trigram (0.2).

### 4-grams

Again the pattern of results were similar to the patterns mentioned above. The smaller (300 lines) datafile produced the 
higher accuracy, whilst the bigger trained model (1000 lines) produced higher accuracy values than the smaller model (300 
lines). The perplexity values were all very similar again, with the lowest for the smallest datafile tested against the bigger 
model. 
The bigger model produced a very low (0.4) accuracy value when tested against the datafile it was trained on; however, the 
smaller model produced the highest (0.7) accuracy value compared to the models of different ngrams.

### General Trends

There is a general (although not complete) trend that as the ngram size gets bigger, the accuracy values improve. There was 
marginal improvement in the accuracy values produced by the 4-gram compared to the other ngrams. Additionally, as the 
modefile size increases, so does the accuracy rates, so that if a model was trained on 1000 lines, it produces higher accuracy 
values than a model trained on 300 lines. These patterns seem logical, as a bigger ngram trained on more data is likely to 
have more predictive power, capable of producing more accurate predictions.
Furthermore, smaller datafiles being tested produced higher accuracy values. This also seems logical, as a smaller test corpus 
would require less predictions to be made, making a correct prediction more likely.

### Improvements

I have not (yet) dealt with the dummy start/end vectors to deal with ngrams starting/ending at the start/end of a file. 
The code should also be able to handle ngrams bigger than 4-grams. 
Furthermore, the code can take a very long time to train bigger datafiles, so I think maybe it can be written more efficiently 
to reduce the training time.
Also, as mentioned above, I believe the method to calculate perplexity needs to be revised, as all the values are very similar 
to each other.
