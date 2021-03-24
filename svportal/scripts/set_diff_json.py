#!/usr/bin/env python3
import json
import re
import argparse

def main(input1, input2, output):
    with open(input1, 'r', encoding='utf-8') as infile1:
        cards_json1 = json.loads(infile1.read())
        try:
            cards_list1 = cards_json1['cards']
        except:
            cards_list1 = cards_json1

    with open(input2, 'r', encoding='utf-8') as infile2:
        cards_json2 = json.loads(infile2.read())
        try:
            cards_list2 = cards_json2['cards']
        except:
            cards_list2 = cards_json2

    output_json = [d for d in cards_list1 if d not in cards_list2]

    with open(output, 'w', encoding='utf-8') as outfile:
        json.dump(output_json, outfile, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    desc = ("Get set diff of two JSON files of card data (input1 - input2)")
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input1',
                         help="1st JSON file containing card data")

    parser.add_argument('input2',
    help="2nd JSON file containing card data")

    parser.add_argument('-o', '--output', default="cards_diff.json",
    help="file to output the resulting JSON to")

    args = parser.parse_args()

    main(args.input1, args.input2, args.output)