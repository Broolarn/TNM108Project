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
        cl = cl.copy()
        for col in columnstr:
            maxval = max(cl[col])
            minval = min(cl[col])
            cl.loc[:,col] = [(float(i)-minval)/ (maxval-minval) for i in cl[col]]
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
        averageVal = numericMean(ci[columnstr])
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


def sumMatrix(inmatrix):
    sumForEachMatrix = []
    for matrix in inmatrix:
        sumOfMatrix = []
        sumOfRow =[]
        for row in matrix:
            sumOfRow.append(sum(row))
    
        sumOfMatrix.append(sum(sumOfRow))
        sumForEachMatrix.append(sumOfMatrix)
    return sumForEachMatrix

def findBestClusters(AllInterMatrixes,AllIntraMatrixes):
    rank = bestBasedOnRanking(AllInterMatrixes,AllIntraMatrixes)
    vals = bestBasedOnValues(AllInterMatrixes,AllIntraMatrixes)
    
    combinedBest = []
    for i in range(0,len(vals)):
        combinedBest.append(rank[i]+vals[i])
    printResult = False
    if(printResult):
        print("Rankbased: " + str(rank))
        print("Valsbased: " + str(vals))
        print("Best index at : " + str(combinedBest.index(min(combinedBest))))

    return combinedBest.index(min(combinedBest))
def bestBasedOnValues(AllInterMatrixes,AllIntraMatrixes):
    allInterSums = sumMatrix(AllInterMatrixes)
    allIntraSums = sumMatrix(AllIntraMatrixes)
    
    maxval = allInterSums[allInterSums.index(max(allInterSums))]
    minval = allInterSums[allInterSums.index(min(allInterSums))]
    inter = [(x[0]-minval[0]) / (maxval[0]-minval[0]) for x in allInterSums]
    
    maxval = allIntraSums[allIntraSums.index(max(allIntraSums))]
    minval = allIntraSums[allIntraSums.index(min(allIntraSums))]
    intra = [1-((x[0]-minval[0]) / (maxval[0]-minval[0])) for x in allIntraSums]

    res = []
    for i in range(0,len(intra)):
        res.append(intra[i]+inter[i])

    rescopy = []
    for i in res:
     rescopy.append(i)
    
    rescopy.sort(reverse=True)

    rank = []
    for i in range(0,len(res)):
        rank.append(res.index((rescopy[i])))

    return rank

def bestBasedOnRanking(AllInterMatrixes,AllIntraMatrixes):
    allInterSums = sumMatrix(AllInterMatrixes)
    allIntraSums = sumMatrix(AllIntraMatrixes)
    
    maxval = allInterSums[allInterSums.index(max(allInterSums))]
    minval = allInterSums[allInterSums.index(min(allInterSums))]
    inter = [(x[0]-minval[0]) / (maxval[0]-minval[0]) for x in allInterSums]
    
    maxval = allIntraSums[allIntraSums.index(max(allIntraSums))]
    minval = allIntraSums[allIntraSums.index(min(allIntraSums))]
    intra = [1-((x[0]-minval[0]) / (maxval[0]-minval[0])) for x in allIntraSums]
    
    intercopy = []
    for i in inter:
     intercopy.append(i)
    intracopy = []
    for i in intra:
     intracopy.append(i)
    
    intercopy.sort(reverse=True)
    intracopy.sort(reverse=True)

    interindex =[]
    intraindex = []
    for i in range(0,len(inter)):
        interindex.append(inter.index((intercopy[i])))
        intraindex.append(intra.index((intracopy[i])))
    rank  =[]

    for i in range(0,len(interindex)):
        rank.append(interindex[i]+intraindex[i])
    
    return rank