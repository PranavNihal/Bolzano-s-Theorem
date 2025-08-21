import sympy as sm
from sympy import Float
# we use Abs from sympy as the datatype given by the output of .subs is not in the normal python libraries
fun = input("Please input the Continuous function: ")
x = sm.Symbol("x")
func = sm.simplify(fun)
# Starting Bolzano Theorem Evaluation uses Binary Search
# The following
a = float(input("Please input lower limit[a]: "))
b = float(input("Please input upper limit[b]: "))
def solver(low, high, acc):
    global mid
    ite = 0
    target = 0
    while abs(high  - low) > acc:
        ite+=1
        mid = (low + high) / 2.0
        f_mid = Float(func.subs(x, mid)).evalf()
        if abs(f_mid - target) < acc:
            return mid
        elif f_mid - target > acc:
            high = mid
        else:
            low = mid
    print("The number of iterations are:" + str(ite))
    return (low + high) / 2.0
root = solver(a,b, 1e-5)
print(root)
