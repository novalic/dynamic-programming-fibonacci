import functools
import timeit


def fibonacci_recursive(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


def fibonacci_dynamic_programming_aux(num, table):
    if table[num] >= 0:
        return table[num]

    if num == 0 or num == 1:
        res = num
    else:
        res = fibonacci_dynamic_programming_aux(num - 1, table) + fibonacci_dynamic_programming_aux(num - 2, table)

    table[num] = res

    return res


def fibonacci_dynamic_programming(num):
    table = [-1] * (num + 1)
    return fibonacci_dynamic_programming_aux(num, table)


number = int(input('Enter a number: '))


recursive_timer = timeit.Timer(functools.partial(fibonacci_recursive, number))
recursive_time = recursive_timer.timeit(1)
print(f'Calculating Fibonacci of {number} recursively took {recursive_time} seconds.')

dp_timer = timeit.Timer(functools.partial(fibonacci_dynamic_programming, number))
dp_time = dp_timer.timeit(1)
print(f'Calculating Fibonacci of {number} with dynamic programming took {dp_time} seconds.')



