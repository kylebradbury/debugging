def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        fact = 1
        for i in range(n):
            fact *= i
        return fact

num = 4
print(f"{num}! = {factorial(num)}")