from colorama import Fore
import sys

usage = "Usage: python main.py [filename]"

def runError(message):
    print(f"{Fore.RED}error: {Fore.RESET}{message}")
    print(f"\n{usage}")
    print("\nFor more information, try 'python main.py --help'\n")
    
    sys.exit(1)

def runtimeError(message, errorType):
    print(f"{Fore.RED}{errorType} error: {Fore.RESET}{message}")
    sys.exit(1)

def runWarning(message):
    print(f"{Fore.YELLOW}warning: {Fore.RESET}{message}")

def help():
    print(usage)
    print("\nOptions:")
    print("  --help, -h\tdisplay this help message")
    print("  --version, -v\tdisplay the version")
    print("  --info, -i\tdisplay information about the interpreter")
    print("\nArguments:")
    print("  filename\tthe file to run")
    print("  repl\trun the REPL")
    print("\nExample:")
    print("  python main.py script.bf")

def info():
    print("brainfk compiler is an attempt to create a compiler for the brainf\*\*k programming language. This project is created to learn more about compilers and how they work. The project is written in Python and does not use any external libraries (other than the standard library and colors).\n")

def version(color=Fore.RESET):
    try:
        version = None
        with open("version.txt", 'r') as f:
            version = f.read()
        print(f"{color}brainfk-compiler v{version}{Fore.RESET}")
    except:
        runError("could not find version.txt")