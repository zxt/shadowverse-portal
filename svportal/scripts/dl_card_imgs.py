#!/usr/bin/env python3
import argparse
import json
import os
import urllib.request

BASE_CARD_URL = "https://shadowverse-portal.com/image/card/phase2/common/C/C_"

def main(input_file, out_dir):
    with open(input_file, 'r', encoding='utf-8') as infile:
        cards_json = json.loads(infile.read())
        try:
            cards_list = cards_json['cards']
        except:
            cards_list = cards_json
    
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)

        for card in cards_list:
            card_id = str(card['card_id'])
            output = out_dir+'/C_'+card_id+'.png'
            with open(output, 'wb') as handle:
                urllib.request.urlretrieve(BASE_CARD_URL+card_id+'.png', output)


if __name__ == "__main__":
    desc = ("Download card images from shadowverse-portal "
            "for each card in the input JSON file")
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input',
                         help="JSON file containing card data")
    parser.add_argument('out_dir', nargs='?', default='card_imgs/',
                         help="Directory where downloaded images will be placed")
    
    args = parser.parse_args()

    main(args.input, args.out_dir)