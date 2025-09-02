x = (int(input("Enter first number: ")))
y = (int(input("Enter second number: ")))

ope = (str(input("Choose operation(+),(-),(x),(/): ")))
if ope == "+":
    final = x + y
    print(f"First number is {x}")
    print(f"Second number is {y}")
    print(f"Sum = {final}")

elif ope == "-":
    final = x - y
    print(f"First number is {x}")
    print(f"Second number is {y}")
    print(f"Difference = {final}")

elif ope == "x":
    final = x*y
    print(f"First number is {x}")
    print(f"Second number is {y}")
    print(f"Product = {final}")

elif ope == "/":
    final = x/y
    print(f"First number is {x}")
    print(f"Second number is {y}")
    print(f"Quotient = {final}")