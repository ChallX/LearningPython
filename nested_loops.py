rows = int(input("How Many Rows: "))
columns = int(input("How Many Column: "))
symbol = input("Enter a Symbol To Use: ")


for i in range (rows):
    for j in range(columns):
        print (symbol, end="")
    print()


