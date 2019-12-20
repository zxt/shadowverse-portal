#!/usr/bin/env python3
import sys
import os
import json

sys.path.insert(1, os.path.realpath(os.path.pardir))

import cards

def main() :
    craft = 0
    if len(sys.argv) == 2:
        craft = int(sys.argv[1])

    crafts = ['all', 'forest', 'sword', 'rune', 'dragon', 'shadow', 'blood', 'haven', 'portal']

    if craft == 0:
        for i, c in enumerate(crafts):
            cards_json = cards.get_cards(i)
            with open('json/'+c+'.json', 'w', encoding='utf-8') as outfile:
                json.dump(cards_json, outfile, ensure_ascii=False, indent=2)
    else:
        cards_json = cards.get_cards(craft)
        with open('json/'+crafts[craft]+'.json', 'w', encoding='utf-8') as outfile:
            json.dump(cards_json, outfile, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
