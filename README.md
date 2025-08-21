# Bolzano's Theorem Root Finder

A Python implementation that finds approximate roots of continuous functions using Bolzano's Theorem (Intermediate Value Theorem) with two different search methods: Linear Search and Binary Search (Bisection Method).

## Overview

This program provides two implementations for finding roots of continuous functions based on Bolzano's Theorem. The theorem states that if a continuous function has opposite signs at two points, then there must be at least one root between those points.

## Dependencies

- **SymPy**: Used for symbolic mathematics, function parsing, and numerical evaluation
  ```bash
  pip install sympy
  ```

## Two Implementation Methods

### Method 1: Linear Search (Grid Search)
A brute-force approach that systematically checks points across the interval.

### Method 2: Binary Search (True Bisection Method)
An efficient approach that uses the bisection method to converge on the root logarithmically.

---

## Method 1: Linear Search Implementation

### How It Works
1. **Function Input**: Takes a continuous function as string input
2. **Interval Definition**: User defines search bounds [a, b]
3. **Grid Generation**: Divides interval into uniform steps based on accuracy
4. **Exhaustive Search**: Evaluates function at all points and finds minimum |f(x)|

### Code Structure
```python
import sympy as sm
from sympy import Abs

fun = input("Please input the Continuous function: ")
x = sm.Symbol("x")
func = sm.simplify(fun)

a = float(input("Please input lower limit[a]: "))
b = float(input("Please input upper limit[b]: "))
acc = float(input("Please input accuracy: "))
step = float((abs(a-b) / acc))

# Generate array of points and find minimum |f(x)|
```

### Algorithm Steps
1. Calculate step size based on interval width and accuracy
2. Generate array of x-values across the interval
3. Evaluate function at each point
4. Find the x-value that produces the result closest to zero

### Characteristics
- **Time Complexity**: O(n) where n = (b-a)/accuracy
- **Space Complexity**: O(n) for storing all points
- **Accuracy**: Depends on step size
- **Guaranteed**: Finds the best approximation within the grid

---

## Method 2: Binary Search (Bisection Method)

### How It Works
1. **Function Input**: Takes a continuous function as string input
2. **Interval Definition**: User defines search bounds [a, b]
3. **Iterative Bisection**: Repeatedly halves the interval containing the root
4. **Convergence**: Continues until interval is smaller than desired accuracy

### Code Structure
```python
import sympy as sm
from sympy import Float

def solver(low, high, acc):
    ite = 0
    target = 0
    while abs(high - low) > acc:
        ite += 1
        mid = (low + high) / 2.0
        f_mid = Float(func.subs(x, mid)).evalf()
        
        if abs(f_mid - target) < acc:
            return mid
        elif f_mid - target > acc:
            high = mid
        else:
            low = mid
    
    return (low + high) / 2.0
```

### Algorithm Steps
1. Find midpoint of current interval
2. Evaluate function at midpoint
3. Determine which half contains the root
4. Replace the appropriate bound with the midpoint
5. Repeat until convergence

### Characteristics
- **Time Complexity**: O(log n) - logarithmic convergence
- **Space Complexity**: O(1) - constant space
- **Accuracy**: Exponentially improving with each iteration
- **Efficiency**: Much faster for high precision requirements

---

## Comparison of Methods

| Aspect | Linear Search | Binary Search |
|--------|---------------|---------------|
| **Speed** | Slow for high accuracy | Very fast |
| **Memory** | High (stores all points) | Low (constant) |
| **Iterations** | Fixed by accuracy | Logarithmic |
| **Precision** | Limited by grid size | Theoretically unlimited |
| **Best Use** | Quick approximations | High precision roots |

## Usage Examples

### Linear Search Method
```
Please input the Continuous function: x**2 - 4
Please input lower limit[a]: 1
Please input upper limit[b]: 3  
Please input accuracy: 0.01
```

### Binary Search Method
```
Please input the Continuous function: x**3 - x - 1
Please input lower limit[a]: 1
Please input upper limit[b]: 2
```
*(Uses fixed accuracy of 1e-5)*

## Limitations

### What These Methods May Not Handle Well
1. **Discontinuous Functions**: Bolzano's Theorem requires continuity - methods may fail on functions with jumps or breaks
2. **Multiple Roots**: Both methods find only one root per interval, even if multiple roots exist
3. **Non-Monotonic Functions**: The binary search method assumes monotonic behavior and may not work optimally on functions with local minima/maxima
4. **Complex/Imaginary Roots**: These implementations only find real-valued roots
5. **Very Flat Functions**: Functions with very small derivatives near roots may converge slowly or inaccurately

## Mathematical Background

**Bolzano's Theorem (Intermediate Value Theorem)**: If f is continuous on [a,b] and f(a) and f(b) have opposite signs, then there exists at least one c ∈ (a,b) such that f(c) = 0.

## When to Use Each Method

- **Use Linear Search**: When you need a quick approximation or want to visualize the function behavior across the entire interval
- **Use Binary Search**: When you need high precision, have confirmed a root exists, or are working with computationally expensive functions where minimizing function evaluations is important