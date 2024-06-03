## Solve the quadratic equation ax**2 + bx + c = 0
#
## import complex math module
#import cmath
#
#a = int(input("a:"))
#b = int(input("b:"))
#c = int(input("c:"))
#
## calculate the discriminant
#d = (b**2) - (4*a*c)
#
## find two solutions
#sol1 = (-b-cmath.sqrt(d))/(2*a)
#sol2 = (-b+cmath.sqrt(d))/(2*a)
#
#print('The solution are {0} and {1}'.format(sol1,sol2))
# Python program to find roots of quadratic equation
# import complex math module
# Python program to find roots of quadratic equation
import math 


# function for finding roots
def equationroots( a, b, c): 

    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
    i=0
    # checking condition for discriminant
    if dis > 0: 
        print("real and different roots") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
    
    elif dis == 0: 
        print("real and same roots") 
        print(-b / (2 * a)) 
    
    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- b / (2 * a), + i, sqrt_val / (2 * a)) 
        print(- b / (2 * a), - i, sqrt_val / (2 * a)) 

# Driver Program 
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
# If a is 0, then incorrect equation
if a == 0: 
        print("Input correct quadratic equation") 

else:
    equationroots(a, b, c)