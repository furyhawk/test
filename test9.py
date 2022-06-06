import math

def is_fibonacci(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n

def fibs():
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b

n = int(input("please, enter a number "))
for fib in fibs():
  if n == fib:
    print("your number is a Fibonacci number!")
    break
  if fib > n:
    print("your number is not a Fibonacci number!")
    break
