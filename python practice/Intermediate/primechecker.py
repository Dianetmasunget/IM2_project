x = (int(input("Enter number: ")))

if x <= 1:
    print("Input not a prime number.")

else:
    is_prime = True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")