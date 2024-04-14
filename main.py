from src.interpreter import Interpreter
import src.logs as logs
from src.repl import repl
import sys
import os

def run(file):
    if not os.path.exists(file):
        logs.runError(f"file '{file}' not found")
        return

    with open(file, 'r') as f:
        code = f.read()
        interpreter = Interpreter(code)
        print(interpreter.run())

def main():
    args = sys.argv[1:]
    if args == []:
        repl()
    elif len(args) > 1:
        logs.runError("too many arguments")
    elif args[0] == "repl":
        repl()
    elif args[0] == "--help" or args[0] == "-h":
        logs.help()
    elif args[0] == "--version" or args[0] == "-v":
        logs.version()
    elif args[0] == "--info" or args[0] == "-i":
        logs.info()
    else:
        run(args[0])

if __name__ == '__main__':
    main()