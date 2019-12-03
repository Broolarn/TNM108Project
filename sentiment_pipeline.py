import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pandas as pd
import math
import nltk
import piphelpers as piphelp
# ATM THE PIPELINE IS WORTHLESS BUT WILL LATER BE USED TO FIND BEST PARAMS
def line(url):
    
    tweets = pd.read_json (url)
    # Split data into training and test sets
    from sklearn.model_selection import train_test_split
    arraylen = len(tweets)
    x = tweets[0:math.floor(arraylen*0.5)] # ska egentligen vara text datan
    y = tweets[math.ceil(arraylen*0.5):arraylen] # ska egentligen vara sentiment redan lablad
    
    X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.20, random_state = 12,shuffle=True)
    tokenizer = CountVectorizer(min_df=1, tokenizer=nltk.word_tokenize)
    # tokenizer = nltk.casual.TweetTokenizer(preserve_case=False, reduce_len=True) # Your milage may vary on these arguments
    count_vect = CountVectorizer(tokenizer=tokenizer) 
    classifier = LogisticRegression()
    sentiment_pipeline = Pipeline([
        ('vectorizer', count_vect),
        ('classifier', classifier)
    ])

    
    sentiment_pipeline, confusion_matrix = piphelp.train_test_and_evaluate(sentiment_pipeline, X_train, y_train, X_test, y_test)
    # do sentimnet analysis here
    return sentiment_pipeline

