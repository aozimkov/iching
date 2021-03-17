from utils import *
from dicts import *

class Hexagram:
    def __init__(self, toss):
        self.toss = toss

    def __repr__(self):
        for side in self.get_hexagram_binary_string():
            if side == '1':
                print("_________")
            else:
                print("___   ___")
        return hexagrams[self.get_hexagram_number()-1]

    def get_hexagram_binary_string(self):
        binary_hexagram_sum = bin(self.toss)
        key_without_0b = str(binary_hexagram_sum)[2:]
        ready_binary_key = "{0:0>6}".format(key_without_0b)
        return ready_binary_key

    def get_hexagram_number(self):
        return hexagon_numbers_dict[self.get_hexagram_binary_string()]


def main():

    # Print out the game introducing
    print_introduce()

    # Get user name
    user_name = str(input("Please enter your name: "))

    # Game Loop
    while True:

        # # Print a start message
        input("Hi, {user}! Please enter your question here or ask it in your mind\nand press ENTER button to start iChing:".format(user=user_name))

        # # Generate and draw the Hexagram
        hexagram = Hexagram(toss())
        
        # # Print out information about this Hexagram from the Book of Changes
        print(hexagram)

        # # User dialog 
        next_action = input("Press Enter to ask one more question or enter 'exit' and push Enter to close the program")

        if next_action.lower() == 'exit':
            print('Bye-bye!')
            break

if __name__ == "__main__":
    main()
