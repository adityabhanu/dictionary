import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        if len(get_close_matches(word, data.keys(), 3, 0.8)) > 0:
            yn = input("Did you mean %s instead? Enter Y if yes or N for no: " % get_close_matches(word, data.keys(), 3, 0.8)[0])
            if yn.lower() == 'y':
                return data[get_close_matches(word, data.keys(), 3, 0.8)[0]]
            elif yn.lower() == 'n':
                return "No matches found."
            else:
                return "we didn't understand your entry"

        return "No matches found"

user_input = input("Enter a word: ")

definition = translate(user_input)

if type(definition) == list:
    for idx, item in enumerate(definition):
        print(f"{idx}. {item}")
else:
    print(definition)
