#https://www.geeksforgeeks.org/ml-intercluster-and-intracluster-distance/
import math
   
def clusterDistanceMessures(data):
    [pos,neu,neg] = groupdata(data)
    clusters = [pos,neu,neg]
    columnstrings = ['Len', 'Likes','Retweets']
    clusters = normClusters(clusters,columnstrings)
    intradist = meanIntraDistance(clusters,columnstrings)
    Interdist = meanInterDistance(clusters,columnstrings)
    return [intradist,Interdist]

def groupdata(data):
    pos = data[data['SA']>0]
    neu = data[data['SA']==0]
    neg = data[data['SA']<0]
    return [pos,neu,neg]

def normClusters(clusters,columnstr):
    
    for cl in clusters:
        for col in columnstr:
            maxval = max(cl[col])
            norm = [float(i)/ maxval for i in cl[col]]
            cl[col] = norm
    return clusters

def meanIntraDistance(clusters,columnstr):
    avgsForColumns = []
    for colstr in columnstr:
        avgIntraDistForColstr = ClustersMeanIntraDistance(clusters,colstr) 
        avgsForColumns.append(avgIntraDistForColstr)
    return avgsForColumns

def ClustersMeanIntraDistance(Clusters,columnstr):
    ret = []
    for ci in Clusters:
        averageVal = numericMean(ci[columnstr])#averageForFeatureInCluster(ci,columnstr)
        intraDist = clusterIntraDistance(ci[columnstr],averageVal)
        ret.append(numericMean(intraDist))
    return ret

def numericMean(data):
    return sum(data)/len(data)

def clusterIntraDistance(data,avg):
    return [abs(val - avg) for val in data ]
    
def meanInterDistance(clusters,columnstr): 
    avgsForColumns = []
    for colstr in columnstr:
        IntraDistForColstr = ClustersMeanInterDistance(clusters,colstr) 
        avgsForColumns.append(IntraDistForColstr)
    return avgsForColumns


def ClustersMeanInterDistance(Clusters,columnstr):
    #ret = []
    averageVals =[]
    intraDists = []
    for ci in Clusters:
        averageVals.append(numericMean(ci[columnstr]))
    intraDists = clusterInterDistanceToAvg(averageVals)
    return intraDists#numericMean(intraDists)

def clusterInterDistanceToAvg(Averages):
    ret = []
    rowress =[]
    for singleAvg in Averages:
        for someOtherAvg in Averages:
            rowress.append(abs(singleAvg - someOtherAvg))
        rowress = sum(rowress)
        ret.append(rowress)
        rowress = []   
    return ret

def PrintAverageforCluster(Clusters,columnstrings):
    
    for columnstr in columnstrings:
        averageVal = []
        for ci in Clusters:
            averageVal.append(numericMean(ci[columnstr]))#averageForFeatureInCluster(ci,columnstr)
        
        print("AverageValue for " + columnstr +" is " + str(averageVal))

    