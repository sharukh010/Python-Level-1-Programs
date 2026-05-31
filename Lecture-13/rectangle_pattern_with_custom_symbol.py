rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))
symbol = input("Enter the desired symbol: ")

for row in range(1, rows+1):
    for col in range(1, cols+1):
        print(symbol, end=" ")
    print()
