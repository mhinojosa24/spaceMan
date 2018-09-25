# '''
# September 8, 2018
#
# Maximo Hinojosa
#
# This program called SpaceMan takes in a character
# input and checks if each letter is correct within
# aa array of words. Each word in the array has a length
# of 7 characters. If the letter is guessed right or wrong,
# I want the correct characters to be displayed green and red for
# incorrect. Once user guesed 7 correct or wrong characters of that word:
#  "You Won" or "You Lost".
#
#
# '''





#import nltk librarty to be able to sort through dictionary
from nltk.corpus import words
import random
import string


words = words.words()


global randomized_word
global ranWord_string
global spaces
global temp_array
words_array = []
guessed_letters = []
trys = 0
letters_in_str = guessed_letters
letters = ""



#function takes in the users input
def user_Input(prompt):
    user_input = input(prompt)
    return user_input


#function returns words the are less than or equal to 7 characters
def get_Dictionary(array):
    global words_array
    for word in array:
        if len(word) == 7:
            words_array.append(word)

    return words_array

get_Dictionary(words)

#function selects random words in global variable called words_array

def random_Word(user_Input):
    global randomized_word
    # global ranWord_array
    global temp_array
    global spaces
    spaces = []
    temp_array = []
    ranWord_string = ""
    # sgletter_append =[]


    randomized_word = random.choice(words_array)
    randomized_word = randomized_word.lower()
    # ranWord_array.append(randomized_word)

    for i in range(len(randomized_word)):
        spaces.append("_")

    # print(" ".join(spaces))


    for i in range(len(list(randomized_word))-1):
        if user_Input == list(randomized_word)[i]:
            print(user_input("hello"))
            spaces[i] = user_Input

    return spaces


random_Word(user_Input)
print(random_Word(user_Input))



#This function checks in guessed_letters to see if the user
#
def letters_tried(user_Input):
    if user_Input in randomized_word:
        guessed_letters.append(user_Input)
        if user_Input in guessed_letters:
            print("Letter already used. \n")
            guessed_letters.remove(user_Input)
            if user_Input != ascii:
                guessed_letters.remove(user_Input)




def is_not_ascii():
    if user_Input != ascii:
        print("This is not a letter, Try again.\n")




# def not_in_array():
#     if user_Input not in randomized_word:
#         print("This is not in array. Try again.\n")


def word_in_array():
    if user_Input in randomized_word:
        print("this letter is in array\n")


def verify_characters(user_Input):
    global trys
    if user_Input == "0":
        return False
        print(user_Input)
    elif len(user_Input) != 1:
        print("Please enter a single letter\n")
        return user_Input
    elif is_not_ascii():
        return user_Input
    elif user_Input not in randomized_word:
        letters_tried(user_Input)
        trys += 1
        if user_Input != ascii:
            trys -= 1
        else:
            if trys == 7:
                print("YOU LOSE!")
                return False
        return user_Input
    elif user_Input in randomized_word:
        letters_tried(user_Input)
        return user_Input
    else:
        return True


running = True
while running:
    # global letters
    selection = user_Input(
    "secret word: {} \n"
    "Trys: {} \n"
    "secret word: {} \n"
    "Guessed letters: {} \n".format(randomized_word, trys, " ".join(spaces), guessed_letters))
    running = verify_characters(selection)
