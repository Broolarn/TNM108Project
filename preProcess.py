import pandas as pd
import numpy as np
import dataVis as dv
import sentiment as sa
tweets = pd.read_json (r'TwitterData\condensed_2018.json')


print (tweets)
print(tweets.size)
print(tweets.columns)
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
# Display of first 10 elements from DataFrame
print(data.head(10))

# Pick tweets with more favorits and more retweets:
mean = np.mean(data['Len'])
print("Mean Length in tweets: {}".format(mean))

dv.maxFavsAndRetweets(data['Likes'],data['Retweets'],data)

dv.timeSeriesVis([data['Len'].values],data['Date'], ['Len'])
dv.timeSeriesVis([data['Likes'].values, data['Retweets'].values],data['Date'], ['Likes','Retweets'])

dv.pieChartSources(sourceDevice)

# We create a column with the result of the analysis:
data['SA'] = np.array([ sa.analize_sentiment(tweet) for tweet in data['Tweets'] ])

# We display the updated dataframe with the new column:
print(data.head(10))

res = sa.analize_results(data)
