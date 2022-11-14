# def greet(first_name, last_name): #first_name and last_name are parameters. Parameter is the input define for your function
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome abroad")
#
# greet("Kubra","Kalkan") # Kubra and Kalkan are arguments. Argument is the actual value for a given parameter
# greet("Mustafa","Kalkan")

### All default function return None by default unless you specificly return a value.
# def greet(name): #(Type 1) types of functions: 1-Perform a task, 2- Return a value
#     print(f"Hi {name}")
#
# def get_greeting(name): #(Type 2)
#     return f"Hi {name}"
#
# message = get_greeting("Kubra")
# print(message)

# def increment(number,by):
#     return  number + by
#
# print(increment(2,1)) # result = increment(2,1) print(result) this is the same
#
# print(increment(2, by=1))

# def increment(number,by=1):
#     return  number + by
#
# print(increment(2))
# print(increment(2,5))

# def multiply (x,y):
#     return x*y
#
# print(multiply(2,3))

# def multiply (*numbers):
#     total = 1
#     for number in numbers:
#         total *= number #  total = total * number
#     return total
#
# print(multiply(2,3,4,5)) #tuples just like list iterable

# def save_user(**user): # when we use multiple asterix we can pass multiple key value pairs or multiple arguments to a function
#     print(user)
#
# save_user(id=1, name="John", age=22) #{'id': 1, 'name': 'John', 'age': 22} this is dictionary

# message= "a" # this is global variable
#
# def greet(name):
#     global message # this make local variable to global variable but this is bad practice, this probably make bug in code
#     message= "b" # this is a local variable
#
# greet("Kubra")
# print(message)

######## FIZZ-BUZZ #############
# def fizz_buzz(num):  ## 1 way
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
#
# fizz_buzz(7)

# def fizz_buzz(input): ## 2.Way
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input
# print(fizz_buzz(3))
