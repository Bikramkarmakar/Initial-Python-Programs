#Take three number from user to compare
x = int(input("Enter 1st integer :"))
y = int(input("Enter 2nd integer :"))
z = int(input("Enter 2nd integer :"))
#Compare both the Number
if x > y and x > z:
    print( x,"is the greatest number.")
elif y > x and y > z: 
    print( y,"is the greatest number.")
else : 
    print( z,"is the greatest number.")