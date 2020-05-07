#!/usr/bin/python3
"""
This module GETS data from an API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Prints the hot posts that are on the top 10
    Endpoint: /r/{}/hot.json?limit=10
    """
    uri = "https://www.reddit.com/r/"
    headers = {'User-Agent': 'Chrome/81.0.4044.138'}
    new_uri = uri + "{}/hot.json?limit=200&after={}".format(subreddit, after)
    response = requests.get(new_uri, headers=headers)

    if (response.status_code == 200):
        obj = response.json()
        posts = obj.get('data').get('children')

        after = obj.get("data").get("after")
        for ea_post in posts:
            hot_list.append(ea_post.get("data").get("title"))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
