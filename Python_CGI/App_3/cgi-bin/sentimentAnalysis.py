import pandas as pd
import numpy as np

from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer,TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split

def train():
    imdb = pd.read_csv("C:\\Users\\Akhilesh Kr. Pandey\\Desktop\\WebML\\App_3\\cgi-bin\\SentimentAnalysis\\imdb_labelled.txt",sep='\t',header=None)
    amazon = pd.read_csv("C:\\Users\\Akhilesh Kr. Pandey\\Desktop\\WebML\\App_3\\cgi-bin\\SentimentAnalysis\\amazon_cells_labelled.txt",sep='\t',header=None)
    yelp = pd.read_csv("C:\\Users\\Akhilesh Kr. Pandey\\Desktop\\WebML\\App_3\\cgi-bin\\SentimentAnalysis\\yelp_labelled.txt",sep='\t',header=None)

    df = pd.DataFrame()
    df = pd.concat([imdb,amazon,yelp],ignore_index=True)
    df.columns = ['Review','Sentiment']
    tokenList = []

    for i in range(df.shape[0]):
        tokenList.append(word_tokenize(df['Review'].iloc[i]))

    stopwords_list = stopwords.words('english')
    stopwords_list.extend([',','.','-','!',"(",")"])
    wordsList = []

    for tokens in tokenList:
        word_temp = []
        for word in tokens:
            if word.lower() not in stopwords_list:
                word_temp.append(word.lower())
        wordsList.append(word_temp)


    wnet = WordNetLemmatizer()

    for i in range(len(wordsList)):
        for j in range(len(wordsList[i])):
            wordsList[i][j] = wnet.lemmatize(wordsList[i][j],pos='v')


    wordsList = np.asarray(wordsList)

    for i in range(len(wordsList)):
        wordsList[i] = ' '.join(wordsList[i])


    cv = CountVectorizer()       

    vector = cv.fit_transform(wordsList)

    reg = LogisticRegression()

    y = df['Sentiment'].values

    xtrain,xtest,ytrain,ytest = train_test_split(vector,y,test_size=0.25)

    reg.fit(xtrain,ytrain)

    ypred = reg.predict(xtest)
    return cv,reg,stopwords_list,wnet

def test(msg,cv,reg,stopwords_list,wnet):
    rev = msg

    tokens = word_tokenize(rev)

    wordsL = []
    for word in tokens:
        if word.lower() not in stopwords_list:
            wordsL.append(word.lower())

    for i in range(len(wordsL)):
        wordsL[i] = wnet.lemmatize(wordsL[i],pos='v')

    sent = []
    sent = ' '.join(wordsL)
    vect = cv.transform([sent])
    senti = reg.predict(vect)

    return senti[0]

# for testing purpose
if __name__ == '__main__':
    cv,reg,stopw,wnet = train()
    senti = test("Bad Movie",cv,reg,stopw,wnet)
    print(senti)
    pass

