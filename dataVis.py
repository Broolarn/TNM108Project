import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def maxFavsAndRetweets(favData,RetweetsData,data):
    maxFav = np.max(favData)
    maxRetweets  = np.max(RetweetsData)

    fav = data[data.Likes == maxFav].index[0]
    rt  = data[data.Retweets == maxRetweets].index[0]

    # Max favorits:
    print("The tweet with more likes is: \n{}".format(data['Tweets'][fav]))
    print("Number of likes: {}".format(maxFav))
    print("{} characters.\n".format(data['Len'][fav]))

    # Max retweets:
    print("The tweet with more retweets is: \n{}".format(data['Tweets'][rt]))
    print("Number of retweets: {}".format(maxRetweets))
    print("{} characters.\n".format(data['Len'][rt]))
    dataToReturn = [maxFav,maxRetweets]
    return dataToReturn

def timeSeriesVis(seriesData,dateData,dataLables):
    series = []
    for index in range(len(seriesData)):
        series.append(pd.Series(data=seriesData[index], index=dateData))
        series[index].plot(figsize=(16,4), label=dataLables[index], legend=True)
    plt.show()

def pieChartSources(deviceData):
    # We obtain all possible sources:
    sources = []
    for source in deviceData:
        if source not in sources:
            sources.append(source)

    # We print sources list:
    print("Creation of content sources:")
    for source in sources:
        print("* {}".format(source))
    # We create a numpy vector mapped to labels:
    percent = np.zeros(len(sources))


    for source in deviceData:
        for index in range(len(sources)):
            if source == sources[index]:
                percent[index] += 1
                pass

    percent /= 100

    # Pie chart:
    pie_chart = pd.Series(percent, index=sources, name='Sources')
    pie_chart.plot.pie(fontsize=11, autopct='%.2f', figsize=(6, 6))
    plt.show()
