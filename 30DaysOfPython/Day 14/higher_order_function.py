# Exercises: Day 14 
from functools import reduce
from countries import countries
from countries_data import countries_data 
#countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
position_number= ['Striker',9,'Wingers',11,7,'Midfielders',8,10,6,'Defenders',2,3,4,5,'Goalkeeper',1]

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
#1 Use map to create a new list by changing each country to uppercase in the countries list
def change_to_upper(country):
    return country.upper()
uppercase_countries = list(map(change_to_upper, countries))
print(uppercase_countries)

#2 Use map to create a new list by changing each number to its square in the numbers list
def square_num(num):
    return num ** 2
squared_numbers = list(map(square_num, numbers))
print(squared_numbers)

#3 Use map to change each name to uppercase in the names list
def change_to_upper(names):
    return names.upper()
uppercase_names = list(map(change_to_upper, names))
print(uppercase_names)

#4 Use filter to filter out countries containing 'land'.
def contain_land(countries):
    if 'land' in countries:
        return False
    else:
        return True
print(list(filter(contain_land,countries)))

#5 Use filter to filter out countries having exactly six characters.
def six_char(countries):
    if len(countries)==6:
        return False
    else:
        return True
print(list(filter(six_char,countries)))

#6 Use filter to filter out countries containing six letters and more in the country list.
def six_plus(countries):
    if len(countries)>=6:
        return False
    else:
        return True
print(list(filter(six_plus,countries)))

#7 Use filter to filter out countries starting with an 'E'
def no_e_allowed(countries):
    if countries[0] == 'E':
        return False
    else:
        return True
print(list(filter(no_e_allowed,countries)))

#8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
def greater_than_ten(num):
    return num > 10
result = list(filter(greater_than_ten, map(double_it, numbers)))
print(result)

#9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
print(get_string_lists(position_number))

#10 Use reduce to sum all the numbers in the numbers list.
def add_two_nums(x, y):
    return x + y
total = reduce(add_two_nums, numbers)
print(total)

#11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def mashed_sentence(x,y):
    return x + ', '+ y
all_except_last = reduce(mashed_sentence, countries[:-1])
final_sentence = f"{all_except_last}, and {countries[-1]} are north European countries"

print(final_sentence)

#12 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern, countries_list):
    return list(filter(lambda country: pattern in country.lower(), countries_list))

print(categorize_countries('land', countries))

#13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def country_starting_letters(countries_list):
    counts = {}
    for country in countries_list:
        letter = country[0]
        counts[letter] = counts.get(letter, 0) + 1
    return counts

print(country_starting_letters(countries))

#14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(countries_list):
    return countries_list[:10]

print(get_first_ten_countries(countries))

#15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries_list):
    return countries_list[-10:]

print(get_last_ten_countries(countries))


# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#1 Sort countries by name, by capital, by population
sorted_by_name = sorted(countries_data, key=lambda x: x['name'])

#2 Sort out the ten most spoken languages by location.
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])

#3 Sort out the ten most populated countries.
sorted_by_population = sorted(countries_data, key=lambda x: x['population'])
