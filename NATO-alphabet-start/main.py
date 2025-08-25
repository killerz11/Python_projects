import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

is_on = True
while is_on:
    word = input("Give the word  ").upper()
    try:
        #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
        phonetic_code_list = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry! you gave the wrong input")
    else:
        print(phonetic_code_list)
        is_on = False