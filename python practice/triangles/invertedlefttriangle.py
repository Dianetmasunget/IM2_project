rows = int(input("Enter number of rows: "))

for i in range(rows,0,-1):
    print(" " * (rows - i)+ "*" * i)