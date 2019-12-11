from summa.summarizer import summarize
from summa import keywords
import clustervalidation as cv
import pandas as pd
#from main import data 


#Extract the keywords from positive/negative/neutral tweets  
def reKeyWords(data):
    [pos,neu,neg] = cv.groupdata(data)
    numberOfTweets = 100

    posSorted =  pos.sort_values(by=['Retweets'], ascending=False)
    neuSorted =  neu.sort_values(by=['Retweets'], ascending=False)
    negSorted =  neg.sort_values(by=['Retweets'], ascending=False)

    posSortedTweets = posSorted['Tweets'].head(numberOfTweets)
    neuSortedTweets = neuSorted['Tweets'].head(numberOfTweets)
    negSortedTweets = negSorted['Tweets'].head(numberOfTweets)

    postext = ''
    neutext = ''
    negtext = ''
    for Tweets in posSortedTweets:
        postext += Tweets
    for Tweets in neuSortedTweets:
        neutext += Tweets
    for Tweets in negSortedTweets:
        negtext += Tweets

    
    return [postext,neutext,negtext]


def LiKeyWords(data):
   
    [pos,neu,neg] = cv.groupdata(data)
    numberOfTweets = 100
    #sort the tweets by the number of likes
    posSorted =  pos.sort_values(by=['Likes'], ascending=False)
    neuSorted =  neu.sort_values(by=['Likes'], ascending=False)
    negSorted =  neg.sort_values(by=['Likes'], ascending=False)

    #Extract a certent number of tweets
    posSortedTweets = posSorted['Tweets'].head(numberOfTweets)
    neuSortedTweets = neuSorted['Tweets'].head(numberOfTweets)
    negSortedTweets = negSorted['Tweets'].head(numberOfTweets)

    #Convert the Data Frames to stings 
    postext = ''
    neutext = ''
    negtext = ''
    for Tweets in posSortedTweets:
        postext += Tweets
    for Tweets in neuSortedTweets:
        neutext += Tweets
    for Tweets in negSortedTweets:
        negtext += Tweets

    #Extract the keywords 
    #print("Top 10 Keywords in positiv tweets:\n",keywords.keywords(postext,words=10))
    return [postext,neutext,negtext]
def normedAvg(data):
    total = 0
    for Tweets in data:
        normedVal = (Tweets - min(data)) /(max(data)-min(data))
        total += normedVal
    normedAvg = total/len(data)  
    return normedAvg  

def avgForEachSentiment(posSorted,neuSorted,negSorted,keyString):
    
    posRetweet = posSorted[keyString]
    neuRetweet = neuSorted[keyString]
    negRetweet = negSorted[keyString]

    averagePos = normedAvg(posRetweet)
    averageNeu = normedAvg(neuRetweet)
    averageNeg = normedAvg(negRetweet)
    printstuff = False   
    if(printstuff): 
        print(keyString +' on positvie (average)' + str(averagePos))
        print(keyString +' on neutral (average) ' + str(averageNeu))
        print(keyString +' on negativ ' + str(averageNeg))
    return [averagePos,averageNeu,averageNeg]

def getAvgOfTestTweet(testTweet,normedAveragesForLikesAndRetweets):
    if(testTweet['SA'] > 0 ):
        [avgLike , avgRetweet] = normedAveragesForLikesAndRetweets[0]
    elif(testTweet['SA'] == 0 ):
        [avgLike , avgRetweet] = normedAveragesForLikesAndRetweets[1]
    else:
        [avgLike , avgRetweet] = normedAveragesForLikesAndRetweets[2]
    return  [avgLike , avgRetweet]

def compareTweetToData(data,testTweet,nrOfLatestTweetsTakenIntoRegard):
    normedAveragesForLikesAndRetweets = ReLiAverage(data,nrOfLatestTweetsTakenIntoRegard)
    normedTestValForLike = (testTweet['Likes'] - min(data['Likes']))/(max(data['Likes'])-min(data['Likes']))
    normedTestValForRetweets = (testTweet['Retweets'] - min(data['Retweets']))/(max(data['Retweets'])-min(data['Retweets']))
    [avgLike , avgRetweet] = getAvgOfTestTweet(testTweet,normedAveragesForLikesAndRetweets)

    likeRelationToAvg = normedTestValForLike/avgLike
    retweetRelationToAvg = normedTestValForRetweets/avgRetweet

    avgForData = {'Likes' : avgLike , 'Retweet' : avgRetweet}
    sample = {'Likes' : normedTestValForLike , 'Retweet' : normedTestValForRetweets}
    relation = {'Likes' : str(likeRelationToAvg) + "%" , 'Retweet' : str(retweetRelationToAvg)+ "%"}
    asMatrix = {'NormedAvgsForData' : avgForData , 'NormedValueForSample' : sample,'sampleRelativToDataAvg' : relation}
    df = pd.DataFrame(asMatrix) 
    print()
    print(df)   


def ReLiAverage(data,nrOfLatestTweetsTakenIntoRegard):
    [pos,neu,neg] = cv.groupdata(data)
    numberOfTweets = nrOfLatestTweetsTakenIntoRegard
    #sort the tweets by the date
    posSorted =  pos.sort_values(by=['Date'], ascending=False)
    neuSorted =  neu.sort_values(by=['Date'], ascending=False)
    negSorted =  neg.sort_values(by=['Date'], ascending=False)
    
    posSorted = posSorted.loc[0:100,:]
    neuSorted = neuSorted.loc[0:100,:]
    negSorted = negSorted.loc[0:100,:]

    [averagePosRe,averageNeuRe,averageNegRe] = avgForEachSentiment(posSorted,neuSorted,negSorted,'Retweets')
    [averagePosLi,averageNeuLi,averageNegLi] = avgForEachSentiment(posSorted,neuSorted,negSorted,'Likes')
    posVals = [averagePosLi, averagePosRe]
    neuVals = [averageNeuLi, averageNeuRe]
    negVals = [averageNegLi,averageNegRe]
    return[posVals , neuVals, negVals]
 

def averageRetweet(data):
    numberOfTweets =100
    totalNumberOfRetweets = 0
    retweetSorted =  data.sort_values(by=['Date'], ascending=False)
    retweetSortedTweets = retweetSorted['Retweets'].head(numberOfTweets)
    
    for Retweets in retweetSortedTweets:
        totalNumberOfRetweets += Retweets
     
    average = totalNumberOfRetweets / numberOfTweets 

    print('total number: ' + str(totalNumberOfRetweets)) 
    print('average: ' + str(average))

 
#summarize the tweets by the number of retweets
def sumRetweet(data):
    numberOfTweets = 500
    print('Beginning of function sumReTweet')
    #sort the data by the number of retweets
    retweetSorted =  data.sort_values(by=['Retweets'], ascending=False)
   

    retweetSortedTweets = retweetSorted['Tweets'].head(numberOfTweets)
  
    retweettext = ''
    for Tweets in retweetSortedTweets: 
        retweettext += Tweets
       
    
    print("Top 3 Keywords in Retweets:\n",keywords.keywords(retweettext,words=10))   
    print('End of function sumReTweet')





