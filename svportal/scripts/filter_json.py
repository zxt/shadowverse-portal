#!/usr/bin/env python3
import json
import re
import argparse

def main(input_file, output_file, sets, rarity) :
    filtered_list = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        cards_json = json.loads(infile.read())
        try:
            cards_list = cards_json['cards']
        except:
            cards_list = cards_json

        # card_dict['card_name'] is not None to filter out cards where card_name is null
        # (those are special uncollectible tokens)
        filtered_list = [card_dict for card_dict in cards_list 
                            if card_dict['card_set_id'] in sets and 
                            card_dict['rarity'] in rarity and card_dict['card_name'] is not None]

    with open(output_file, 'w', encoding='utf-8') as outfile:
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

    parser.add_argument('-o', '--output', default="filtered.json",
    help="file to output the resulting JSON to")

    parser.add_argument('-r', '--rarity', nargs='*', type=int, default=[1,2],
                        help="rarity to filter by (defaults to bronze and silver)")
    
    args = parser.parse_args()

    main(args.input, args.output, args.sets, args.rarity)