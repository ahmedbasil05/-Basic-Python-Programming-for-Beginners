#RANDOM MOUDLE

import random

number = random.randint(0,5)
print(number)  #print a random integer

floating = random.random()
print(floating)  #print a random floating number

options = ("rock", "paper","scissor")
print(random.choice(options))  #print a random choice - useful for multiple choices

cards = ["2","5","Q","K","6","J"]
print(random.shuffle(cards))  #randomly shuffles the cards
