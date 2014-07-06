import sys
from collections import defaultdict
import json

states = {
 'alaska' :'AK',
'alabama' :'AL',
'arkansas' :'AR',
'american samoa' :'AS',
'arizona' :'AZ',
'california' :'CA',
'colorado' :'CO',
'connecticut' :'CT',
'district of columbia' :'DC',
'delaware' :'DE',
'florida' :'FL',
'georgia' :'GA',
'guam' :'GU',
'hawaii' :'HI',
'iowa' :'IA',
'idaho' :'ID',
'illinois' :'IL',
'indiana' :'IN',
'kansas' :'KS',
'kentucky' :'KY',
'louisiana' :'LA',
'massachusetts' :'MA',
'maryland' :'MD',
'maine' :'ME',
'michigan' :'MI',
'minnesota' :'MN',
'missouri' :'MO',
'northern mariana islands' :'MP',
'mississippi' :'MS',
'montana' :'MT',
'national' :'NA',
'north carolina' :'NC',
'north dakota' :'ND',
'nebraska' :'NE',
'new hampshire' :'NH',
'new jersey' :'NJ',
'new mexico' :'NM',
'nevada' :'NV',
'new york' :'NY',
'ohio' :'OH',
'oklahoma' :'OK',
'oregon' :'OR',
'pennsylvania' :'PA',
'puerto rico' :'PR',
'rhode island' :'RI',
'south carolina' :'SC',
'south dakota' :'SD',
'tennessee' :'TN',
'texas' :'TX',
'utah' :'UT',
'virginia' :'VA',
'virgin islands' :'VI',
'vermont' :'VT',
'washington' :'WA',
'wisconsin' :'WI',
'west virginia' :'WV',
'wyoming' :'WY',
'alberta' :'AB',
'british columbia' :'BC',
'manitoba' :'MB',
'new brunswick' :'NB',
'newfoundland and labrador' :'NL',
'northwest territories' :'NT',
'nova scotia' :'NS',
'nunavut' :'NU',
'ontario' :'ON',
'prince edward island' :'PE',
'quebec' :'QC',
'saskatchewan' :'SK',
'yukon' :'YT',
'alberta' :'AB',
'british columbia' :'BC',
'manitoba' :'MB',
'new brunswick' :'NB',
'newfoundland and labrador' :'NL',
'nova scotia' :'NS',
'ontario' :'ON',
'prince edward island' :'PE',
'quebec' :'QC',
'saskatchewan' :'SK',
'northwest territories' :'NT',
'nunavut' :'NU',
'yukon' :'YT'
}


def lines(fp):
    scores = defaultdict(int)
    for line in fp:
        word,score=line.split('\t')
        scores[word]=int(score)
    return scores



def readTweets(file):
    tweets=[json.loads(line) for line in file]
    return  tweets


def getTweetScore(scores,tweet):
    text=tweet.get('text','')
    scoreTweet=0
    for word in text.split():
        scoreTweet+=scores.get(word,0)
    return scoreTweet

def getPlace(tweet):
    user=tweet.get('user')
    if user is None:
        return None
    place=user.get('location','')
    return states.get(place.lower())

def getStatTweetScores(Scores,tweets):
    ScoresStats = defaultdict(int)
    for tweet in tweets:
        place=getPlace(tweet)
        if place is not None:
            ScoresStats[place]=getTweetScore(Scores,tweet)

    return ScoresStats

def sortDict(dictionnary):
    values_key_value=[(value,key) for key,value in dictionnary.items()]
    values_key_value.sort(reverse=True)
    return  values_key_value

def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    Scores=lines(sent_file)
    tweets=readTweets(tweet_file)
    ScoresStats=getStatTweetScores(Scores,tweets)

    ScoresStats=sortDict(ScoresStats)
    (value,key)=ScoresStats[0]
    print '%s'%(key)

if __name__ == '__main__':
    main()
