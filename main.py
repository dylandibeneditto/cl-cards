import os
import glob
from algorithms import algorithms
from load import load_set

currentSet = "main.set"
currentAlg = "flashcards"
currentCmd = None
currentlyRunning = False
currentIndex = 0
flashcardsData = load_set(currentSet)
currentAlgorithmInstance = algorithms[currentAlg]()

def header():
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
    global currentIndex, currentlyRunning
    user_input = ""
    clear()
    currentAlgorithmInstance.initialDisplay()
    while(user_input != "exit"):
        user_input = input()
        clear()
        params = {
            'index': currentIndex,
            'data': flashcardsData,
            'currentCard': flashcardsData[currentIndex],
            'user_input': user_input
        }
        currentIndex = currentAlgorithmInstance.logic(params)
        currentAlgorithmInstance.display(params)
    currentlyRunning = False

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    header()

def cset(newSet):
    global currentSet, flashcardsData, currentIndex
    if not newSet.endswith(".set"):
        newSet += ".set"
    currentSet = newSet
    flashcardsData = load_set(newSet)
    currentIndex = 0

def calg(newAlg):
    global currentAlg, currentAlgorithmInstance
    if newAlg in algorithms:
        currentAlgorithmInstance = algorithms[newAlg]()
        currentAlg = newAlg
    else:
        print(f"Algorithm '{newAlg}' not found.")

def main():
    global currentCmd, currentlyRunning
    while True:
        cmd = input("> ")
        currentCmd = cmd
        clear()

        if cmd == "help":
            print("cset: change set\ncalg: change algorithm\nrun: start running the flashcards")

        elif cmd == "cset":
            files = glob.glob("./*.set")
            print("\n".join(files) if files else "You don't have any sets")
            if files:
                newSet = input("Enter new set: ")
                cset(newSet)
        elif cmd == "calg":
            newAlg = input("Enter new algorithm: ")
            calg(newAlg)
        elif cmd == "run":
            currentlyRunning = True
            run()
        else:
            print(f"Unknown command: {cmd}")

        currentCmd = None
        input("[ enter ]")
        clear()

clear()
main()
