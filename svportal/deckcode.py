#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json
import sys

def get_hash(deck_code):
    """
    This generates a deck hash with the given deck code.

    Args:
        deck_code: The deck code to hash. Valid codes should be 4 characters long.

    Returns:
        A valid deck hash string if the api call was a success.
        A valid hash will look something like:
            1.6.6YBRY.6b_5S.5_pF2.6Y8W2.6YAyI.6YFqo.6fmoW.6jiFy.6nP42 [...]

    Raises:
        ValueError: The deck code provided is invalid or has expired

    """
    base_url = 'https://shadowverse-portal.com/api/v1/deck/import'
    data = {}
    data['format'] = 'json'
    data['lang'] = 'en'
    data['deck_code'] = deck_code
    url_params = urllib.parse.urlencode(data)
    url = base_url + '?' + url_params
    with urllib.request.urlopen(url) as response:
        response_json = json.loads(response.read())
        data = response_json['data']
        if data['errors']:
            raise ValueError(data['errors'])
        return data['hash']


def get_deck(deck_hash):
    """
    This generates a deck with the given deck hash

    Args:
        deck_hash: A deck hash returned by a call to get_hash()

    Returns:
        A dictionary containing info about the deck generated.
        Dict has 3 keys 'deck_format', 'clan', and 'cards'

    Raises:
        ValueError: The hash provided is invalid.

    """
    base_url = 'https://shadowverse-portal.com/api/v1/deck'
    data = {}
    data['format'] = 'json'
    data['lang'] = 'en'
    data['hash'] = deck_hash
    url_params = urllib.parse.urlencode(data)
    url = base_url + '?' + url_params
    with urllib.request.urlopen(url) as response:
        response_json = json.loads(response.read())
        data = response_json['data']
        if not data:
            raise ValueError("Invalid deck hash provided.")
        return data['deck']
