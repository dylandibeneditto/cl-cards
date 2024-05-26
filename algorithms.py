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

class FlashcardsAlgorithm:
    def __init__(self):
        self.flipped = 0
        
    def initialDisplay(self):
        print("- `n` | move to next card")
        print("- `b` | move back one card")
        print("- `f` | flip card")
        print("- `exit` | end session")
        print("[ enter to start ]")
        
    def display(self, params):
        print(params['currentCard'][self.flipped])

    def logic(self, params):
        # Example algorithm: Show next flashcard in sequence, unless user inputs 'repeat'
        next_index = params['index']
        if params['user_input'] == 'n':
            next_index = (params['index'] + 1) % len(params['data'])
            self.flipped = 0
        elif params['user_input'] == 'b':
            next_index = (params['index'] - 1) % len(params['data'])
            self.flipped = 0
        elif params['user_input'] == 'f':
            self.flipped = 1-self.flipped
        
        return next_index


class WrittenAlgorithm:
    def __init__(self):
        self.flipped = 0
        
    def initialDisplay(self):
        print("- `n` | move to next card")
        print("- `b` | move back one card")
        print("- `f` | flip card")
        print("- `exit` | end session")
        print("[ enter to start ]")
        
    def display(self, params):
        print(params['currentCard'][self.flipped])

    def logic(self, params):
        # Example algorithm: Show next flashcard in sequence, unless user inputs 'repeat'
        next_index = params['index']
        if params['user_input'] == 'n':
            next_index = (params['index'] + 1) % len(params['data'])
            self.flipped = 0
        elif params['user_input'] == 'b':
            next_index = (params['index'] - 1) % len(params['data'])
            self.flipped = 0
        elif params['user_input'] == 'f':
            self.flipped = 1-self.flipped
        
        return next_index

# Dictionary of algorithms
algorithms = {
    # !!! DONT REMOVE "flashcards" !!!
    # flashcards is the automatic choice when entering the program
    # removing it will permanantly break the program until it is restored
    "flashcards": FlashcardsAlgorithm,
    "written": WrittenAlgorithm
}
