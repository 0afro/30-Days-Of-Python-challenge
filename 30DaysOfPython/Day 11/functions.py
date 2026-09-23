# Exercises: Level 1
#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    total = a + b
    return total

print(add_two_numbers(65,2))

#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle():
    pi = 3.14
    r = float(input('What is your radius? '))
    total = pi*r*r
    return total

print(area_of_circle())

#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total=0
    for num in nums:
        if type(num) != int and type(num) != float:
            return "Please provide only numbers (integers or floats)."
        total += num    
    return total

print(add_all_nums(19999,4122.44,5285,122,12200245))

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def celsius_2_fahrenheit(c):
    total = (c*9/5)+32
    return total

print(celsius_2_fahrenheit(20))

#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    months = month.lower()
    if months in ['september','october','november']:
        return('The season is Autumn. Expect a bit of rain')
    elif months in ['december','january','february']:
        return('The season is Winter. Chilly!')
    elif months in ['march','april','may']:
        return('The season is Spring. Ah just right!')
    elif months in ['june','july','august']:
        return('The season is Summer. Do not forget sunscreen!')
    else:
        return('Please enter a valid month!!')

print(check_season('Starscream'))

#6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(y,x,b):
    m= (y-b)/x
    return m

print(calculate_slope(10,6,7))

#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    x_positive= (-b+ (b**2 - 4*a*c)**0.5)/(2*a)
    x_negative = (-b- (b**2 - 4*a*c)**0.5)/(2*a)
    return x_negative, x_positive

print(solve_quadratic_eqn(1,-3,2))

#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(characters):
    for item in characters:
        print(item)

print_list(["Goku", "Vegeta", "Gohan", "Piccolo", "Krillin", "Frieza"])

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"])) 
# # ["C", "B", "A"]
def reverse_list(lst):
    reversed_list =[]
    for char in lst:
        reversed_list.insert(0,char)
    return(reversed_list)

print(reverse_list(["Goku", "Vegeta", "Gohan", "Piccolo", "Krillin", "Frieza"]))

#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized_list=[]
    for char in lst:
        capitalized_list.append(char.capitalize())
    return capitalized_list

print(capitalize_list_items(["goku", "vegeta", "gohan", "piccolo", "krillin", "frieza"]))


#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
def add_item(lst,item):
    lst.append(item)
    return lst
colour=['red','green','pink']
print(add_item(colour,'blue'))

#12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(lst,item):
    lst.remove(item)
    return lst
char = ["Goku", "Shockwave", "Gohan", "Piccolo", "Brawl", "Mindwipe"]
print(remove_item(char,'Brawl'))

#13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
def sum_of_numbers(numb):
    total = 0
    for numb in range(0,numb+1):
        total = numb + total
    return total
print(sum_of_numbers(69))

#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odd(numb):
    total=0
    for odd in range(0,numb+1):
        if odd % 2 == 1:
                total = total + odd
    return total
print(sum_of_odd(10))

#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(numb):
    total=0
    for even in range(0,numb+1,2):
        total = total + even
    return total
print(sum_of_even(10))

# Exercises: Level 2