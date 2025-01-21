import pandas
# dict_comprehension = {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for(index,row) in data.iterrows() }

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        list_output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry,only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list_output)


generate_phonetic()
