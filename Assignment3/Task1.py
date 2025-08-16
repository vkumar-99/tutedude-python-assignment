def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

inputNum = input('Enter the number:')
result  = factorial(int(inputNum))
print('Factorial of',inputNum,'is:', result)