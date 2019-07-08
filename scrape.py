#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json
import sys
from pkgutil import simplegeneric

@simplegeneric
def get_items(obj):
    while False: # no items, a scalar object
        yield None

@get_items.register(dict)
def _(obj):
    return obj.items() # json object

@get_items.register(list)
def _(obj):
    return enumerate(obj) # json array

def strip_whitespace(json_data):
    for key, value in get_items(json_data):
        if hasattr(value, 'strip'): # json string
            json_data[key] = value.strip()
        else:
            strip_whitespace(value) # recursive call

def get_cards():
    base_url = 'https://shadowverse-portal.com/api/v1/cards'
    data = {}
    data['format'] = 'json'
    data['lang'] = 'en'
    url_params = urllib.parse.urlencode(data)
    url = base_url + '?' + url_params
    with urllib.request.urlopen(url) as response:
        cards_json = json.loads(response.read())
        strip_whitespace(cards_json)
        with open('json/cards.json', 'w', encoding='utf-8') as outfile:
            json.dump(cards_json['data'], outfile, ensure_ascii=False, indent=2)

def main() :
    get_cards()

if __name__ == "__main__":
    main()
