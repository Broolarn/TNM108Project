
#Used links 
# https://www.codementor.io/ferrorodolfo/sentiment-analysis-on-trump-s-tweets-using-python-pltbvb4xr?fbclid=IwAR3MAN3hGLz0s9zx-KfGDIZQnB49bLeZGqctmxSdSXjGUExbBJ40ruxs9xw
# https://ryan-cranfill.github.io/sentiment-pipeline-sklearn-1/ denna är nog inte relevant 
# https://towardsdatascience.com/unsupervised-sentiment-analysis-a38bf1906483
# https://www.geeksforgeeks.org/ml-intercluster-and-intracluster-distance/


import preProcess as pre
import numpy as np
import dataVis as dv
import sentiment as sa
import pandas as pd
import clustervalidation as cval
import mainUtilites as mu
import predictiveModel as pm
import summarize as su

url = r'TwitterData\condensed_2018.json'
data = pre.preProcs(url)
userinput = True
if(userinput):
    print()
    text = input("Enter tweet text to predict: ")
    SentenceToBePredicted = [text]
    
else:
    SentenceToBePredicted =  ['I am the best builder of walls in all wall builders history , Mexico is bad'] #["I am the best builder of walls in all wall builders history , Mexico is bad"]

pm.predictionModel(data,SentenceToBePredicted,nrOfLatestTweetsTakenIntoRegard=100)

if(userinput):
    print()
    NrOfSamples = input("How many of the recent tweets you want to summarize? ")
    NrOfSamples = int(NrOfSamples)    
else:
    NrOfSamples = 100

su.sumNLastTweets(data,N = NrOfSamples)