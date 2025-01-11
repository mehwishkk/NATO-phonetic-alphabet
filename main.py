import pandas
# dict_comprehension = {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for(index,row) in data.iterrows() }
print(phonetic_dict)
word = input("Enter a word: ").upper()

list_output = [phonetic_dict[letter] for letter in word]
print(list_output)
