# shadowverse-portal

Python wrappers around unofficial APIs to [shadowverse-portal](https://shadowverse-portal.com/), as well as related scripts and files

## Installation/Setup

You can install using pip after cloning the repo:

```bash
git clone https://github.com/zxt/shadowverse-portal
cd <your-project>
pip install <path/to/where/you/cloned/shadowverse-portal>
```
## Usage/Examples

```python
import svportal

all_cards = svportal.cards.get_cards()
print(all_cards)

my_deck_hash = svportal.deckcode.get_hash("pd0204")
print(my_deck_hash)

my_deck = svportal.deckcode.get_deck(my_deck_hash)
print(my_deck)
```
## Scripts

There are useful scripts in `svportal/scripts/`. The two most notable ones are `create_json.py` and `create_db.py`.

`create_json.py`: This script downloads all the card data and saves them as JSON files under `./json/`

`create_db.py`: This script takes data from `./json/all.json` and populates a SQLite database. The resulting file is saved in `./db/cards.db`

## Acknowledgements

 - [Shadowverse Card API](https://gist.github.com/theabhishek2511/dfd54989013254324cc4d67f1dbc9f7f)

## License

[MIT](https://github.com/zxt/shadowverse-portal/blob/master/LICENSE)
