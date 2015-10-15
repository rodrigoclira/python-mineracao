#!/bin/python
import re
import json
import pandas as pd
import matplotlib.pyplot as plt

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

if __name__ == '__main__':
    
    tweets_data_path = 'twitter_data.txt'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    tweets = pd.DataFrame()

    texts = []
    langs = []
    countries = []
    for line, tweet in enumerate(tweets_data):
        #print line, tweet
        try:
            texts.append(tweet['text'])
#            langs.append(tweet['lang'])
#            countries.append(tweet['place']['country'] if tweet['place'] != None else None)
        except:
            print "Error line %d" % (line)
            

    tweets['text'] = texts
#    tweets['lang'] = langs
#    tweets['country'] = countries

    #Mining
    tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
    tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
    tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))

    tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
    tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))

    tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))

    tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

    tweets_relevant = tweets[tweets['relevant'] == True]
    tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

    print tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link']
    print tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link']
    print tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link']
    plt.show()


