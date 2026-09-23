# 1. Count Letters and Digits

value = input()

letters = 0
digits = 0

for i in value:
    if i.isalpha():
        letters = letters + 1
    elif i.isdigit():
        digits = digits + 1

print("Letters:", letters)
print("digits:", digits)


# 2. Binary Numbers Divisible by 5

value = input().split(",")

result = []

for i in value:
    number = int(i, 2)

    if number % 5 == 0:
        result.append(i)

print(",".join(result))


# 3. Factorial of a Number

n = int(input())

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)