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

      