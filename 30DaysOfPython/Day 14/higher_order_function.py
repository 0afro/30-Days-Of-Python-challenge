# Exercises: Day 14 
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

#1 Explain the difference between map, filter, and reduce.
'Map takes a single item and applies it to the entire list,'
'whereas a filter kicks out any item which is not true to function'
'And reduce snowballs a list into one final value'

#2 Explain the difference between higher order function, closure and decorator
'A higher-order function is a function that accepts another function as an argument or returns one.'
'A closure is a specific type of higher-order function which is an inner function remembering outer variables.'
'A decorator is a specific way to use a closure to wrap extra behaviour around a function using @ to modify it'

#3 Define a call function before map, filter or reduce, see examples.
def double_it(num):
    doubled= (num*2)
    return doubled
print(list(map(double_it, numbers)))


def is_long_word(word):
    default = 5
    if len(word) > default:
        return(True)
    else:
        return(False)
print(list(filter(is_long_word, names)))


def add_two_nums(x, y):
    return x+y
print(reduce(add_two_nums, numbers))


#4 Use for loop to print each country in the countries list.
for country in countries:
    print(country)

#5 Use for to print each name in the names list.
for name in names:
    print(name)

#6 Use for to print each number in the numbers list.
for number in numbers:
    print(number)


# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
# Use map to create a new list by changing each number to its square in the numbers list
# Use map to change each name to uppercase in the names list
# Use filter to filter out countries containing 'land'.
# Use filter to filter out countries having exactly six characters.
# Use filter to filter out countries containing six letters and more in the country list.
# Use filter to filter out countries starting with an 'E'
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# Use reduce to sum all the numbers in the numbers list.
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.



# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population
# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.
