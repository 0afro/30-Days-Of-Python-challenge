# Exercises: Level 1
import keyword
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
#1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def evens_and_odds(num):
    if not isinstance(num, int) or num < 0:
        return "Please enter a positive integer."

    even = 0
    odd = 0

    for i in range(0,num+1):
        if i % 2 == 1:
            odd += 1
        else:
            even +=1
    return f'The number of evens are {even}.\nThe number of odds are {odd}.'

print(evens_and_odds(500))

#2 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    if not isinstance(num, int):
        return "Please enter a whole number."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(factorial(4))

#3 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(check):
    if len(check)== 0:
        return True
    else:
        return False

print(is_empty(''))
        
#4 Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_stats(data):
    mean = sum(data) / len(data)
    data_range = max(data) - min(data)
    mode = max(data, key=data.count)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std = variance ** 0.5
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 != 0: 
        median = sorted_data[mid]
    else:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return{
        'Mean' : mean,
        'Range': data_range,
        'Mode' : mode,
        'Median' : median,
        'Variance' : variance,
        'Standard deviation' : std
    }

print(calculate_stats([2, 4, 4, 4, 5, 5, 7, 9]))

#5 Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
#     greet()
#     # "Hello, Guest!
#     greet("Alice")
#     # "Hello, Alice!"
def greet(default = 'Guest'):
    welc_message = 'Hello, '+ default + '!'
    return welc_message

print(greet('Bob'))
print(greet())

#6 Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
# show_args(name="Alice", age=30, city="New York")
# # Received: name: Alice, age: 30, city: New York
# show_args(name="Bob", pet="Fluffy, the bunny")
# # Received: name: Bob, pet: Fluffy, the bunny
def show_args(**args):
    pairs = []
    for key, value in args.items():
        pairs.append(f"{key}: {value}")

    formatted = ", ".join(pairs)
    print(f"Received: {formatted}")

show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")

# Exercises: Level 3
#1 Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))
print(is_prime(1))
print(is_prime(954))

#2 Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    unique_items = set()
    for item in lst:
        if item in unique_items:
            return False
        unique_items.add(item)
    return True

print(is_unique(["Goku", "Shockwave", "Gohan", "Piccolo", "Brawl", "Mindwipe"]))
print(is_unique(["Goku", "Shockwave", "Gohan", "Piccolo", "Piccolo", "Mindwipe"]))

#3 Write a function which checks if all the items of the list are of the same data type.
def isSame_dataType(data):
    if not data:
        return True
    first_type = type(data[0])
    for item in data:
        if type(item) != first_type:
            return False
    return True

print(isSame_dataType([1, 2, 3]))
print(isSame_dataType([1, 'special beam cannon', 3]))

#4 Write a function which check if provided variable is a valid python variable
def isValid_pythonVariable(var_name):
    if var_name.isidentifier() and not keyword.iskeyword(var_name):
        return True
    else:
        return False

print(isValid_pythonVariable("for"))
print(isValid_pythonVariable("user_name"))

#5 Go to the data folder and access the countries-data.py file.
#5a Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
from countries_data import countries_data 
def most_spoken_languages(countries_data,limit=10):
    lang_count={}
    for country in countries_data:
        for lang in country['languages']:
            if lang in lang_count:
                lang_count[lang] +=1
            else:
                lang_count[lang] =1
    counts_list = [(count, lang) for lang, count in lang_count.items()]
    sorted_counts = sorted(counts_list, reverse=True)

    return sorted_counts[:limit]

print(most_spoken_languages(countries_data))
print(most_spoken_languages(countries_data, 20))

#5b Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries_data,limit=10):
    pop_list = []
    for country in countries_data:
        pop_list.append((country['population'], country['name']))
    sorted_pop = sorted(pop_list, reverse=True)

    return sorted_pop[:limit]

print(most_populated_countries(countries_data))
print(most_populated_countries(countries_data, 20))