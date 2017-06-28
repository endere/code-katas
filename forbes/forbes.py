"""Code for finding the oldest (under 80) and youngest billionaires from a json file."""
import json
with open('data.json') as data_file:
    data = json.load(data_file)
#json reader found at https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-using-python


def find_billionaires(info):
    """Return two lists, presenting the oldest and youngest billionaires from the provided json file."""
    highest_age = 0
    lowest_age = 100
    for person in info:
        try:
            if person['age'] > highest_age and person['age'] < 80:
                if person['net_worth (USD)'] >= 1000000000:
                    oldest = [person['name'], person['net_worth (USD)'], person['source']]
                    highest_age = person['age']
            elif person['age'] < lowest_age and person['age'] > 0:
                if person['net_worth (USD)'] >= 1000000000:
                    youngest = [person['name'], person['net_worth (USD)'], person['source']]
                    lowest_age = person['age']
        except TypeError:
            continue
    print(lowest_age, highest_age)
    return (oldest, youngest)


if __name__ == '__main__':
    print(find_billionaires(data))
