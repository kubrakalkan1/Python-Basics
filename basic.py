######### iNPUT FROM USER ########
# name = input("What is your name?")
# print("Hello " + name)
# birth_year = input("Enter your birth year: ")

# age = 2022 - int(birth_year)
# print(age)
######### EXERCISE ########
# first_number = input("First: ")
# second_number = input("Second: ")
# sum = float(first_number)+float(second_number)
# print("Sum: ", sum)
######### STRINGS ########
# course = 'Python for Beginners'
# print(course) #Python for Beginners
# print(course.upper()) #PYTHON FOR BEGINNERS
# print(course.lower()) #python for beginners
# print(course.find('y')) #finds index 1
# print(course.find('for')) #finds started index 7
# print(course.replace('for', '4')) #Python 4 Beginners
# print('Python' in course) #True
######### ARITHMETIC OPERATORS ########
# print(10+3) #adding 13
# print(10/3) #divide 3.3333333333333335
# print(10 // 3) #divide  only 1 digit 3
# print(10*3) #multiple 30
# print(10-3) #minus 7
# print(10 % 3) #1
# print(10**3) #1000

# x = 10
# x = x+3 # x+=3 same
# x += 2
# x *= 2
# print(x)
######### COMPARISON OPERATORS ########
# x = 3 > 2 #True
# x = 3 == 2 #False
# x = 3 != 2 #True
######### LOGICAL OPERATORS ########
# price = 25
# print (price > 10 and price < 30) #True two operatior must be true
# print (price > 50 or price < 30) #True one expression is true
######### IF STATEMENTS ########
# temperature = 25
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20: #(20,30]
#     print("It's a nice day")
# elif temperature > 10: #(10,20]
#     print("It's a bit cold")
# else:
#     print("It's a cold day")
# print("Done")
############ EXERCISE #############
# weight= int(input("Weight: "))
# unit= input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print("Weight in Kgs: " + str(converted))
############ WHILE LOOPS ############
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1
#     print(i * '*')
############## LISTS ################
# names = ["John","Bob", "Mosh","Sam" ,"Julie"]
# print(names) #['John', 'Bob', 'Mosh', 'Sam', 'Julie']
# print(names[0]) #John
# print(names[-1]) #Julie
# print(names[-2]) #Same
# names[0] = "Jon"
# print(names) #['Jon', 'Bob', 'Mosh', 'Sam', 'Julie']
# print(names[0:3]) #['Jon', 'Bob', 'Mosh']
# print(names) #['Jon', 'Bob', 'Mosh', 'Sam', 'Julie']

############# LIST METHODS ###################
# numbers = [1,2,3,4,5]
# print(1 in numbers) #True
# print(len(numbers)) #5
# numbers.append(6)
# print(numbers) #[1, 2, 3, 4, 5, 6]
# numbers.insert(0,-1)
# print(numbers) #[-1, 1, 2, 3, 4, 5, 6]
# numbers.remove(3)
# print(numbers) #[-1, 1, 2, 4, 5, 6]
# numbers.clear()
# print(numbers) #[]
############## FOR LOOPS ##################
# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)
# i=0
# while i< len(numbers):
#     print(numbers[i])
#     i = i+1
########### range() FUNCTION ############
# numbers = range(5)
# print(numbers) #range(0, 5)
# for number in numbers:
#     print(number) # 0 1 2 3 4
# numbers = range(5,10,2)
# for number in numbers:
#     print(number) # 5 7 9
# for number in range(5):
#     print(number) # 0 1 2 3 4
########## TUPLES ##############
# numbers = (1,2,3,3) # tuples are immutable and unchangeable
# print(numbers.count(3)) #2

