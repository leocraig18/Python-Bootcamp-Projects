import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(dictionary)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only use letters.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
