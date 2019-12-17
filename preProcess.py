import pandas as pd
import numpy as np
import dataVis as dv
import sentiment as sa
import dataVis as vis
import clustervalidation as cval
import mainUtilites as mu
def preProcs(fileurl):
    tweets = pd.read_json (fileurl)
    tweetid = tweets['id_str']
    sourceDevice = tweets['source']
    twitterTexts = tweets['text']
    creationDate = tweets['created_at']
    retweets = tweets['retweet_count']
    favorites = tweets['favorite_count']
    retweetedPost = tweets['is_retweet']

    # We create a pandas dataframe as follows:
    data = pd.DataFrame(data=[tweet for tweet in twitterTexts], columns=['Tweets'])
    data['Len']  = np.array([len(tweet) for tweet in twitterTexts])
    data['ID']   = np.array([tweet for tweet in tweetid])
    data['Date'] = np.array([tweet for tweet in creationDate])
    data['Source'] = np.array([tweet for tweet in sourceDevice])
    data['Likes']  = np.array([tweet for tweet in favorites])
    data['Retweets']    = np.array([tweet for tweet in retweets])

    sentimentAnalysis= True
    if(sentimentAnalysis==True):
        # We create a column with the result of the analysis:
        data['SA'] = np.array([ sa.analize_sentiment(tweet) for tweet in data['Tweets'] ])
        [pos_tweets,neu_tweets,neg_tweets] = sa.analize_results(data)
       
        sa.howDoesDataLook(data,pos_tweets,neu_tweets,neg_tweets)

    vis = False
    if(vis==True):
        dv.maxFavsAndRetweets(data['Likes'],data['Retweets'],data)
        dv.timeSeriesVis([data['Len'].values],data['Date'], ['Len'])
        dv.timeSeriesVis([data['Likes'].values, data['Retweets'].values],data['Date'], ['Likes','Retweets'])
        dv.pieChartSources(data["Source"])
    
    clustering = False
    if(clustering==True):
        [intra,inter] = cval.clusterDistanceMessures(data)
        intraMatrix = mu.printAsMatrix(intra,[['Pos', 'Neu', 'Neg'],['Len', 'Likes','Retweets']],"Intra")
        interMatrix = mu.printAsMatrix(inter,[['Pos', 'Neu', 'Neg'],['Len', 'Likes','Retweets']],"Inter")
        
        dv.linesPlot(intraMatrix,'Intra','Normed Intra Distance')
        dv.linesPlot(interMatrix,'Inter','Normed Inter Distance')

    return data


