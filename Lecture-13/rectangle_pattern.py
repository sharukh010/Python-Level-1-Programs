'''
row = 5 
col = 3 

* * * 
* * * 
* * * 
* * * 
* * * 

'''

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: ")) 
for row in range(1,rows+1):
    for col in range(1,cols+1):
        print("*",end=" ")
    print()
