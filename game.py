#!/usr/bin/python3
import random
import graph

with open("words.txt") as file:
    list_words = file.read().splitlines()

word = random.choice(list_words)
length = len(word)
word = " ".join(word)
base = "_ " * length
basel = list(base)
del basel[-1]
n = 0  # defining number of attempts used
graph.fun(7)  # printing initial graph
print("")

while word != base:
    if n == 7:
        print("Game over.")
        exit()
    letter = input("Choose a letter: ")
    if letter in word:
        for index, char in enumerate(word):
            if char == letter:
                basel[index] = letter
    else:
        print("Wrong guess.")
        n = n + 1  # attempts used
        n1 = 7 - n  # attempts left
        graph.fun(n1)
        print("")
        print("You have", n1, "tries left.")
    base = "".join(basel)
    print(base)
    if word == base:
        print("Congratulations, you guessed the word.")
