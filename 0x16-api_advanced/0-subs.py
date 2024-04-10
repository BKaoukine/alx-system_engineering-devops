#!/usr/bin/python3
"""Number_of_subscribers function that queries the Reddit.

API and returns the number of subscribers.
"""

import sys
import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers returns a number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    resp = requests.get(url, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        return data['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    subreddit = sys.argv[1]
    num_subscribers = number_of_subscribers(subreddit)
    print(num_subscribers)
