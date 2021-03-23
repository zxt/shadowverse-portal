#!/usr/bin/env python3
import json
import re
import argparse

def main(input_file, sets, rarity) :
    filtered_list = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        cards_json = json.loads(infile.read())
        cards_list = cards_json['cards']

        filtered_list = [card_dict for card_dict in cards_list if card_dict['card_set_id'] in sets and card_dict['rarity'] in rarity]

    with open('filtered.json', 'w', encoding='utf-8') as outfile:
        json.dump(filtered_list, outfile, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    desc = ("Helper script to filter cards.json file by card set and rarity,"
            "for purpose of batch processing card set reveal dumps")
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input',
                         help="JSON file containing card data")

    parser.add_argument('sets', nargs='+', type=int,
                        help="sets to filter and include")

    parser.add_argument('-r', '--rarity', nargs='*', type=int, default=[1,2],
                        help="rarity to filter by (defaults to bronze and silver)")
    
    args = parser.parse_args()

    main(args.input, args.sets, args.rarity)