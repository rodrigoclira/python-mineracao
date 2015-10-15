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

    print tweets['programming'].value_counts()[True]
    print tweets['tutorial'].value_counts()[True]
    print tweets['relevant'].value_counts()[True]

    print tweets[tweets['relevant'] == True]['python'].value_counts()[True]
    print tweets[tweets['relevant'] == True]['javascript'].value_counts()[True]
    print tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]

    tweets_by_prg_lang = [tweets[tweets['relevant'] == True]['python'].value_counts()[True], 
                          tweets[tweets['relevant'] == True]['javascript'].value_counts()[True], 
                          tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]]
    x_pos = list(range(len(prg_langs)))
    width = 0.8
    fig, ax = plt.subplots()
    plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('Ranking: python vs. javascript vs. ruby (Relevant data)', fontsize=10, fontweight='bold')
    ax.set_xticks([p + 0.4 * width for p in x_pos])
    ax.set_xticklabels(prg_langs)
    plt.grid()
    plt.show()


