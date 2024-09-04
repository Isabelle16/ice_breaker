import os
from dotenv import load_dotenv

load_dotenv()

import tweepy
import requests


def scrape_user_tweets(username, num_tweets=5, mock: bool = True):
    """
    Scrape a user's original tweets and return them as a list of dictionaries. Each dictionary should have 3 fields: "time_posted", "next" and "url".
    """
    tweet_list = []

    if mock:
        TWITTER_GIST = "https://gist.githubusercontent.com/emarco177/9d4fdd52dc432c72937c6e383dd1c7cc/raw/1675c4b1595ec0ddd8208544a4f915769465ed6a/eden-marco-tweets.json"
        tweets = requests.get(TWITTER_GIST, timeout=5).json()

        for tweet in tweets:
            tweet_dict = {
                "time_posted": tweet["time_posted"],
                "text": tweet["text"],
                "url": f"https://twitter.com/{username}/status/{tweet["id"]}",
            }
            tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":
    # Test the function
    tweets = scrape_user_tweets(username="isabellamasiero")
    print(tweets)
