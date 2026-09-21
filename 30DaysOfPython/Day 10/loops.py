# Exercises: Day 10
# Exercises: Level 1
#1 Iterate 0 to 10 using for loop, do the same using while loop.
number = 0
while number < 11:
    print(number)
    number = number+1

number_list = [0,1,2,3,4,5,6,7,8,9,10]
for number_list in number_list:
    print(number_list)

#2 Iterate 10 to 0 using for loop, do the same using while loop.
number = 10
while number > -1:
    print(number)
    number = number-1

reverse = list(range(10,-1,-1))
print(reverse)

#3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
thing = '#'
for number in range(1, 8):
    print(thing * number)


#4 Use nested loops to create the following:
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
for row in range(8):
    for col in range(8):
        print(thing, end=' ')
    print()


#4 Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for numbers in range(0,11):
    print(f"{numbers} x {numbers} = ", numbers*numbers)


#5 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lang = ['Python', 'Numpy','Pandas','Django', 'Flask']
for word in lang:
    print(word)

#6 Use for loop to iterate from 0 to 100 and print only even numbers
for even in range (0,101,2):
    print(even)

#7 Use for loop to iterate from 0 to 100 and print only odd numbers
for odd in range(0,101):
    if odd % 2 == 1:
        print(odd)

# Exercises: Level 2
#8 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
total = 0
for num in range (0,101):
    total = total + num
print('The sum of all numbers is ',total)

#9 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
total_even = 0
for even in range (0,101,2):
    total_even = total_even + even
print('The sum of all evens is',total_even)

total_odd = 0
for odd in range (0,101):
    if odd % 2 == 1:
        total_odd = total_odd + odd
print('The sum of all odds is',total_odd)


# Exercises: Level 3
#10 Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from countries import countries

for country in countries:
    if 'land' in country.lower():
        print(country)

#11 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in range(-1,-5,-1):
    print(fruits[i])

#12 Go to the data folder and use the countries_data.py file.
#a What are the total number of languages in the data
from countries_data import countries_data 
unique_lang = set()
for country in countries_data:
    for languages in country['languages']:
        unique_lang.add(languages)
print('There are a total of',len(unique_lang), 'languages in the data.')

#b Find the ten most spoken languages from the data
lang_count={}
for country in countries_data:
    for languages in country['languages']:
        if lang in lang_count:
            lang_count[lang] +=1
        else:
            lang_count[lang] =1
counts_list = []
for lang, count in lang_count.items():
    counts_list.append((count, lang))
sorted_counts =sorted(counts_list, reverse=True)
top_10 =sorted_counts[:10]

print("Top 10 most spoken languages:")
for count, lang in top_10:
    print(f"{lang}: {count} countries")

#c Find the 10 most populated countries in the world
pop_list = []
for country in countries_data:
    pop_list.append((country['population'], country['name']))
sorted_pop = sorted(pop_list, reverse=True)

top_10_populated=sorted_pop[:10]
print("Top 10 most populated countries:")
for pop, name in top_10_populated:
    print(f"{name}: {pop:,}")
