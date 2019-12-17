import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import sentiment as sen
import sentiment as sa
import mainUtilites as mu
import clustervalidation as cval
import summarize as su
nltk.download('punkt')

def predictionModel(data, testsentence,nrOfLatestTweetsTakenIntoRegard=100):
    [AllInterMatrixes,AllIntraMatrixes,foldData] = mu.seperatedata(data,nrOfSplits=5)
    bestIndex = cval.findBestClusters(AllInterMatrixes,AllIntraMatrixes)
    [train,test] =  foldData[bestIndex]

    [predLikes, predRetweets,predSA] = createPrediction(foldData[bestIndex],KPOINTS=10,testsentence=testsentence)
    testTweet = {'Tweets' : testsentence, 'Likes' :predLikes, 'Retweets' : predRetweets, 'SA' : predSA}
    
    print()
    print("The provided tweet is predicted to have: ")
    print(str(predLikes) + " likes , " + str(predRetweets) + " retweets , " + str(predSA) + " as sentiment")

    su.compareTweetToData(train,testTweet,nrOfLatestTweetsTakenIntoRegard)

def createPrediction(bestClusteringFold,KPOINTS, testsentence):
    [train,test] = bestClusteringFold
    features = [train['Len'],train['Likes'],train['Retweets']]
    testTweet = [test['Len'].iloc[0],test['Likes'].iloc[0],test['Retweets'].iloc[0]]
    
    
    [predictedLikes,predictedRetweets] = textstuff(testsentence,train)
    predSA = sa.analize_sentiment(testsentence[0])
    printstuff = False
    if(printstuff):
        print("Predicted values")
        print("Likes " + str(predictedLikes))
        print("Retweets " + str(predictedRetweets))
        print("Sentiment " + str(predSA))

    #findClosestMatchs(features,testTweet,KPOINTS,NDIM=3)
    return [predictedLikes,predictedRetweets,predSA]

    
def textstuff(test,train):
    text = [sen.clean_tweet(test[0])]
    cleanedTraining = []
    for i in range(0,len(train['Tweets'])):
        cleanedTraining.append(sen.clean_tweet(train['Tweets'].iloc[i]) )
        
    vec = TfidfVectorizer()
    vec.fit(cleanedTraining)
    features = vec.transform(cleanedTraining)  
    new_features = vec.transform(text)
    
    from sklearn.metrics.pairwise import cosine_similarity  
    cosSim = cosine_similarity(new_features, features).flatten()
    related_product_indices = cosSim.argsort()[:-11:-1]
    mostSimilarTweets = train.iloc[related_product_indices]

    mostSimilarsLikes = mostSimilarTweets['Likes']
    mostSimilarsRetweets = mostSimilarTweets['Retweets']
    predictedLikes = sum(mostSimilarsLikes)/len(mostSimilarsLikes)
    predictedRetweets = sum(mostSimilarsRetweets)/len(mostSimilarsRetweets)

    printres = False
    if(printres):
        print ("cosine scores ==> ", cosSim )
        print("related_product_indices")
        print(related_product_indices)
        print("resulting similar tweets")
        print(mostSimilarTweets)
    return [predictedLikes,predictedRetweets]

