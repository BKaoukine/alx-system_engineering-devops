#!/usr/bin/python3
"""Number_of_subscribers function that queries the Reddit.

API and returns the number of subscribers.
"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """number_of_subscribers returns a number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
