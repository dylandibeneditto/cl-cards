import os
import glob
from termcolor import colored, cprint
from algorithms import algorithms
from load import load_set

# Initialize variables
current_set = "help.set"  # Default set
current_algorithm = "flashcards"  # Default algorithm
current_command = None
currently_running = False
current_index = 0
flashcards_data = load_set(current_set)  # Load the initial set of flashcards
current_algorithm_instance = algorithms[current_algorithm]()  # Instantiate the default algorithm

def header():
    """
    Display the header information based on the current state.
    """
    global current_command, current_set, current_algorithm, current_index, currently_running
    header_str = f' ${current_command}' if current_command else f'{current_set} > {current_algorithm}'
    if currently_running:
        header_str = f"{current_set} | {current_index + 1} / {len(flashcards_data)}"
    
    cprint(header_str.center(os.get_terminal_size().columns), 'cyan')
    
    # Display progress bar
    if currently_running:
        total_width = os.get_terminal_size().columns - 2
        progress_width = int((total_width / len(flashcards_data)) * (current_index + 1))
        progress_bar = "[" + "-" * progress_width + " " * (total_width - progress_width) + "]"
        cprint(progress_bar, 'green')

def run():
    """
    Main loop for running the current algorithm on the flashcards.
    """
    global current_index, currently_running
    user_input = ""
    clear()
    params = {
        'index': current_index,
        'data': flashcards_data,
        'currentCard': flashcards_data[current_index],
        'user_input': user_input
    }
    
    current_algorithm_instance.initialDisplay(params)  # Display initial message for the algorithm
    clear()
    current_algorithm_instance.display(params)
    
    while user_input != "exit":
        user_input = input()
        params['user_input'] = user_input
        current_index = current_algorithm_instance.logic(params)  # Get next index based on user input
        clear()
        params['index'] = current_index
        params['currentCard'] = flashcards_data[current_index]
        current_algorithm_instance.display(params)  # Display the current flashcard
    
    currently_running = False

def clear():
    """
    Clear the terminal screen and display the header.
    """
    os.system('cls' if os.name == "nt" else "clear")
    header()

def change_set(new_set):
    """
    Change the current set of flashcards.
    """
    global current_set, flashcards_data, current_index
    if not new_set.endswith(".set"):
        new_set += ".set"
    files = glob.glob("./*.set")
    files = [file[2:] for file in files]
    if new_set in files:
        current_set = new_set
        flashcards_data = load_set(new_set)  # Load the new set of flashcards
        current_index = 0  # Reset the current index
    else:
        cprint(f"Set '{new_set}' not found.", 'red')

def change_algorithm(new_algorithm):
    """
    Change the current algorithm.
    """
    global current_algorithm, current_algorithm_instance
    if new_algorithm in algorithms:
        current_algorithm_instance = algorithms[new_algorithm]()  # Instantiate the new algorithm
        current_algorithm = new_algorithm
    else:
        cprint(f"Algorithm '{new_algorithm}' not found.", 'red')

def main():
    """
    Main loop for handling user commands.
    """
    global current_command, currently_running
    while True:
        cmd = input(colored("> ", 'yellow'))
        current_command = cmd
        clear()

        if cmd == "help":
            help_text = (
                "\ncset: change set\n\tChange your working set to any '.set' file in the app directory"
                "\ncalg: change algorithm\n\tChange your working algorithm to any algorithm in the 'algorithm.py' file"
                "\nrun: start running the flashcards\n\tStart the study session based on your working algorithm and set"
                "\nlist: lists all cards\n\tList every parsed card from using the 'load.py' file\n"
            )
            cprint(help_text, 'blue')
        elif cmd == "cset":
            files = glob.glob("./*.set")
            files = [file[2:] for file in files]
            if files:
                cprint("\n".join(files), 'green')
                new_set = input(colored("?: ", 'yellow'))
                change_set(new_set)
            else:
                cprint("You don't have any other sets", 'red')
        elif cmd == "calg":
            if len(algorithms) > 1:
                cprint("\n".join(algorithms), 'green')
                new_algorithm = input(colored("?: ", 'yellow'))
                change_algorithm(new_algorithm)
            else:
                cprint("You don't have any other algorithms", 'red')
        elif cmd == "run":
            currently_running = True
            run()
        elif cmd == "list":
            # List all flashcards in the current set
            for card in flashcards_data:
                cprint(f"\nfront: {card[0]}", 'yellow')
                cprint(f"back: {card[1]}", 'yellow')
            print("")
        else:
            cprint(f"Unknown command: {cmd}", 'red')

        current_command = None
        input(colored("[ enter ]", 'yellow'))
        clear()

clear()
main()
