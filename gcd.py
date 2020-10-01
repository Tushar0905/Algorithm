
def computeGCD(x, y):

   while(y):
       x, y = y, x % y

   return x

print("Enter value of a: ")
a = input()
print("Enter value of b: ")
b= input()

# prints 12
print ("The gcd of a and b is : ")
print (computeGCD(a,b))
