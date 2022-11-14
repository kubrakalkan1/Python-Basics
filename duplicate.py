numbers = [1,2,2,5,7,9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
