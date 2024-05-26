import os
import glob
from algorithms import algorithms
from load import load_set

# Initialize variables
currentSet = "help.set"  # Default set
currentAlg = "flashcards"  # Default algorithm
currentCmd = None
currentlyRunning = False
currentIndex = 0
flashcardsData = load_set(currentSet)  # Load the initial set of flashcards
currentAlgorithmInstance = algorithms[currentAlg]()  # Instantiate the default algorithm

def header():
    """
    Display the header information based on the current state.
    """
    global currentCmd, currentSet, currentAlg, currentIndex, currentlyRunning
    header_str = f'{f" ${currentCmd}" if currentCmd else f""}'
    if currentlyRunning:
        header_str = f"{currentSet} | {currentIndex+1} / {len(flashcardsData)}"
    elif currentCmd:
        header_str = f" ${currentCmd}"
    else:
        header_str = f"{currentSet} > {currentAlg}"
    print(header_str.center(os.get_terminal_size().columns))

def run():
    """
    Main loop for running the current algorithm on the flashcards.
    """
    global currentIndex, currentlyRunning
    user_input = ""
    clear()
    params = {
        'index': currentIndex,
        'data': flashcardsData,
        'currentCard': flashcardsData[currentIndex],
        'user_input': user_input
    }
    currentAlgorithmInstance.initialDisplay(params)  # Display initial message for the algorithm
    clear()
    currentAlgorithmInstance.display(params)
    while(user_input != "exit"):
        user_input = input()
        params = {
            'index': currentIndex,
            'data': flashcardsData,
            'currentCard': flashcardsData[currentIndex],
            'user_input': user_input
        }
        currentIndex = currentAlgorithmInstance.logic(params)  # Get next index based on user input
        clear()
        paramsD = {
            'index': currentIndex,
            'data': flashcardsData,
            'currentCard': flashcardsData[currentIndex],
            'user_input': user_input
        }
        currentAlgorithmInstance.display(paramsD)  # Display the current flashcard
    currentlyRunning = False

def clear():
    """
    Clear the terminal screen and display the header.
    """
    os.system('cls' if os.name == "nt" else "clear")
    header()

def cset(newSet):
    """
    Change the current set of flashcards.
    """
    global currentSet, flashcardsData, currentIndex
    if not newSet.endswith(".set"):
        newSet += ".set"
    currentSet = newSet
    flashcardsData = load_set(newSet)  # Load the new set of flashcards
    currentIndex = 0  # Reset the current index

def calg(newAlg):
    """
    Change the current algorithm.
    """
    global currentAlg, currentAlgorithmInstance
    if newAlg in algorithms:
        currentAlgorithmInstance = algorithms[newAlg]()  # Instantiate the new algorithm
        currentAlg = newAlg
    else:
        print(f"Algorithm '{newAlg}' not found.")

def main():
    """
    Main loop for handling user commands.
    """
    global currentCmd, currentlyRunning
    while True:
        cmd = input("> ")
        currentCmd = cmd
        clear()

        if cmd == "help":
            print("\ncset: change set\n\tleads to a menu in order to change your working set to any '.set' file in the app directory\n\ncalg: change algorithm\n\tleads to a menu in order to change your working algorithm to any algorithm in the 'algorithm.py' file\n\nrun: start running the flashcards\n\tstarts the study session based on your working algorithm and set\n\nlist: lists all cards\n\tlists every parsed card from using the 'load.py' file\n")
        elif cmd == "cset":
            files = glob.glob("./*.set")
            print("\n".join(files) if files else "You don't have any other sets")
            if files:
                newSet = input("?: ")
                cset(newSet)
        elif cmd == "calg":
            print("\n".join(algorithms) if len(algorithms) > 1 else "You don't have any other algorithms")
            if len(algorithms) > 1:
                newAlg = input("?: ")
                calg(newAlg)
        elif cmd == "run":
            currentlyRunning = True
            run()
        elif cmd == "list":
            # List all flashcards in the current set
            for card in flashcardsData:
                print(f"\nfront: {card[0]}")
                print(f"back: {card[1]}")
            print("")
        else:
            print(f"Unknown command: {cmd}")

        currentCmd = None
        input("[ enter ]")
        clear()

clear()
main()
