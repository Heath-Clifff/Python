import json
from difflib import get_close_matches

data = json.load(open("data.json"))

while True:
    def translate(word):
        word = word.lower()

        if word in data:
            return data[word]

        if len(get_close_matches(word, data.keys())) > 0:
            yn = input(
                f"Did you mean {get_close_matches(word, data.keys())[0]}? Enter 'Y' or 'N'. ")

            if yn == "Y":
                return data[get_close_matches(word, data.keys())[0]]
            else:
                return f"Sorry, could not find the word '{word}'."

        else:
            print(f"Sorry, could not find the word '{word}'.")

    word = input("Enter the word: ")
    result = (translate(word))

    if isinstance(result, list):
        for word in result:
            print(word)

    user_input = input("Do you want to continue? Enter 'Y' or 'N'.")

    if user_input == "Y":
        continue
    else:
        break
