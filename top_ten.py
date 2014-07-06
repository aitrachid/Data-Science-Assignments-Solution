import sys
from collections import defaultdict
import json


def getHashtags(tweet):
    hashtags=[]
    entities=tweet.get('entities')
    if entities is None:
        return None

    for hashtag in entities.get('hashtags',[]):
        hashtags.append(hashtag.get('text'))
    return hashtags

def readTweets(file):
    scoreHashTags=defaultdict(int)
    TermsFreq = defaultdict(float)
    allTermes=0
    for line in file:
        tweet=json.loads(line)
        hashtags=getHashtags(tweet)
        if hashtags is not None:
            for hashtag in hashtags:
                if (hashtag is not None):
                    scoreHashTags[hashtag]+=1

    return  scoreHashTags

def sortDict(dictionnary):
    values_key_value=[(value,key) for key,value in dictionnary.items()]
    values_key_value.sort(reverse=True)
    return  values_key_value


def main():

    tweet_file = open(sys.argv[1])

    hashtags=readTweets(tweet_file)

    SortedHashTag=sortDict(hashtags)

    for (value,key) in SortedHashTag[:10]:
        print '%s %i'%(key,value)

if __name__ == '__main__':
    main()

