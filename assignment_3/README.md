# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Tala Zaeimzadeh

## Additional instructions

I'm submitting this early as I am leaving the country for a while, but I hope that you guys don't check this until I am back 
so I can have time to fix the issues.

In the command line (for train.py and test.py), please input datafile name first and then modelfile name

## Reporting for Part 4

Training a model on 1000 lines

when tested against a smaller datafile (~300 lines), there are higher accuracy and perplexity values versus when tested against bigger (~500 lines) datafiles, which is an inverse relationship between accuracy and perplexity. This is surprising 
as I expected better accuracy to correlate with lower perplexity. I assume this is because I have done something wrong, 
probably in calculating my perplexity values.
When tested against itself (pretty being 'trained'), the accuracy and perplexity values were highest, as expected; however
not as high as would be expected.

Training a model on 300 lines

when tested against datafile of ~300 lines, it had the best accuracy but worst perplexity. Datefile of 500 lines had the 
lowest accuracy, whilst the datafile of ~1000 lines had the lowest perplexity but a mid-range accuracy. The relationship 
between accuracy and perplexity is surprising here as well, which is probably further evidence that I am calculating perplexity incorrectly.
When run against itself, it produced better results than the model trained on 1000 lines, but still probably not as good as 
I was expecting.


## Reporting for Part Bonus 

(maybe in the future)
