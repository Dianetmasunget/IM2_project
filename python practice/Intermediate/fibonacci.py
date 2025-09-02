x = (int(input("Enter number: ")))

a ,b = 0,1

print("Fibonacci Sequence: ")

for i in range(x):
    print(a,end=" ")
    a,b=b,a+b