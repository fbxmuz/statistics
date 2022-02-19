def factorial(n):
    if n == 1:
        return n
    else:
        factorial(n) * factorial(n-1)


print(factorial(5))
