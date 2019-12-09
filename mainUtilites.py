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
     #   print(sumOfRow)
        sumOfMatrix.append(sum(sumOfRow))
        sumForEachMatrix.append(sumOfMatrix)
      #  print(sumOfMatrix)    
        
    #print(min(sumForEachMatrix))
    return sumForEachMatrix

def findBestClusters(AllInterMatrixes,AllIntraMatrixes):
    rank = bestBasedOnRanking(AllInterMatrixes,AllIntraMatrixes)
    vals = bestBasedOnValues(AllInterMatrixes,AllIntraMatrixes)
    print("Rankbased: " + str(rank))
    print("Valsbased: " + str(vals))

def bestBasedOnValues(AllInterMatrixes,AllIntraMatrixes):
    allInterSums = sumMatrix(AllInterMatrixes)
    allIntraSums = sumMatrix(AllIntraMatrixes)
    
    maxval = allInterSums[allInterSums.index(max(allInterSums))]
    minval = allInterSums[allInterSums.index(min(allInterSums))]
    inter = [(x[0]-minval[0]) / (maxval[0]-minval[0]) for x in allInterSums]
    
    maxval = allIntraSums[allIntraSums.index(max(allIntraSums))]
    minval = allIntraSums[allIntraSums.index(min(allIntraSums))]
    intra = [1-((x[0]-minval[0]) / (maxval[0]-minval[0])) for x in allIntraSums]
    #print(allInterSums)
    #print(inter)

    #print(allIntraSums)
    #print(intra)

    res = []
    for i in range(0,len(intra)):
        res.append(intra[i]+inter[i])
    #print(res)

    #print(res.index(max(res)))    
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