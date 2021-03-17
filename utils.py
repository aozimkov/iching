import random

def print_introduce():
    with open('introduce.txt') as file:
        print(file.read())

def toss():
    return random.randint(0, 63)