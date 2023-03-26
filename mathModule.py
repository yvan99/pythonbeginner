import math

# Basic mathematical operations
a = 5
b = 3
print(f"a + b = {a + b}")   # Addition
print(f"a - b = {a - b}")   # Subtraction
print(f"a * b = {a * b}")   # Multiplication
print(f"a / b = {a / b}")   # Division
print(f"a % b = {a % b}")   # Modulo
print(f"a ** b = {a ** b}") # Exponentiation

# Trigonometric functions
theta = math.pi / 4  # 45 degrees in radians
print(f"sin({theta}) = {math.sin(theta)}")
print(f"cos({theta}) = {math.cos(theta)}")
print(f"tan({theta}) = {math.tan(theta)}")
print(f"asin(1/{math.sqrt(2)}) = {math.asin(1/math.sqrt(2))}")
print(f"acos(1/{math.sqrt(2)}) = {math.acos(1/math.sqrt(2))}")
print(f"atan(1) = {math.atan(1)}")

# Logarithmic functions
print(f"log({a}) = {math.log(a)}")
print(f"log10({a}) = {math.log10(a)}")
print(f"log2({a}) = {math.log2(a)}")
print(f"e ** {a} = {math.exp(a)}")

# Other functions
print(f"sqrt({a}) = {math.sqrt(a)}")
print(f"ceil(4.3) = {math.ceil(4.3)}")
print(f"floor(4.7) = {math.floor(4.7)}")
print(f"fabs(-5) = {math.fabs(-5)}")
print(f"factorial(5) = {math.factorial(5)}")
