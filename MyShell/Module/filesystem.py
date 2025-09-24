import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

sys.path.pop(0)


command_list = ["ls","cd","cat","exit","rm","touch","mkdir","rmdir","pwd"]


# Colors for Console Output
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

path = os.getcwd()

# readline.set_completer(function_completer)
# readline.parse_and_bind("tab: complete")

#! Add autocomplete for files


def default_line(path:str)->str:
        return f"{RED}filesystem{RESET} "+path+f"{GREEN}${BLUE}>{RESET}"



if __name__ == "__main__":
    while True:
        user_input = input(default_line(path))
        if user_input.lower() in ["exit"]:
            print("Exiting filesystem Module!")
            break
        elif user_input == "":
            continue
        else:
            try:
                # Actual Logic
                pass
            except:
                print("Error processing input")
                continue

