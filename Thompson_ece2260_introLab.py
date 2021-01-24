import math
import cmath

def calculate_roots(coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    #Determine whether we need roots to be complex or not
    if ((b**2-4*a*c) < 0):
        #If discriminant is negative
        r1 = (-b + cmath.sqrt(b**2-4*a*c)) / (2*a)
        r2 = (-b - cmath.sqrt(b**2-4*a*c)) / (2*a)

    else:
        #If discriminant is 0 or positive
        r1 = (-b + math.sqrt(b**2-4*a*c)) / (2*a)
        r2 = (-b - math.sqrt(b**2-4*a*c)) / (2*a)
    
    return (r1, r2)
    

def compute_factorial(n):
    foo = 1
    for i in range(1, n+1):
        foo *= i
    return foo
    

def sum_factorial(n):
    foo=0
    for i in range (1, n+1):
        foo += compute_factorial(i)
    return foo

def f(x):
    return math.exp(-3 * x) * math.cos(math.pi * x) 
    
      
def left_riemann(delta_x, lb, ub):
    foo = int((ub - lb) / (delta_x))
    sum=0
    for i in range(0, foo+1):
        sum+=f(lb + i*delta_x ) * delta_x

    return sum
    

def right_riemann(delta_x, lb, ub):
    foo = int((ub - lb) / (delta_x))
    sum=0
    for i in range(1, foo):
        sum+=f(lb + i*delta_x) * delta_x

    return sum
    

def midpoint_riemann(delta_x, lb, ub):
    foo = int((ub - lb) / (delta_x))
    sum=0
    for i in range(1, foo):
        sum+=f(lb + i*delta_x - delta_x / 2) * delta_x

    return sum
  
def trap_riemann(delta_x, lb, ub):
    # As by the proof, we discussed, the integral as expressed an an integral is just an average between the right hand and left hand integrals
    return (right_riemann(delta_x, lb, ub) + left_riemann(delta_x, lb, ub)) / 2

   
def main():

    ##############################################################
    # Part 1
    ##############################################################
    print("Part 1 Results")
    
    coef = [2, 4, 0]
    roots = calculate_roots(coef)
    print("roots 1:")
    print(roots)

    coef = [1, 4, 4]
    roots = calculate_roots(coef)
    print("roots 2:")
    print(roots)
    
    coef = [1, 0, 9]
    roots = calculate_roots(coef)
    print("roots 3:")
    print(roots)

    coef = [2, 8, 26]
    roots = calculate_roots(coef)
    print("roots 4:")
    print(roots)

    ##############################################################
    # Part 2
    ##############################################################
    print("\n")
    print("Part 2 Results")
    
    for n in [4, 10, 16]:
        output_factorial = compute_factorial(n)
        print("computed factorial for n=%i is: %i" %
              (n, output_factorial))

    ##############################################################
    # Part 3
    ##############################################################
    print("\n")
    print("Part 3 Results")
    
    for n in [3, 5, 6]:
        output_summation = sum_factorial(n)
        print("computed factorial summation for n=%i is: %i" %
              (n, output_summation))
        
    ##############################################################
    # Part 4
    ##############################################################
    print("\n")
    print("Part 4 Results")
    
    lb = 0
    ub = 10
    
    print("calculating left Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.001]:
        summation = left_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating right Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = right_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating midpoint Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = midpoint_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating trapezoid Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = trap_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

        
if __name__ == "__main__":
    main()
