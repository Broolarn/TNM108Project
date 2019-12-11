import pandas as pd
import numpy as np
import dataVis as dv
import sentiment as sa

def preProcs(fileurl):
    tweets = pd.read_json (fileurl)
    #print (tweets)
    #print(tweets.size)
    #print(tweets.columns)
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

    return data


