x = (int(input("Enter number: ")))

sum_digits = 0

num = abs(x)

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print(sum_digits)