# Exercises: Day 6

# Exercises: Level 1
#1 Create an empty tuple
empty = ()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brother_names = ('Alan','Bob', 'Carl', 'Dan')
sister_names = ('Alice', 'Barbara', 'Carol', 'Denisa')

#3 Join brothers and sisters tuples and assign it to siblings
siblings = brother_names + sister_names

#4 How many siblings do you have?
print(len(siblings))

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
list_version = list(siblings)
list_version.insert(0,'Goku')
list_version.insert(0,'Chichi')
print(list_version)
family_members = tuple(list_version)
print(family_members)


# Exercises: Level 2
#1 Unpack siblings and parents from family_members
parent_1, parent_2, *sibling_list = family_members
siblings_v2 = tuple(sibling_list)
print('The parents are,', parent_1, 'and', parent_2)
print('The siblings are', siblings_v2)
#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruit = ('apple', 'mango', 'pear', 'grapefruit')
animal_products = ('milk', 'meat', 'butter', 'cheese')
vegetables = ('carrot', 'cabbage', 'aubergine', 'potato')
food_stuff_tp = fruit + animal_products + vegetables

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(len(food_stuff_lt))
middle_index = len(food_stuff_lt)//2
print(food_stuff_lt[middle_index])


#5 Slice out the first three items and the last three items from food_stuff_lt list
first_three= food_stuff_lt[0:3]
last_three= food_stuff_lt[-4:]
print('First three are: ', first_three, 'Last three are: ', last_three)


#6 Delete the food_stuff_tp tuple completely
del food_stuff_tp

#7 Check if an item exists in tuple:
print('bob' in brother_names)

#8 Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)


#9 Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)

