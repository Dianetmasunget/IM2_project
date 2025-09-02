x = (int(input("Enter number: ")))

i = 1

while x % i == 0:
    x //= i
    i += 1

if x == 1:
    print(f"Reverse Factorial is {i-1}")
else:
    print("Not a factorial")