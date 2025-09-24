import pyfiglet
import random
# import readline
# from autocomplete import function_completer

possible_fonts = ["slant","epic","doom","speed"]
path=""

# Colors for Console Output
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'


# readline.set_completer(function_completer)
# readline.parse_and_bind("tab: complete")


def default_line(path:str)->str:
    return f"{RED}"+path+f"{GREEN} ${BLUE}>{RESET}"

if __name__ == "__main__":
    pyfiglet.print_figlet("MYSHELL \n", font=possible_fonts[random.randint(0, 3)])
    while True:
        user_input = input(default_line(path))
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting. Goodbye!")
            break
        else:
            # Logic here
            print(f"Command received: {user_input}")

