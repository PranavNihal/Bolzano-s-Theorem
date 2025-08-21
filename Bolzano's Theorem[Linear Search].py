import sympy as sm
from sympy import Abs


# we use Abs from sympy as the datatype given by the output of .subs is not in the normal python libraries
fun = input("Please input the Continuous function: ")
x = sm.Symbol("x")
func = sm.simplify(fun)
# Starting Bolzano Theorem Evaluation
# Set for mainly positive roots [for now]func = sm.simplify(fun)
a = float(input("Please input lower limit[a]: "))
b = float(input("Please input upper limit[b]: "))
acc = float(input("Please input accuracy: "))
step = float (( abs(a-b) / acc ))
if((func.subs(x, a).evalf() * (func.subs(x, b).evalf()) < 0)):
    print("The function does not necassarily guarantee the existence of the root ")
else:
    print(step)
approximation = 0
accarr = []
while a < b:
    n = 0.0
    accarr.append(a + (n * step))
    n += 1
    a += step
i = 0
j = len(accarr) - 1
# print(accarr) to print the value in the array
min_val = float("inf")
while i <= j:
    bolz_result = func.subs(x, accarr[i]).evalf()
    if Abs(bolz_result) < min_val:
        min_val = Abs(bolz_result)
        approximation = accarr[i]
    i += 1

print("The Approximation using Bolzano's Theorem is: " + str(approximation))








