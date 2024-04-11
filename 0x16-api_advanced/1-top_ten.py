#!/usr/bin/python3
"""Top_Ten function that queries the Reddit.

API and returns the top 10 hot posts of a given subreddit.
"""


import requests
import sys
headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def top_ten(subreddit):
    """Top_Ten returns top 10 hot posts of a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json??limit=10"
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()

        for child in data['data']['children']:
            link_title = child['data']['title']
            print(link_title)

    else:
        print("None")
