print("Hello world")
# variables

age=20
isOnline=False # it is case sensitive 
print(isOnline)

# receive input
name =input("What is your name? ")
print("Hello " + name) # string concatenated

# change variable types

birth_year = input("What is your birth year? ")
userAge = 2023 - int(birth_year)
print("Your age is " + str(userAge))

# add

first = float(input("First Number"))
second = float(input("Second Number"))
print("sum:"+str(first+second))

# Characters

course = 'Python for beginners'
print(course.replace('for','4'))

# arithmetic operations

print(10//3) # here we get an integer

print(10/3) # here we get floating numbers
print(10%3) # modulus
print(10**3) # to the power of nth number

## augmented assignment operations
x=20 
x=x+3 
x+=3

# conditional operations

temperature = 25

if temperature>30 :
    print("It is a hot day")
    print("So hot")
elif temperature >20:
    print("It is a nice day")
else:
    print("It is cold")