# homework 3

# say goodbye
def say_goodbye(name):
	return print("Goodbye, " + name)

# area of a circle
def circle_area(radius):
	return print(3.14 * radius ** 2)

# 4.1
def subtract(a, b):
	return a - b
def multiply(a, b):
	return a * b
def divide(a, b):
	return a / b

# 5.1 
def hi_low_temp(readings):
	return (min(readings), max(readings))

#5.2 
def is_weekend(day):
	if day == 6 or day == 7: #67
		return True
	else:
		return False

# 5.3
def fuel_efficiency(distance, fuel_used):
	return distance / fuel_used

# 5.4
def secret_code(input):
	temp = str(input)
	count = 0
	output = ""
	output += temp[-1]
	for char in range(len(temp)-1):
		output += temp[char]
	return int(output)

# 6.1 
def foski(x, y):
	output = x
	for i in range(y-1):
		output *= x
	return output

#6.2.1 
def minimum(ints):
	output = ints[0]
	for i in range(len(ints)):
		if output > ints[i]:
			output = ints[i]
	return output
	#maximum is the same except is a < sign instead. 

# 6.2.2
def minimum_while(ints):
	output = ints[0]
	count = 0
	while len(ints) > count:
		if ints[count] < output:
			output = ints[count]
	return output
	# again, maximum is same except flip sign of the if statement.
# 6.3 
def sum(integer):
	temp = str(integer)
	output = 0
	for i in range(len(temp)):
		output += int(temp[i])
	return output

print(sum(12345))