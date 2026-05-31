n = int(input("Enter the number: "))
symbol = input("Enter the symbol: ")

for row in range(1, n+1):
    for col in range(1, n+1):
        print(symbol, end=" ")
    print()
