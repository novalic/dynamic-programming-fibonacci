import functools, timeit

def fibo_rec(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo_rec(num - 1) + fibo_rec(num - 2)


def fibonacci_dp(num, table):
   if table[num] >= 0:
       return table[num]

   if (num == 0 or num == 1):
       res = num
   else:
       res = fibonacci_dp(num - 1, table) + fibonacci_dp(num - 2, table)

   table[num] = res

   return res


def fibo_dp(num):
    table = [-1] * (num + 1)
    return fibonacci_dp(num, table)


number = int(input('Enter a number: '))


recursive_timer = timeit.Timer(functools.partial(fibo_rec, number))
recursive_time = recursive_timer.timeit(1)
print(f'Calculating Fibonacci of {number} recursively took {recursive_time} seconds.')

dp_timer = timeit.Timer(functools.partial(fibo_dp, number))
dp_time = dp_timer.timeit(1)
print(f'Calculating Fibonacci of {number} with dynamic programming took {dp_time} seconds.')



