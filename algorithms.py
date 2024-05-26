"""
params: dict {
    'index': int,                           # Current index of the flashcard
    'data': list                            # The flashcards data
    'currentCard': {front: str, back: str}  # The current flashcard
    
    (only in def logic call)
    'user_input': str                       # Input from the user
}
"""

"""
BOILERPLATE ALGORITHM

class Algorithm:
    def __init__(self):
        # state variables go here
    
    # function which is called on initialization
    # intended for displaying commands
    def initialDisplay(self):
        print("- `exit` | end session")
        print("[ enter to start ]")
        
    # called after logic, to display the next card
    def display(self, params):
        # this code will print the front of the current card
        print(params["currentCard"][0])
        
    # called to respond to user input and trigger next card
    def logic(self, params):
        
        next_index = 0
        
        # return the next index to be shown (required)
        return next_index
"""
import math
import random
import os

class FlashcardsAlgorithm:
    def __init__(self):
        self.flipped = 0  # State variable to track if the card is flipped
    
    def initialDisplay(self, params):
        # Display the available commands for the flashcard algorithm
        print("- `n` | move to next card")
        print("- `b` | move back one card")
        print("- `f` | flip card")
        
    def display(self, params):
        # Display the current side of the card
        print(params['currentCard'][self.flipped])

    def logic(self, params):
        # Process the user input and update the state accordingly
        next_index = params['index']
        if params['user_input'] == 'n':
            next_index = (params['index'] + 1) % len(params['data'])
            self.flipped = 0  # Reset to show the front of the next card
        elif params['user_input'] == 'b':
            next_index = (params['index'] - 1) % len(params['data'])
            self.flipped = 0  # Reset to show the front of the previous card
        elif params['user_input'] == 'f':
            self.flipped = 1 - self.flipped  # Toggle between front and back
        
        return next_index  # Return the index of the next card to show


class WrittenAlgorithm:
    def __init__(self):
        self.correct = []  # List to keep track of correctly answered cards
        self.round = 0  # Variable to track the number of rounds
    
    def initialDisplay(self, params):
        # Display the initial message and commands for the written algorithm
        print("Written study")
        print("type your answer to the question")
        
        # Get user input to start the session
        input("- `exit` | ends the session\n[ enter to start ]")
        self.display(params)
        
    def display(self, params):
        # Display the current progress and the front of the card
        centerSize = os.get_terminal_size().columns - len(f"correctly answered {len(self.correct)}") - len(f"round {self.round}")
        print(f"correctly answered {len(self.correct)}{(''.center(centerSize))}round {self.round}\n")
        print(params['currentCard'][0])

        
    def displayCheck(self, params, result):
        # Display whether the user's answer was correct or incorrect
        print("Correct!" if result else "Incorrect.")
        print(f"You said {params['user_input']}")
        print(f"The answer was {params['currentCard'][1]}")

    def logic(self, params):
        # Process the user's input and update the state accordingly
        if params['user_input'] == params['currentCard'][1]:
            self.correct.append(params['index'])  # Add to correct list if the answer is correct
            self.displayCheck(params, True)
        else:
            self.displayCheck(params, False)
        input("[ enter ]")
        
        # Check if all cards have been answered correctly
        if len(self.correct) == len(params['data']):
            self.correct = []  # Reset the correct list for a new round
            self.round += 1  # Increment the round counter
        
        # Select the next card to show, ensuring it's not already answered correctly
        next_index = random.randrange(0, len(params['data']), 1)
        while next_index in self.correct or next_index == params['index']:
            next_index = random.randrange(0, len(params['data']), 1)
        return next_index  # Return the index of the next card to show

# Dictionary of algorithms
algorithms = {
    # !!! DONT REMOVE "flashcards" !!!
    # flashcards is the automatic choice when entering the program
    # removing it will permanently break the program until it is restored
    "flashcards": FlashcardsAlgorithm,
    "written": WrittenAlgorithm
}
