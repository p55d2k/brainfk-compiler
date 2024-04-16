from src.interpreter import Interpreter
from colorama import Fore
from src.logs import version, info

def repl():
    version(color=Fore.GREEN)
    print(Fore.GREEN + "REPL | Type 'exit' to exit the REPL" + Fore.RESET)

    while True:
        code = input(Fore.MAGENTA + ">> " + Fore.RESET)

        if code == "exit":
            break
        if code == "":
            continue
        if code == "clear" or code == "cls":
            print("\033[H\033[J")
            continue
        if code == "info":
            info()
            continue
        if code == "version":
            version()
            continue

        interpreter = Interpreter(code)
        print(interpreter.run())
