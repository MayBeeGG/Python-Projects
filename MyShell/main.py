import pyfiglet
import random
from Module import *
import subprocess
# import readline

possible_fonts = ["slant","epic","doom","speed"]
module=""
command_dict = {
    "load": "Commands/load.py",
}
module_list = ["portscan"]

# Colors for Console Output
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'


# readline.set_completer(function_completer)
# readline.parse_and_bind("tab: complete")


def default_line(module:str)->str:
    if module == "":
        return f"{GREEN} ${BLUE}>{RESET}"
    else:
        return f"{RED}"+module+f"{GREEN}${BLUE}>{RESET}"



if __name__ == "__main__":
    pyfiglet.print_figlet("MYSHELL \n", font=possible_fonts[random.randint(0, 3)])
    while True:
        user_input = input(default_line(module))
        if user_input.lower() in ["exit"]:
            if module != "":
                module = ""
                continue
            print("Goodbye!")
            break
        elif user_input == "":
            continue
        else:
            if module == "":
                try:
                    user_input_split = user_input.split(" ")
                    choosen_command = user_input_split[0]
                    if choosen_command in command_dict.keys():
                        try:
                            choosen_module = user_input_split[1]
                            if choosen_module in module_list:
                                module = choosen_module
                                print(f"Module {module} loaded")
                                subprocess.run(["python", f"./MOdule/{module}.py"])
                            else:
                                print("Unknown module")
                                continue
                        except IndexError:
                            print("Unknown command")
                            continue
                            
                    else:
                        print("Unknown command")
                        continue

                except Exception as e:
                    print("Error processing input")
                    continue
            else:
                print("Error processing input")
