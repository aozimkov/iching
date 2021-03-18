from utils import *
from dicts import *

class Hexagram:
    def __init__(self, toss):
        self.toss = toss
        self.hexagram_key = self.get_hexagram_binary_key()

    def __repr__(self):
        print(self.get_hexagram_picture())
        return self.get_hexagram_description()

    def get_hexagram_binary_key(self):
        binary_hexagram_sum = bin(self.toss)
        key_without_0b = str(binary_hexagram_sum)[2:]
        ready_binary_key = "{0:0>6}".format(key_without_0b)
        return ready_binary_key

    def get_hexagram_description(self):
        return hexagrams_dict[self.hexagram_key]
    
    def get_hexagram_picture(self):
        hexagram_picture = ''
        binary_key = self.hexagram_key
        for symbol in reversed(binary_key):
            if symbol == '1':
                hexagram_picture += "_________\n"
            else:
                hexagram_picture += "___   ___\n"
        return hexagram_picture


def main():

    print_introduce()
    user_name = str(input("Please enter your name: "))

    # Game Loop
    while True:

        input("Hi, {user}! Please enter your question here or ask it in your mind\nand press ENTER button to start iChing:".format(user=user_name))

        hexagram = Hexagram(toss())
        print(hexagram)

        next_action = input("Press Enter to ask one more question or enter 'exit' and push Enter to close the program\n")

        if next_action.lower() == 'exit':
            print('Bye-bye!')
            break

if __name__ == "__main__":
    main()