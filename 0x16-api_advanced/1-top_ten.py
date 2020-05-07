#!/usr/bin/python3
"""
This module GETS data from an API
"""

import requests


def top_ten(subreddit):
    """
    Prints the hot posts that are on the top 10
    Endpoint: /r/{}/hot.json?limit=10
    """
    uri = "https://www.reddit.com"
    headers = {'User-Agent': 'Chrome/81.0.4044.138'}
    response = requests.get(uri + "/r/{}/hot.json?limit=10".format(subreddit),
                            headers=headers)
    if (response.status_code == 200):
        obj = response.json()
        posts = obj.get('data').get('children')
        for ea_post in posts:
            print(ea_post.get("data").get("title"))
    else:
        print("None")
