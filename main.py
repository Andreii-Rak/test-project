#function computes factorial of a given number
def factorial(n):
	result = 1
	i=1
	while i<=n:
		result*=i
		i+=1
	return result

#read input from user
n = int(input('Enter a number: '))

#calculate factorial
result = factorial(n)

print('Factorial from the input number is:',result)


# def is_int(str):
#     try:
#         int(str)
#         return True
#     except ValueError:
#         return False
# a = result
# print('Is it an integer:',is_int(a))

if (result % 2) == 0:
	print("This number is even".format(result))
else:
	print("This number is odd".format(result))


my_array = []
my_array.append(result)
my_array.append(result)
my_array.append(result)
my_array.append(result)
print(my_array)

import random
random_numbers = random.randint(1,10)
print("Random number:", random_numbers)


def custom_randomizer(result, random_numbers):
	return result * random_numbers
print(custom_randomizer(result, random_numbers))

my_array[0]= custom_randomizer(result, random_numbers)
my_array[1]= custom_randomizer(result, random_numbers)
my_array[2]= custom_randomizer(result, random_numbers)
my_array[3]= custom_randomizer(result, random_numbers)
print(my_array)