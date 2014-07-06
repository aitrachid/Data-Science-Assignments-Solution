import sys
from collections import defaultdict
import json


def lines(fp):

    scores = defaultdict(int)
    for line in fp:
        word,score=line.split('\t')
        scores[word]=int(score)
    return scores

def readTweets(file):
    tweets=[json.loads(line) for line in file]
    return  tweets


def getTweetScores(scores,tweets):

    scoreTweets=[]
    for tweet in tweets:
        text=tweet.get('text','')
        scoreTweet=0
        for word in text.split():
            scoreTweet+=scores.get(word,0)
        scoreTweets.append(scoreTweet)
    return scoreTweets

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores=lines(sent_file)
    tweets=readTweets(tweet_file)
    stweetsScore=getTweetScores(scores,tweets)

    for t in stweetsScore:
        print t

if __name__ == '__main__':
    main()
