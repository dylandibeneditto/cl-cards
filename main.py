import os

currentSet = "main.set"
currentAlg = "flashcard"
currentCmd = None

def header():
    global currentCmd, currentSet, currentAlg
    print(f'{f" ${currentCmd}" if currentCmd else f"{currentSet} > {currentAlg}"}'.center(os.get_terminal_size().columns))

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    header()

def cset(newSet):
    global currentSet
    currentSet = newSet

def calg(newAlg):
    global currentAlg
    currentAlg = newAlg

def main():
    global currentCmd
    while True:
        cmd = input("> ")
        currentCmd = cmd
        clear()

        if cmd=="help":
            print("cset: change set\ncalg: change algorithm")

        elif cmd == "cset":
            newSet = input("Enter new set: ")
            cset(newSet)
        elif cmd == "calg":
            newAlg = input("Enter new algorithm: ")
            calg(newAlg)
        else:
            print("unknown command:", cmd)
        
        currentCmd = None
        input("[ enter ]")
        clear()

clear()
main()
