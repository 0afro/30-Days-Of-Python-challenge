#1 Declare an empty list
empty_list = []

#2 Declare a list with more than 5 items
inazuma = ['Jude Sharp','Axel Blaze','Mark Evans', 'Jack Wallside', 'Nathan Swift']

#3 Find the length of your list
print(len(inazuma))

#4 Get the first item, the middle item and the last item of the list
print(inazuma[0],inazuma[2], inazuma[-1])

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Muhammed Marong', 20, 185.6, 'Single', 'London']

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook','Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7 Print the list using print()
print(it_companies)

#8 Print the number of companies in the list
print(len(it_companies))

#9 Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[-1])

#10 Print the list after modifying one of the companies
it_companies.pop(0)
print(it_companies)

#11 Add an IT company to it_companies
it_companies.append('Chud Company')

#12 Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Chad comapany')
print(it_companies)

#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print(it_companies)

#14 Join the it_companies with a string '#;  '
new_company ='#;  '.join(it_companies)
print(new_company)

#15 Check if a certain company exists in the it_companies list.
does_exist = 'Chud Company' in it_companies
print(does_exist)

#16 Sort the list using sort() method
it_companies.sort()
print(it_companies)
#17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
#18 Slice out the first 3 companies from the list
print(it_companies[0:3])

#19 Slice out the last 3 companies from the list
print(it_companies[:-4:])

#20 Slice out the middle IT company or companies from the list
print(it_companies[3:5])

#21 Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#22 Remove the middle IT company or companies from the list
it_companies.pop(4)
print(it_companies)

#23 Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25 Destroy the IT companies list
del it_companies
#print(it_companies)

#26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end + back_end
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

#28 Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#A) Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]

#B) Add the min age and the max age again to the list
ages.insert(-1,min_age)
ages.insert(-1,max_age)
ages.sort()
print(ages)

#C) Find the median age (one middle item or two middle items divided by two)
print(len(ages))
middle_index = len(ages)//2
median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
print(median_age)

#D) Find the average age (sum of all items divided by their number )
total = sum(ages)
average = total / len(ages)
print(average)

#E) Find the range of the ages (max minus min)
print(max_age-min_age)

#F) Compare the value of (min - average) and (max - average), use abs() method
mini = abs(min_age-average) 
maxi = abs(max_age-average)
if mini < maxi:
    print('the minimum value is closer to the average than the maximum')
elif maxi < mini:
    print('the maximum value is closer to the average than the minimum')
else:
    print('The distances from the average between both are equal')

#G) Find the middle country(ies) in the countries list
from countries import countries
print(len(countries))
mid_point = len(countries)//2
print(countries[mid_point])

#29  Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half =countries[0:mid_point+1]
print(countries[mid_point+1:])

#30 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_v2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2,country3, *rest = countries_v2
print(country1)
print(country2)
print(country3)
print('Scandic Countries: ', rest)
