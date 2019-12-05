
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

url = r'TwitterData\condensed_2018.json'
data = pre.preProcs(url)
# Display of first 10 elements from DataFrame

showDatastructs = False
if(showDatastructs==True):
    print(data.head(10))
    # Pick tweets with more favorits and more retweets:
    mean = np.mean(data['Len'])
    print("Mean Length in tweets: {}".format(mean))

vis = False
if(vis==True):
    dv.maxFavsAndRetweets(data['Likes'],data['Retweets'],data)
    dv.timeSeriesVis([data['Len'].values],data['Date'], ['Len'])
    dv.timeSeriesVis([data['Likes'].values, data['Retweets'].values],data['Date'], ['Likes','Retweets'])
    dv.pieChartSources(data["Source"])


sentimentAnalysis= True
if(sentimentAnalysis==True):
    # We create a column with the result of the analysis:
    data['SA'] = np.array([ sa.analize_sentiment(tweet) for tweet in data['Tweets'] ])

    # We display the updated dataframe with the new column:
    print(data.head(10))
    [pos_tweets,neu_tweets,neg_tweets] = sa.analize_results(data)

clustering = True
if(clustering==True):
    [intra,inter] = cval.clusterDistanceMessures(data)

    printavg = False
    if(printavg ==True):
        [pos,neu,neg] = cval.groupdata(data)
        clusters = [pos,neu,neg]#[pos,neu,neg,data]
        columnstrings = ['Len', 'Likes','Retweets']
        
        for x in range(0,len(inter)):
            print("==============")
            for y in range(len(inter[0])):
                print(inter[x][y])

    print("intra distance is: " + str(intra))
    print("inter distance is: " + str(inter))


