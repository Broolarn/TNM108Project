import pandas as pd

def printAsMatrix(data, lables, title):
    print("Matrix representation of " + title)
    printframe = pd.DataFrame(data, columns=lables[0], index=lables[1])
    print(printframe)
    return printframe

def seperatedata(data,nrOfSplits):
    AllInterMatrixes = []
    AllIntraMatrixes = []
    from sklearn.model_selection import KFold
    import clustervalidation as cval
    cv = KFold(n_splits=nrOfSplits, random_state=42, shuffle=False)
    for train_index, test_index in cv.split(data):
        X_train = pd.DataFrame(data , index=train_index)
        X_test = pd.DataFrame(data , index=test_index)
        [intra,inter] = cval.clusterDistanceMessures(X_train)
        AllIntraMatrixes.append(intra)
        AllInterMatrixes.append(inter)
        #intraMatrix = mu.printAsMatrix(intra,[['Pos', 'Neu', 'Neg'],['Len', 'Likes','Retweets']],"Intra")
        #interMatrix = mu.printAsMatrix(inter,[['Pos', 'Neu', 'Neg'],['Len', 'Likes','Retweets']],"Inter")
    return [AllIntraMatrixes,AllInterMatrixes]

def printAllmatrixes(matrixes,titles):
    for i in range(0,len(titles)):
        print(len(matrixes[i]))
        for matrix in matrixes[i]:
            temp=printAsMatrix(matrix,[['Pos', 'Neu', 'Neg'],['Len', 'Likes','Retweets']],titles[i])

def sumMatrix(inmatrix):
    sumForEachMatrix = []
    for matrix in inmatrix:
        sumOfMatrix = []
        sumOfRow =[]
        for row in matrix:
            sumOfRow.append(sum(row))
        print(sumOfRow)
        sumOfMatrix.append(sum(sumOfRow))
        sumForEachMatrix.append(sumOfMatrix)
        print(sumOfMatrix)    
        
    print(min(sumForEachMatrix))
    return sumForEachMatrix

def findBestClusters(AllInterMatrixes,AllIntraMatrixes):
    allInterSums = sumMatrix(AllInterMatrixes)
    allIntraSums = sumMatrix(AllIntraMatrixes)
    maxindex = allInterSums.index(max(allInterSums))
    minindex = allIntraSums.index(min(allIntraSums))
   
    intercopy = []
    for i in allInterSums:
     intercopy.append(i)
    intracopy = []
    for i in allIntraSums:
     intracopy.append(i)
 
    intercopy.sort(reverse=True)
    intracopy.sort()
    indexlistmax =[]
    indexlistmin = []
    for i in range(0,len(allInterSums)):
        indexlistmax.append(allInterSums.index((intercopy[i])))
        indexlistmin.append(allIntraSums.index((intracopy[i])))
  

    print(minindex)
    print(maxindex)
    print(allInterSums)
    print(allIntraSums)
    print(intercopy)
    print(intracopy)
    print(indexlistmax)
    print(indexlistmin)
  
    rank  =[]
    for i in range(0,len(indexlistmax)):
        rank.append(indexlistmax[i]+indexlistmin[i])
    print(rank)
    bestClusterIndex = rank.index(min(rank))
    print(bestClusterIndex)