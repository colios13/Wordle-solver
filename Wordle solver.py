# Wordle solver
import os

# Done First objective help you to play wordle 
    # Possible upgrade be able to use it only from the terminal
# TODO Second objective be able to play wordle with it
# TODO Third objective be able to play wordle against herself

file_path = os.path.realpath(__file__).replace(os.path.basename(__file__),"")
l_valid_words = []

# Store our dictionnary file in a list
with open(file_path + 'valid_word_wordle.txt') as dictionary:
    l_valid_words = dictionary.read().splitlines()

s_valid_words = set(l_valid_words)

# We chose salet for the first word because based on MIT research it looks to be the best starting word
first_word = "salet" # alternative slate

# I have chosed to have a second word to eliminate all the vowels except y, have chosed this word using a precedent version of this tools 
# also choosed this one particularly because it's an easy word to find
second_word = "opium"

all_tested_words = first_word + second_word
third_word_possibility = []

# Chose the the best third word
for word in l_valid_words:
    # finding word with an y, who desn't have more than 1 letter in common with our first two word and without repetitive letter
    if sum(letter in word for letter in all_tested_words) < 2 and "y" in word and len(word) - len(set(word)) < 1:
        third_word_possibility += [word]

third_word = third_word_possibility[0] # Default chynd "cut into chines (for cooking)" 
                                       # or angry for different dictionnary 

let_know_pos = ["","","","",""] # Letter in word with knowed position (index correspond to the letter position)
let_unknow_pos = [["",[]],["",[]],["",[]],["",[]],["",[]]] # Letter in word but with unknow position, mark the checked position in the second array (0 indexed)

#add 4th-5th... tested words without spaces
user_chosen_words = ""
all_tested_words = third_word + user_chosen_words

# list of letter wich are not present in the word we need to guess
banned_letter = [letter for letter in all_tested_words if (letter not in let_know_pos and all(letter != e[0] for e in let_unknow_pos))]

possible_words = []

# Iterate on our dictionnary and compute the valids word(s)
for word in l_valid_words:
    # check the fact that the word has the letter with known position at the right place 
    check_l_know = all(word[i] == letter if len(letter) else 1 for i, letter in enumerate(let_know_pos))
    # check the fact that the word has the letter with unknown position but not at the position we already tried 
    check_l_unknow = all(all(word[i] !=e [0] for i in e[1]) and e[0] in word if len(e[0]) else 1 for e in let_unknow_pos )

    # Check the word does'nt contain banned letter and combine it with the precedent check result
    if all(letter not in banned_letter for letter in word) and check_l_know and check_l_unknow:
        possible_words += [word]

# Print the possible word(s) and let the user chose one
print("Tips: chose the most common word / or the one with biggest number of different letters")
print(len(possible_words), possible_words)