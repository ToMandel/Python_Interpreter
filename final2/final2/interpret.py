from language_specifications import MAX_RESULT_DIGITS, MAX_VARIABLES


# Function to handle overflow by truncating the result to the maximum allowed digits
def handle_overflow(result):
    if len(result) > MAX_RESULT_DIGITS:
        print("Warning: Result exceeds maximum allowed digits. Truncating result...")
        result = result[:MAX_RESULT_DIGITS]
    return result

# Function to handle overflow by printing an error message and returning a flag to indicate overflow
def handle_variable_overflow(env):
    if len(env) >= MAX_VARIABLES:
        print("Error: Maximum number of variables exceeded.")
        return False  # Return a flag to indicate an overflow
    return True  # Return a normal value to indicate no overflow

def interpret(parse_tree, env={}):
    if isinstance(parse_tree, tuple):
        operator, *operands = parse_tree
        if operator == 'declare':
            if not handle_variable_overflow(env):  # Check overflow before declaring a new variable
                return None  # Skip this declaration if there's an overflow
            var_name, value_expression = operands
            value = interpret(value_expression, env)
            env[var_name] = value
            return value  # Ensure a value is returned
        elif operator == 'set':
            var_name, value_expression = operands
            if var_name in env:
                value = interpret(value_expression, env)
                env[var_name] = value
                return value  # Ensure a value is returned
            else:
                raise NameError(f"Variable '{var_name}' not declared.")
        elif operator in ['+', '-', '*', '/']:
            operand1, operand2 = operands
            val1 = interpret(operand1, env)
            val2 = interpret(operand2, env)
            # Perform the operation and handle overflow
            result = handle_overflow(str(val1 + val2)) if operator == '+' else \
                     handle_overflow(str(val1 - val2)) if operator == '-' else \
                     handle_overflow(str(val1 * val2)) if operator == '*' else \
                     handle_overflow(str(val1 // val2)) if operator == '/' else None
            return int(result)  # Convert result back to integer after overflow handling
        elif operator in ['<', '>', '=']:
            operand1, operand2 = operands
            val1 = interpret(operand1, env)
            val2 = interpret(operand2, env)
            # Compare and return 1 or 0 as true/false
            if operator == '<': return 1 if val1 < val2 else 0
            elif operator == '>': return 1 if val1 > val2 else 0
            elif operator == '=': return 1 if val1 == val2 else 0
        elif operator == 'if':
            condition, true_branch, false_branch = operands
            condition_result = interpret(condition, env)
            # Depending on the condition, interpret the corresponding branch
            return interpret(true_branch, env) if condition_result != 0 else interpret(false_branch, env)
        elif operator == 'while':
            condition, true_branch, false_branch = operands
            condition_result = interpret(condition, env)
            while condition_result != 0:
                interpret(true_branch, env)
                condition_result = interpret(condition, env)
            return interpret(false_branch, env)  # Execute the false branch when the condition is no longer true

    elif isinstance(parse_tree, str):
        if parse_tree.isdigit():
            return int(parse_tree)  # Return the integer value
        elif parse_tree in env:
            return env[parse_tree]  # Return the variable's value from env
        else:
            raise NameError(f"Variable '{parse_tree}' not declared.")
    else:
        raise RuntimeError("Invalid parse tree node: " + str(parse_tree))
