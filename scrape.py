#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json

def get_cards():
    base_url = 'https://shadowverse-portal.com/api/v1/cards'
    data = {}
    data['format'] = 'json'
    data['lang'] = 'en'
    url_params = urllib.parse.urlencode(data)
    url = base_url + '?' + url_params
    with urllib.request.urlopen(url) as response:
        cards_json = json.loads(response.read())
        with open('cards.json', 'w', encoding='utf-8') as outfile:
            json.dump(cards_json['data'], outfile, ensure_ascii=False, indent=2)



def main() :
    get_cards()

if __name__ == "__main__":
    main()
