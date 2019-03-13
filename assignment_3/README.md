# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Tala Zaeimzadeh

## Additional instructions

In the command line (for train.py and test.py), please input datafile name first and then modelfile name.

## Reporting for Part 4

### 3-grams

The accuracy value produced by the smaller model was highest for the biggest datafile. The perplexity values were all very 
close together, which I think might be due to a mistake in the code, nonetheless, it was the highest for the biggest datafile.
When the model file was run against the same datafile used to train the modelfile, it produced the highest accuracy rate, but 
it was still a lower value than I was expecting. Additionally, I expected the perplexity value to be lowest here; 
however, it was not as low as when the modelfile was run against another smaller datafile. 

For the bigger trained model,accuracy was highest for the smaller datafile, unlike the results from the smaller model. The 
bigger datafile had a lower accuracy and higher perplexity value. Although, the accuracy values were in general higher for 
each datafile versus the values produced for same datafile tested against the smaller model. When the model was tested 
against the datafile used to train it, it produced a lower accuracy value and a higher perplexity value than the smaller 
modelfile did when it was tested against itself.

### 2-grams

The pattern of results for the bigrams were similar to the trigrams, with a higher accuracy rate for the bigger datafiles when 
tested against the smaller model, and vice versa for the bigger model. Perplexity values were again all very similar. 
When each model was tested against the datafile it was trained on, both produced lower results than the trigram.

### 4-grams

Again the pattern of results were similar to the patterns mentioned above. The smaller model produced higher accuracy for 
the bigger datafile, and vice versa, whilst the bigger trained model produced higher accuracy values than the smaller model 
overall. The perplexity values were all very similar again, with the lowest for the smallest datafile tested against the 
bigger model. The bigger model produced a very low accuracy value when tested against the datafile it was trained on; however, 
the smaller model produced the highest accuracy value compared to the models of different ngrams.

### General Trends

There is a general trend that as the ngram size gets bigger the accuracy values improve. There was marginal improvement in the 
accuracy values produced by the 4-gram compared to the other ngrams. Additionally, as the model size increases, so does the 
accuracy rates, so that if a model was trained on 1000 lines, it produces higher accuracy values than a model trained on 500 
lines. These patterns seem logical, as a bigger ngram trained on more data is likely to have more predictive power, capable of 
producing more accurate predictions. Furthermore, the bigger model produced higher accuracy values for the smaller datafile, 
whilst the smaller model produced higher accuracy values for the bigger datafiles. This shows that whilst the size of the 
ngram and the size of the corpus used to train the model affect its predictive power, so does the size of the data used to 
test the model.

### Improvements

I have not (yet?) dealt with the dummy start/end vectors to deal with ngrams starting/ending at the start/end of a file. 
Furthermore, the code can take a very long time to train bigger datafiles (especially for bigger ngrams), so I think maybe it 
can be written more efficiently to reduce the training time. This is also the reason why I couldn't train a modelfile bigger 
than 1000 words. Ideally, the data should be tested against a model trained on all/most of the available corpus to compare 
changes in accuracy and perplexity values produced.
Also, as mentioned above, I believe the method to calculate perplexity needs to be revised, as all the values are very similar 
to each other, and do not seem correct.
