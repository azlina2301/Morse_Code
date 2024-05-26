import pandas as pd

data = pd.read_csv('Morse_Code.csv')

# Cleansing the data
data = data.drop(columns=['Unnamed: 2', 'Unnamed: 3'])


# Use the dictionary comprehension to associate the letter to Morse Code
morse_dict = {row.Letter: row.Morse for index, row in data.iterrows()}

# Request the user input
user_input = input("Please write any word that you would to encode into Morse Code: ").upper()

# convert the letter into Morse code
for word in user_input:
    print(morse_dict[word], end="")
