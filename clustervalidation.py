#https://www.geeksforgeeks.org/ml-intercluster-and-intracluster-distance/
import math
   
def clustervalidation(data):
    [pos,neu,neg] = groupdata(data)
    clusters = [pos,neu,neg,data]
    columnstrings = ['Len', 'Likes','Retweets']
    calcAverageForColumns(clusters,columnstrings)
    infradist = calcinfradist(pos,neu,neg,data)
    intradist = calcintradist(pos,neu,neg,data)
    return [intradist,infradist]

def groupdata(data):
    #print(data['SA']==0)
    pos = data[data['SA']>0]
    neu = data[data['SA']==0]
    neg = data[data['SA']<0]
    return [pos,neu,neg]

def calcAverageForColumns(clusters,columnstr):
    avgsForColumns = []
    for colstr in columnstr:
        avgsForcolstr = calcClustersMeanIntraDistance(clusters,colstr) 
        print( "For " + colstr +" the average values are: " )
        print(avgsForcolstr)
        avgsForColumns.append(avgsForcolstr)
    return avgsForColumns

def calcClustersMeanIntraDistance(Clusters,columnstr):
    ret = []
    for ci in Clusters:
        averageVal = numericMean(ci[columnstr])#averageForFeatureInCluster(ci,columnstr)
        intraDist = clusterIntraDistanceToAvg(ci[columnstr],averageVal)
        ret.append(numericMean(intraDist))
    return ret

def numericMean(data):
    return sum(data)/len(data)

def clusterIntraDistanceToAvg(data,avg):
    return [abs(val - avg) for val in data ]
    
def calcinfradist(pos,neu,neg,data): 
    return "to be implemented"
def calcintradist(pos,neu,neg,data):
    return "to be implemented"

    