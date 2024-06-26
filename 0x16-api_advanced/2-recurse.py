#!/usr/bin/python3
"""Module that consumes the Reddit API and returns a list containing the.

titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recurse is a recursive function that queries the Reddit API.

    retrieving the titles of all hot articles for a specified subreddit.
    If no results are found for the given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None
    params = {"after": after} if after else {}
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "costum"},
        params=params,
    )

    if response.status_code == 200:
        if response.json()["data"]:
            data = response.json()["data"]
            for item in data["children"]:
                hot_list.append(item["data"]["title"])
            if data["after"]:
                return recurse(subreddit, hot_list, after=data["after"])
            else:
                return hot_list
    else:
        return None
