#Day 2: 30 days or python programming

#1 Declare a first name variable and assign a value to it
first_name = 'Muhammed'
#2 Declare a last name variable and assign a value to it
last_name = 'Marong'
#3 Declare a full name variable and assign a value to it
full_name = 'Muhammed Marong'
#4 Declare a country variable and assign a value to it
country = 'England'
#5 Declare a city variable and assign a value to it
city = 'London'
#6 Declare an age variable and assign a value to it
age = 20
#7 Declare a year variable and assign a value to it
year = 2026
#8 Declare a variable is_married and assign a value to it
is_married = False
#9 Declare a variable is_true and assign a value to it
is_true = True
#10 Declare a variable is_light_on and assign a value to it
is_light_on = False
#11 Declare multiple variable on one line
foot, position, height, weight, team = 'left', 'centreback', 185.6, 83, 'Arsenal'
print('Player Name is ',full_name, 'Player is ', age, 'Player is a', position, 'and is ', foot, 'footed')

#1 Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(height))
print(type(is_light_on))
print(type(year))
#2 Using the len() built-in function, find the length of your first name
print(len(first_name))
#3 Compare the length of your first name and your last name
print(len(first_name))
print(len(last_name))
if len(first_name) > len(last_name):
    print(True)
#Intended way below
#print(len(first_name))
#print(len(last_name))
#print(len(first_name) > len(last_name))

#4 Declare 5 as num_one and 4 as num_two
num_one= 5 
num_two = 4
#5 Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)
#6 Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)
#7 Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(product)
#8 Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
print(division)
#9 Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two%num_one
print(remainder)
#10 Calculate num_one to the power of num_two and assign the value to a variable 
power = num_one**num_two
print(power)
#11 Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one//num_two
print(floor_division)

#12 The radius of a circle is 30 meters.
#12a Calculate the area of a circle and assign the value to a variable name of area_of_circle
pi = 3.14
radius = 30
print(pi * radius**2)

#12b Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = radius * 2
print(circum_of_circle)

#12c Take radius as user input and calculate the area.
radius = input('Enter the radius: ')
radius = int(radius)
print(pi * radius**2)

#13 Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name2 = input('Enter first name: ')
last_name2 = input('Enter last name: ')
country2 = input('Enter your country: ')
age2 = input('Enter your age: ')

#14 Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')