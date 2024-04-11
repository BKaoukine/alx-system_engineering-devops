#!/usr/bin/python3
"""Top_Ten function that queries the Reddit.

API and returns the top 10 hot posts of a given subreddit.
"""


import requests


def top_ten(subreddit):
    """Top_Ten returns top 10 hot posts of a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-agent': 'python-requests/2.22.0'}
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
