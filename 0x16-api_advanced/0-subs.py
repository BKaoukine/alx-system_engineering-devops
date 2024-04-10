#!/usr/bin/python3
"""Number_of_subscribers function that queries the Reddit.

API and returns the number of subscribers.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """number_of_subscribers returns a number of subscribers."""
    username = 'ledbag123'
    password = 'Reddit72'

    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    client = requests.session()
    client.headers = headers

    resp = client.get(url, allow_redirects=False)
    if resp.status_code == 200:
        return (resp.json()["data"]["subscribers"])
    else:
        return(0)
