from functools import reduce

# Q9
print("Q9:")
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

# Q10
print("Q10:")
concatenate = lambda lst: '' if not lst else lst[0] + (' ' + concatenate(lst[1:]) if len(lst) > 1 else '')

res = concatenate(['a', 'aa', 'shir'])
print(res)

# Q11
print("Q11:")
cumulative_sums = lambda lists: list(map(
    lambda lst: (lambda sum_squares: sum_squares)(
        reduce(lambda acc, x: acc + (lambda x: x**2)(x),
            filter(lambda x: (lambda x: x % 2 == 0)(x), lst), 0)), lists))

test_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
res = cumulative_sums(test_lists)
print(res)

# Q12
print("Q12:")
nums = [1, 2, 3, 4, 5, 6]
sum_squared = reduce(lambda acc, x: acc + x, map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(sum_squared)

# Q13
print("Q13:")
count_palindromes = lambda lists: list(map(lambda lst: reduce(lambda acc, x: acc + (x == x[::-1]), lst, 0), lists))

test_lists_strings = [["madam", "apple", "kayak", "banana"], ["level", "world", "racecar"], ["hello", "noon", "bye"]]
res = count_palindromes(test_lists_strings)
print(res)


# Q14
print("Q14:")
def generate_values():
    print('Generating values...')
    yield 1
    yield 2
    yield 3


def square(x):
    print(f'Squaring {x}')
    return x * x


print('Eager evaluation:')
values = list(generate_values())
squared_values = [square(x) for x in values]
print(squared_values)
print('\nLazy evaluation:')
squared_values = [square(x) for x in generate_values()]
print(squared_values)
