# ModuLearn

ModuLearn is an open-source app based in python focused on efficient learning. Develop your own algorithms to speed up learning or use other algorithms created by the community.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Creating Custom Algorithms](#creating-custom-algorithms)
- [Available Commands](#available-commands)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Modular Design**: Easily add or modify algorithms to fit your study needs.
- **Offline**: No need for internet or trusting your study sets to cloud databases.
- **Customizable**: Play around with the source code until the application completely suits your needs.

## Installation

To install the Flashcards Study App, clone the repository and install the required dependencies:

```bash
git clone https://github.com/dylandibeneditto/ModuLearn.git
cd ModuLearn
```

## Usage

To start using the Flashcards Study App, run the main script:

```bash
python main.py
```

### Available Commands

- `help`: Displays a list of available commands.
- `cset`: Change the current flashcard set.
- `calg`: Change the current algorithm.
- `run`: Start the study session.
- `list`: List all flashcards in the current set.
- `exit`: End the current session.

## Creating Custom Algorithms

You can create your own algorithms to customize how you study. Follow the boilerplate structure provided below:

```python
class Algorithm:
    def __init__(self):
        # State variables go here
        pass
    
    def initialDisplay(self, params):
        print("- `exit` | end session")
        print("[ enter to start ]")
        
    def display(self, params):
        # Display the front of the current card
        print(params["currentCard"][0])
        
    def logic(self, params):
        next_index = 0
        # Logic to determine the next index
        return next_index
```

### Example Algorithm

Here is an example of a custom algorithm:

```python
class FlashcardsAlgorithm:
    def __init__(self):
        self.flipped = 0  # State variable to track if the card is flipped
    
    def initialDisplay(self, params):
        print("- `n` | move to next card")
        print("- `b` | move back one card")
        print("- `f` | flip card")
        input("- `exit` | ends the session\n[ enter to start ]")
        
    def display(self, params):
        print(params['currentCard'][self.flipped])

    def logic(self, params):
        next_index = params['index']
        if params['user_input'] == 'n':
            next_index = (params['index'] + 1) % len(params['data'])
            self.flipped = 0
        elif params['user_input'] == 'b':
            next_index = (params['index'] - 1) % len(params['data'])
            self.flipped = 0
        elif params['user_input'] == 'f':
            self.flipped = 1 - self.flipped
        return next_index
```

Add your custom algorithm to the `algorithms` dictionary in the main script:

```python
algorithms = {
    "flashcards": FlashcardsAlgorithm,
    "written": WrittenAlgorithm,
    "your_algorithm_name": YourAlgorithmClass
}
```

## Contributing

We welcome contributions! If you have ideas for new features or improvements, feel free to submit a pull request. Please follow the guidelines in the [CONTRIBUTIONS](./CONTRIBUTIONS.md) file.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for details.

---

Enjoy your studies and happy learning