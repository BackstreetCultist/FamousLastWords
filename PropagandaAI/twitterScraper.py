# Imports
import GetOldTweets3 as got
import pandas as pd
import numpy as np

# Function the pulls tweets from a specific username and turns to csv file

# Parameters: (list of twitter usernames), (max number of most recent tweets to pull from)
def username_tweets_to_txt(username, count):
    # Creation of query object
    tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                            .setMaxTweets(count)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Creating list of chosen tweet data
    user_tweets = [[tweet.text] for tweet in tweets]

    # Creation of dataframe from tweets list
    tweets_df = pd.DataFrame(user_tweets, columns = ['Text'])

    # Converting dataframe to TXT
    np.savetxt(r'twitterYield.txt', tweets_df.values, fmt='%s')

username_tweets_to_txt("scrowder", 50)