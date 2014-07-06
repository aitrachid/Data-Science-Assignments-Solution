import sys
from collections import defaultdict
import json

def lines(fp):

    PositifScores = defaultdict(int)
    NegatifScores = defaultdict(int)
    for line in fp:
        word,score=line.split('\t')
        score=int(score)
        if score>0:
            PositifScores[word]=score
        else:
            NegatifScores[word]=score

    return PositifScores,NegatifScores


def getTweetScores(PositifScores,tweets):
    TermsScores = defaultdict(float)

    positiveLen=0
    for tweet in tweets:
        text=tweet.get('text','')
        score=0
        for word in text.split():
            if PositifScores.__contains__(word):
                score+=1
                positiveLen+=1
        for word in text.split():
            TermsScores[word]+=score

    return TermsScores,positiveLen


def readTweets(file):
    tweets=[json.loads(line) for line in file]
    return  tweets

def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    PositifScores,NegatifScores=lines(sent_file)
    tweets=readTweets(tweet_file)
    terms,len=getTweetScores(PositifScores,tweets)
    for key,value in terms.items():
        print '%s %f'%(key,value/len)
if __name__ == '__main__':
    main()
