#!/bin/python
# -*- coding: utf-8 -*-
import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'twitter_data.txt'


if __name__ == '__main__':
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue


    print len(tweets_data)

    tweets = pd.DataFrame()

    texts = []
    langs = []
    countries = []
    for line, tweet in enumerate(tweets_data):
        #print line, tweet
        try:
            texts.append(tweet['text'])
            langs.append(tweet['lang'])
            countries.append(tweet['place']['country'] if tweet['place'] != None else None)
        except:
            print "Error line %d" % (line)
            

    tweets['text'] = texts
    tweets['lang'] = langs
    tweets['country'] = countries

#    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
#    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
#    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

    tweets_by_lang = tweets['lang'].value_counts()

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel(u'Línguas', fontsize=15)
    ax.set_ylabel(u'Número de tweets' , fontsize=15)
    ax.set_title(u'Top 5 línguas', fontsize=15, fontweight='bold')
    tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')


    tweets_by_country = tweets['country'].value_counts()
    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel(u'Países', fontsize=15)
    ax.set_ylabel(u'Número de tweets' , fontsize=15)
    ax.set_title(u'Top 5 países', fontsize=15, fontweight='bold')
    tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

    plt.show()
