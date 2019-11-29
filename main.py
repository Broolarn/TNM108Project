import preProcess as pre
import numpy as np
import dataVis as dv
import sentiment as sa

url = r'TwitterData\condensed_2018.json'
data = pre.preProcs(url)
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
