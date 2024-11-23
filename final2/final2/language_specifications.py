# language_specifications.py

MAX_RESULT_DIGITS = 10
MAX_VARIABLES = 10

BNF_GRAMMAR = """
<expression> ::= <arithmetic_expr> | <variable_declaration> | <variable_assignment> | <conditional_expr> | <loop_expr>

<arithmetic_expr> ::= '(' <operator> <operand> <operand> ')'
<operand> ::= <integer> | <variable_name> | <expression>
<operator> ::= '+' | '-' | '*' | '/'

<variable_declaration> ::= '(' 'declare' <variable_name> <integer> ')'
<variable_assignment> ::= '(' 'set' <variable_name> <integer> ')'

<conditional_expr> ::= '(' 'if' <condition> <true_branch> <false_branch> ')'
<condition> ::= <expression>
<true_branch> ::= <expression>
<false_branch> ::= <expression>

<loop_expr> ::= '(' 'loop' <condition> <body> ')'
<body> ::= <expression>

<integer> ::= [0-9]+
<variable_name> ::= [a-zA-Z][a-zA-Z0-9_]*
"""
