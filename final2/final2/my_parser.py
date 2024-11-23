# my_parser.py

# my_parser.py


def parse_expression(tokens):
    token_type, token_value = tokens.pop(0)
    if token_type == 'LPAREN':
        operator = tokens.pop(0)[1]
        operands = []
        while tokens[0][1] != ')':
            operands.append(parse_expression(tokens))
        tokens.pop(0)  # Consume the closing parenthesis
        return (operator, *operands)
    elif token_type in ['INTEGER', 'VAR_NAME']:
        return token_value
    else:
        raise SyntaxError("Invalid expression")


def parse(tokens):
    expressions = []
    while tokens:
        expressions.append(parse_expression(tokens))
    return expressions if len(expressions) > 1 else expressions[0]
