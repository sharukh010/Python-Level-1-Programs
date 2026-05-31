'''
height = 5 

* 
* * 
* * * 
* * * * 
* * * * * 

'''

rows = int(input("Enter the height: "))
cols = 1 

for row in range(1,rows+1):
    for col in range(1,cols+1):
        print("*",end=" ")
    print()
    cols = cols + 1 
