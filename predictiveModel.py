import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import sentiment as sen

nltk.download('punkt')

def createModel(bestClusteringFold,KPOINTS):
    [train,test] = bestClusteringFold
    features = [train['Len'],train['Likes'],train['Retweets']]
    testTweet =[test['Len'].iloc[0],test['Likes'].iloc[0],test['Retweets'].iloc[0]]
    print("testtweet" )
    print(testTweet)
    [predictedLikes,predictedRetweets] = textstuff(test,train)
    
    findClosestMatchs(features,testTweet,KPOINTS,NDIM=3)
    return [predictedLikes,predictedRetweets]

    
def textstuff(test,train):
    
    text = [sen.clean_tweet(test['Tweets'].iloc[0])]
    cleanedTraining = []
    for i in range(0,len(train['Tweets'])):
        cleanedTraining.append(sen.clean_tweet(train['Tweets'].iloc[i]) )
        
    vec = TfidfVectorizer()
    vec.fit(cleanedTraining)
    features = vec.transform(cleanedTraining)  
    new_features = vec.transform(text)
    
    from sklearn.metrics.pairwise import cosine_similarity  
    cosSim = cosine_similarity(new_features, features).flatten()
    print ("cosine scores ==> ", cosSim )#here the first element of tfidf_matrix_train is matched with other three elements
    related_product_indices = cosSim.argsort()[:-11:-1]
    print("related_product_indices")
    print(related_product_indices)
    print("resulting similar tweets")
    mostSimilarTweets = train.iloc[related_product_indices]
    print(mostSimilarTweets)
    mostSimilarsLikes = mostSimilarTweets['Likes']
    mostSimilarsRetweets = mostSimilarTweets['Retweets']
    predictedLikes = sum(mostSimilarsLikes)/len(mostSimilarsLikes)
    predictedRetweets = sum(mostSimilarsRetweets)/len(mostSimilarsRetweets)
    printWayToResults = False
    if(printWayToResults):
        print("LIKES : ")
        print(mostSimilarsLikes)
        print(sum(mostSimilarsLikes)/len(mostSimilarsLikes))
        mostSimilarsRetweets = mostSimilarTweets['Retweets']
        print("Retweets : ")
        print(mostSimilarsRetweets)
        print(sum(mostSimilarsRetweets)/len(mostSimilarsRetweets))
        print("TEST :  ")
        print(text)
        print(test.iloc[0])
    return [predictedLikes,predictedRetweets]


def findClosestMatchs(features,testTweet,KPOINTS,NDIM):
    import numpy
    #NDIM = 3 # number of dimensions

    from numpy import transpose
    a = np.array(features)
    a = a.transpose()
    a.shape = int(a.size / NDIM), NDIM
    
    from scipy.spatial import KDTree
    tree = KDTree(a, leafsize=a.shape[0]+1)
    [distances, ndx] = tree.query([testTweet], k=KPOINTS)

    closestMatches = a[ndx]
    print(closestMatches)

    interpolated = interpolateClosestMatch(closestMatches) 
    print("interpolated: ")
    print( interpolated)

def interpolateClosestMatch(closestMatches):
    Lendata  = closestMatches[0,:,0]
    Likesdata  = closestMatches[0,:,1]
    Retweetsdata  = closestMatches[0,:,2]
    length = len(Lendata) 
    avgLendata  = sum(Lendata) / length 
    avgLikesdata  = sum(Likesdata) / length 
    avgRetweetsdata  = sum(Retweetsdata) / length 
    
    return [avgLendata,avgLikesdata,avgRetweetsdata]
   
