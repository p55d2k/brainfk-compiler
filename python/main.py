from src.interpreter import Interpreter
import src.logs as logs
from src.repl import repl
import sys
import os

def run(file, output=None):
    if not os.path.exists(file):
        logs.runError(f"file '{file}' not found")
        return

    with open(file, 'r') as f:
        code = f.read()
        interpreter = Interpreter(code)
        decoded = interpreter.run()
        print(decoded)

        if output:
            with open(output, 'w') as f:
                f.write(decoded)
            print(f"Output written to '{output}'")

def main():
    args = sys.argv[1:]
    if args == []:
        repl()
    elif len(args) > 1:
        if len(args) > 3:
            logs.runError("too many arguments")
        else:
            if args[0] == "--out" or args[0] == "-o":
                run(args[1], args[2])
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