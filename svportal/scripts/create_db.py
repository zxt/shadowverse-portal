#!/usr/bin/env python3
import sys
import os
import contextlib
import sqlite3
import json

sys.path.insert(1, os.path.realpath(os.path.pardir))
from enums import *

def create_db():
    with contextlib.suppress(FileNotFoundError):
        os.remove('db/cards.db')

    conn = sqlite3.connect('db/cards.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE cards (
                card_id INTEGER PRIMARY KEY,
                card_set_id INTEGER,
                card_name TEXT,
                char_type INTEGER,
                clan INTEGER,
                tribe_name TEXT,
                skill_disc TEXT,
                evo_skill_disc TEXT,
                cost INTEGER,
                atk INTEGER,
                life INTEGER,
                evo_atk INTEGER,
                evo_life INTEGER,
                rarity INTEGER,
                get_red_ether INTEGER,
                use_red_ether INTEGER,
                description TEXT,
                evo_description TEXT,
                base_card_id INTEGER,
                format_type INTEGER,
                restricted_count INTEGER,
                FOREIGN KEY(card_set_id) REFERENCES card_sets(id),
                FOREIGN KEY(char_type) REFERENCES card_types(id),
                FOREIGN KEY(clan) REFERENCES crafts(id),
                FOREIGN KEY(rarity) REFERENCES card_rarity(id)
            )""")

        tables = ('card_sets', 'card_types', 'crafts', 'card_rarity')
        for t in tables:
            cur.execute("""CREATE TABLE {0} (
                            id INTEGER PRIMARY KEY,
                            name TEXT
                        )""".format(t))

def populate_lookup_tables():
    conn = sqlite3.connect('db/cards.db')
    with conn:
        cur = conn.cursor()
        for cset in CARD_SETS:
            cur.execute('INSERT INTO card_sets values (?,?)', cset)
        for ctype in CARD_TYPES:
            cur.execute('INSERT INTO card_types values (?,?)', ctype)
        for craft in CRAFTS:
            cur.execute('INSERT INTO crafts values (?,?)', craft)
        for rarity in CARD_RARITYS:
            cur.execute('INSERT INTO card_rarity values (?,?)', rarity)

def populate_cards_table():
    filtered_card_list = []
    with open('json/all.json', 'r', encoding='utf-8') as infile:
        keys = ['card_id',
                'card_set_id',
                'card_name',
                'char_type',
                'clan',
                'tribe_name',
                'skill_disc',
                'evo_skill_disc',
                'cost',
                'atk',
                'life',
                'evo_atk',
                'evo_life',
                'rarity',
                'get_red_ether',
                'use_red_ether',
                'description',
                'evo_description',
                'base_card_id',
                'format_type',
                'restricted_count'
               ]
        cards_json = json.loads(infile.read())
        cards_list = cards_json['cards']
        for card_dict in cards_list:
            filtered_card_list.append(dict((k, card_dict[k]) for k in keys if k in card_dict))

    conn = sqlite3.connect('db/cards.db')
    with conn:
        cur = conn.cursor()
        for card_dict in filtered_card_list:
            columns = ', '.join(card_dict.keys())
            placeholders = ', '.join('?' * len(card_dict))
            cur.execute("""
                INSERT INTO cards
                    ({}) VALUES ({})
            """.format(columns, placeholders), tuple(card_dict.values()))

def main():
    create_db()
    populate_lookup_tables()
    populate_cards_table()

if __name__ == "__main__":
    main()
