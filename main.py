import random
from art import *
TRIES = 6


def initial_display_word(word):
    word_dictionary = {}
    p = random_alphabet(word)
    for x in range(len(word)):
        if word[x] == p:
            word_dictionary[x] = True
            print(word[x], end="")
        else:
            print(" _ ", end="")
            word_dictionary[x] = False
    print(word_dictionary)
    return word_dictionary


def random_alphabet(word):
    if len(word) > 3:
        return word[random.randrange(0, len(word) - 1)]


def get_all_trues(w_dic):
    counter = 0
    for x in w_dic:
        if w_dic.get(x) is True:
            counter += 1
            if counter == len(word):
                return True


def guess_the_word(word, w_dic, score, mistakes):
    if get_all_trues(w_dic):
        print("YOu WIN")
        return True
    elif mistakes == TRIES:
        print("yOu LoSe")
        return False
    else:
        character = input("Enter a letter (a-z):")
        if character not in word:
            mistakes = mistakes + 1
            display_word(word, w_dic)
            display_hangman(score, mistakes)
        for x in range(len(word)):
            if word[x] == character:
                w_dic[x] = True
                score = score + 1
        display_word(word, w_dic)
        display_hangman(score, mistakes)
        guess_the_word(word, w_dic, score, mistakes)


def display_word(word, w_dic):
    for x, y in w_dic.items():
        if y is False:
            print(" _ ", end="")
        else:
            print(word[x], end="")


def display_hangman(score, mistakes):
    print()
    print(initial)
    print_info(mistakes, score)
    print()
    if mistakes == 1:
        print()
        print(first_mistake)
        print_info(mistakes, score)
        print()
    if mistakes == 2:
        print()
        print(second_mistake)
        print_info(mistakes, score)
        print()
    if mistakes == 3:
        print()
        print(third_mistake)
        print_info(mistakes, score)
        print()
    if mistakes == 4:
        print()
        print(fourth_mistake)
        print_info(mistakes, score)
        print()
    if mistakes == 5:
        print()
        print(fifth_mistake)
        print_info(mistakes, score)
        print()
    if mistakes == 6:
        print()
        print(six_mistake)
        print_info(mistakes, score)
        print()


def hangman_game(word):
    score = 0
    mistakes = 0
    w_dic = initial_display_word(word)
    display_hangman(score, mistakes)
    result = guess_the_word(word, w_dic, score, mistakes)

def print_info(mistakes, score):
    print("Mistakes: ", mistakes)
    print("Score: ", score)

if __name__ == '__main__':
    word = input("Enter the word")
    print("Begin: ")
    hangman_game(word)
