'''
Enter a number: 4 

* * * * 
* * * * 
* * * * 
* * * * 

Enter a number: 6 

* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
'''

# how to print a line of n stars 
n = int(input("Enter the number: "))
for row in range(1,n+1):
    for col in range(1,n+1):
        print("*",end=" ")
    print()
