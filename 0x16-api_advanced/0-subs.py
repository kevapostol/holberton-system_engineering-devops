#!/usr/bin/python3
"""
This module GETS data from an API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    Endpoint: /r/{}/about.json
    """
    uri = "https://www.reddit.com"
    headers = {'User-Agent': 'Chrome/81.0.4044.138'}
    response = requests.get(uri + "/r/{}/about.json".format(subreddit),
                            headers=headers)
    if (response.status_code == 200):
        obj = response.json()
        subs = obj.get('data').get('subscribers')
        return subs
    else:
        return 0
