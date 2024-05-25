"""
params: dict {
    'index': int,                           # Current index of the flashcard
    'data': list                            # The flashcards data
    'currentCard': {front: str, back: str}  # The current flashcard
    'user_input': str                       # Input from the user
}
"""

class FlashcardsAlgorithm:
    def __init__(self):
        self.flipped = 0
        
    def initialDisplay(self):
        print("- `n` | move to next card")
        print("- `b` | move back one card")
        print("- `f` | flip card")
        print("[ enter to start ]")
        
    def display(self, params):
        print(params['currentCard'][self.flipped])

    def logic(self, params):
        # Example algorithm: Show next flashcard in sequence, unless user inputs 'repeat'
        next_index = params['index']
        if params['user_input'] == 'n':
            next_index = (params['index'] + 1) % len(params['data'])
        elif params['user_input'] == 'b':
            next_index = (params['index'] - 1) % len(params['data'])
        elif params['user_input'] == 'f':
            self.flipped = 1-self.flipped
        return next_index


class WrittenAlgorithm:
    def __init__(self):
        self.state = {}

    def next_index(self, params):
        # Example algorithm: Go to the next flashcard unless user inputs 'repeat'
        if params['user_input'] == 'repeat':
            next_index = params['index']
        else:
            next_index = (params['index'] + 1) % len(params['data'])
        return next_index

# Dictionary of algorithms
algorithms = {
    # !!! DONT REMOVE "flashcards" !!!
    # flashcards is the automatic choice when entering the program
    # removing it will permanantly break the program until it is restored
    "flashcards": FlashcardsAlgorithm,
    "written": WrittenAlgorithm
}
