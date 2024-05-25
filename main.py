import os
import glob
from algorithms import a

currentSet = "main.set"
currentAlg = "flashcards"
currentCmd = None

def header():
    global currentCmd, currentSet, currentAlg
    print(f'{f" ${currentCmd}" if currentCmd else f"{currentSet} > {currentAlg}"}'.center(os.get_terminal_size().columns))
    a[currentAlg]("hello")

def clear():
    os.system('cls' if os.name == "nt" else "clear")
    header()

def cset(newSet):
    global currentSet
    if newSet.endswith(".set") == False:
        newSet += ".set"
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
            files = glob.glob("./*.set")
            print("\n".join(files) if len(files)>0 else "You don't have any sets")
            if len(files)>0:
                newSet = input("?: ")
                cset(newSet)
        elif cmd == "calg":
            newAlg = input("?: ")
            calg(newAlg)
        else:
            print("unknown command:", cmd)
        
        currentCmd = None
        input("[ enter ]")
        clear()

clear()
main()
