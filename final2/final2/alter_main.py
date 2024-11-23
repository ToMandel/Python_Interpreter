# alter_main.py
from lexer import lexer
from my_parser import parse
from interpret import interpret


def main():
    env = {}
    while True:
        try:
            input_string = input("Enter an expression (or type 'exit' to quit): ")
            if input_string.lower() == 'exit':
                print("Exiting...")
                break
            tokens = lexer(input_string)
            print("Tokens:", tokens)  # Debug print to show the tokens
            parse_tree = parse(tokens)
            print("Parse Tree:", parse_tree)  # Debug print to show the parse tree
            result = interpret(parse_tree, env)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
