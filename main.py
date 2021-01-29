import random
from words import words
import string


def valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    # getting user input

    while len(word_letters) > 0:
        print('you have used these letters: ', ' '.join(used_letter))

        word_list = [letter if letter in used_letter else '_' for letter in word]
        print('current word: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

        elif user_letter in used_letter:
            print('you have already used this later. try again.')
        else:
            print('invalid character')




hangman()




