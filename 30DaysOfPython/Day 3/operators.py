## Exercises - Day 3

#1 Declare your age as integer variable
age = 20
print('I am ', age)
#2 Declare your height as a float variable
height = 185.6
print('I am ', height, 'cm')
#3 Declare a variable that store a complex number
complex_num = 6+7j
print(complex_num)
#4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#    Enter base: 20
#    Enter height: 10
#    The area of the triangle is 
base = int(input('what is the base: '))
height = int(input('what is the height: '))
area = (0.5 * base * height)
print('the area of your triangle is: ', area)

#5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    #Enter side a: 5
    #Enter side b: 4
    #Enter side c: 3
    #The perimeter of the triangle is 
side_a = int(input('what is the length of side a: '))
side_b = int(input('what is the length of side b: '))
side_c = int(input('what is the length of side c: '))
perimeter = side_a + side_b + side_c
print('the perimeter of your triangle is', perimeter, 'cm')

#6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter the length of your rectangle: '))
width = int(input('Enter the width of your rectangle: '))
area = (length * width)
perimeter = (2 * (length + width))
print('Your area is', area, 'cm^2')
print('Your perimeter is', perimeter, 'cm')

#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = float(input('Enter your radius: '))
area = (pi * radius * radius)
circumference = (2 * pi * radius)
print('The area of the circle is', area,'cm^2')
print('The circumference of the circle is', circumference, 'cm')

#8 Calculate the slope, x-intercept and y-intercept of y = 2x - 2
m = 2
b = -2
x_intercept = -b/m
print('The slope is', m)
print('The x-intercept is', (x_intercept,0))
print('The y-intercept is', (0,b))

#9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1=2 
y1=2 
x2=6 
y2=10
slope = (y2-y1)/(x2-x1)
print('the slope is', slope)
Euclidean_dist= (((x2-x1)**2) + ((y2-y1)**2))**0.5
print('the euclidean distance is', Euclidean_dist)

#10 Compare the slopes in tasks 8 and 9.
if m == slope:
    print('The two slopes are not equal')
else: 
    print('The slopes are equal')

#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x=-3 #x=-3 y=0  #x=-2 y= 1 #x= -1 y= 4
Value_of_y= (x)**2 + 6*(x) + 9
print(Value_of_y, 'is the value of y')

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
word1 = len('python')
word2 = len('dragon')
print(word1 != word2)

#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print(('on' in 'dragon') and ('on' in 'python'))

#14 'I hope this course is not full of jargon.' Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

#15 There is no 'on' in both dragon and python
print(('on' not in 'dragon') and ('on' not in 'python'))

#16 Find the length of the text python and convert the value to float and convert it to string
text = float(len('python'))
print(str(text))

#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numb = int(input('Enter your number '))
calc_numb= numb%2
if calc_numb == 0:
    print('This number is even')
else:
    print('This number is odd')

#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
calc_one = 7//3
calc_two = int(2.7)
#if calc_one == calc_two:
#    print('They are equal')
#else:
#    print('They are not equal')
print(calc_one == calc_two)

#19 Check if type of '10' is equal to type of 10
#if type('10') == type(10):
#    print(True)
#else:
#    print(False)
print(type('10')== type(10))

#20 Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120
hours = float(input('How many hours do you do?'))
rate = float(input('What is your hourly rate?'))
weekly = hours * rate
print('Your weekly earnings are £',weekly)

#22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#Enter number of years you have lived: 100
#You have lived for 3153600000 seconds.
year = 31536000
years = int(input('Enter how many years... '))
final = year * years
print('You have lived for ', final, 'seconds!!!')

#23 Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print('1, 1**0, 1**1, 1**2, 1**3')
print('2, 2**0, 2**1, 2**2, 2**3')
print('3, 3**0, 3**1, 3**2, 3**3')
print('4, 4**0, 4**1, 4**2, 4**3')
print('5, 5**0, 5**1, 5**2, 5**3')