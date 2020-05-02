Fibonacci
==

The simple recursion:

```
fib(0) = 0
fib(1) = 1
fib(n) = fib(n - 1) + fib(n - 2)
```

e.g.:
```
fib(4) = [fib(3)] + [fib(2)] = [fib(2) + fib(1)] + [fib(1) + fib(0)] = [(fib(1) + fib(0)) + 1] + [1 + 0] = 3
```

With this approach we have to repeat a lot of calculations.

With dynamic programming techniques we only calculate each value one time.


Execution use cases
==

```
Calculating Fibonacci of 10 recursively took 2.508100033082883e-05 seconds.
Calculating Fibonacci of 10 with dynamic programming took 7.996000022103544e-06 seconds.
```

```
Calculating Fibonacci of 20 recursively took 0.0030608279998887156 seconds.
Calculating Fibonacci of 20 with dynamic programming took 2.0420000055310084e-05 seconds.
```

```
Calculating Fibonacci of 30 recursively took 0.2475134070000422 seconds.
Calculating Fibonacci of 30 with dynamic programming took 1.4527999610436382e-05 seconds.
```

```
Calculating Fibonacci of 35 recursively took 2.728477938999731 seconds.
Calculating Fibonacci of 35 with dynamic programming took 1.7669000044406857e-05 seconds.
```

```
Calculating Fibonacci of 38 recursively took 11.392906241000219 seconds.
Calculating Fibonacci of 38 with dynamic programming took 1.8928999907075195e-05 seconds.
```

```
Calculating Fibonacci of 40 recursively took 34.496809830000075 seconds.
Calculating Fibonacci of 40 with dynamic programming took 2.2804999844083795e-05 seconds.
```

```
Calculating Fibonacci of 45 recursively took 367.38581775700004 seconds.
Calculating Fibonacci of 45 with dynamic programming took 2.579200008767657e-05 seconds.
```
