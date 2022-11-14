# exit code 0 ---> program terminated successfully, there no errors
# ValueError ---> exit code 1 program crash because invalid value
# ZeroDivisionError ----> division by zero
# handle errors
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")
