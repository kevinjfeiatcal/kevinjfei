# File: homework 4

# 3: Lists
# 3.1
foods = ["Yogurt", "Orange Juice", "Noodles", "Beef Stew", "Feijoada"]
print(foods[1])
print(foods[-1])
foods.append("Clam Chowder")
foods.insert(0, "pasta")
del foods[2]
print(len(foods))

for food in foods:
    if food.upper():
        print(food)

newfoods = [foods[0], foods[-1]]

is_potato = False
for food in newfoods:
    if food == "potato":
        is_potato = True
if is_potato:
    print("A potato!")
else:
    print("No potato!")
    
# 3.2
numbers = []
for i in range(21):
    numbers.append(i)

def get_first_15(numbers):
    fifteen = []
    for i in range(15):
        fifteen.append(numbers[i])
    return fifteen

def get_every_5th(first):
    return first[::5]

def reverse_and_stride(first):
    return get_every_5th(first)[::-3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(matrix[2])
print(matrix[2][2])
matrix.append([10, 11, 12])

def sum_nested(lists):
    total = 0
    for sublist in lists:
        for num in sublist:
            total += num
    return total

def fivebyfive():
    matrix = []
    num = 1
    for a in range(5):
        row = []
        for b in range(5):
            row.append(num)
            num += 1
        matrix.append(row)
    return matrix

def removex3(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] % 3) == 0:
                matrix[i][j] = "?"
    return matrix

def sumnotquestion(matrix):
    sum = 0
    for row in matrix:
        for index in row:
            if index != "?":
                sum += index
    return sum

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])
ages["Mariam"] = 100
ages["Milana"] = 52
ages.pop("Mariam")

for key in ages:
    print(key, ages[key])

# can also get values .items() after the dictionary for both.

print(sumnotquestion(fivebyfive()))