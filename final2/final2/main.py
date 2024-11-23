# alter_main.py
from lexer import lexer
from my_parser import parse
from interpret import interpret


def main(file_path):
    env = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.lower() == 'exit':
                print("Exiting...")
                break
            tokens = lexer(line)
            print("Tokens:", tokens)  # Debug print to show the tokens
            parse_tree = parse(tokens)
            print("Parse Tree:", parse_tree)  # Debug print to show the parse tree
            result = interpret(parse_tree, env)
            print("Result:", result)


if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    main(file_path)

