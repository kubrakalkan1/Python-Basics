# prices = [10,20,30]
# total = 0
# for price in prices:
#     total += price
# print(total)
# print(f"Total: {total}")
# ###### NESTED LOOP ###### easliy generate a list of coordinate
# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")
######### F shape with loop #########
# numbers = [5,2,5,2,2]
# for number in numbers: # 1. way
#     print(number * "x")
# for x_count in numbers: # 2. way
#     output = ''
#     for count in range(x_count):
#         output += "x"
#     print(output)
#### 2D LIST ###
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1]) #2
matrix[0][1] = 20
print(matrix[0][1]) #20

for row in matrix:
    for item in row:
        print(item)
