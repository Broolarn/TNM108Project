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
  

def ReLiAverage(data):
    [pos,neu,neg] = cv.groupdata(data)
    numberOfTweets = 100
    #sort the tweets by the date
    posSorted =  pos.sort_values(by=['Date'], ascending=False)
    neuSorted =  neu.sort_values(by=['Date'], ascending=False)
    negSorted =  neg.sort_values(by=['Date'], ascending=False)
    
    posSorted = posSorted.loc[0:100,:]
    neuSorted = neuSorted.loc[0:100,:]
    negSorted = negSorted.loc[0:100,:]

    posRetweet = posSorted['Retweets']
    neuRetweet = neuSorted['Retweets']
    negRetweet = negSorted['Retweets']
 
    totalPosRetweet = 0
    totalNeuRetweet = 0
    totalNegRetweet = 0
    for Tweets in posRetweet:
        totalPosRetweet = posRetweet.sum()

    for Tweets in posRetweet:
        totalNeuRetweet = neuRetweet.sum()

    for Tweets in posRetweet:
        totalNegRetweet = negRetweet.sum()

    averagePosRe = totalPosRetweet / posRetweet.size
    averageNeuRe = totalNeuRetweet / neuRetweet.size
    averageNegRe = totalNegRetweet / negRetweet.size
    
    print('retweet on positvie (average)' + str(averagePosRe))
    print('retweet on neutral (average) ' + str(averageNeuRe))
    print('retweet on negativ ' + str(averageNegRe))


    posSorted = posSorted['Likes']
    neuSorted = neuSorted['Likes']
    negSorted = negSorted['Likes']   
   
    totalPosLikes = 0
    totalNeuLikes = 0
    totalNegLikes = 0

    for Tweets in posSorted:
        totalPosLikes += Tweets
    averagePosLi = totalPosLikes/numberOfTweets

    for Tweets in neuSorted:
        totalNeuLikes += Tweets
    averageNeuLi = totalNeuLikes/numberOfTweets

    for Tweets in negSorted:
        totalNegLikes += Tweets
    averageNegLi = totalNegLikes/numberOfTweets

    print( 'likes on positive (average): ' + str(averagePosLi))
    print( 'likes on neutral (average): ' + str(averageNeuLi))
    print( 'likes on negative (average): '+ str(averageNegLi))

    return[averagePosLi, averagePosRe , averageNeuLi, averageNeuRe ,averageNegLi,averageNegRe ]
 


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





