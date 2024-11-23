import re


def lexer(input_string):
    token_patterns = [
        (r'\(', 'LPAREN'),
        (r'\)', 'RPAREN'),
        (r'\+', 'PLUS'),
        (r'-', 'MINUS'),
        (r'\*', 'MULTIPLY'),
        (r'/', 'DIVIDE'),
        (r'declare', 'DECLARE'),
        (r'set', 'SET'),
        (r'if', 'IF'),
        (r'while', 'WHILE'),
        (r'loop', 'LOOP'),
        (r'[0-9]+', 'INTEGER'),
        (r'[a-zA-Z][a-zA-Z0-9_]*', 'VAR_NAME'),
        (r'declare', 'DECLARE'),
        (r'set', 'SET'),
        (r'<', 'LESS_THAN'),
        (r'>', 'GREATER_THAN'),
        (r'=', 'EQUALS'),

    ]
    # Use non-capturing groups for the regex parts and separate group names from the patterns.
    token_regex = '|'.join('(?:%s)' % pattern for (pattern, _) in token_patterns)
    tokens = []
    for match in re.finditer(token_regex, input_string):
        token_type = None
        # Find which token type this match belongs to
        for pattern, type_name in token_patterns:
            if re.match(pattern, match.group(0)):
                token_type = type_name
                break
        token_value = match.group(0)
        tokens.append((token_type, token_value))
    return tokens
