# Exercises: Day 9
# Exercises: Level 1
#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
user_age = int(input('Enter your age: '))
legal_age = 18
if user_age >= legal_age:
    print('You are old enough to drive.')
else:
    print('You need', legal_age - user_age, 'more years till you can drive.')

#2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = 20 
your_age = int(input('Enter your age: '))

if my_age > your_age:
    diff= my_age-your_age
    if diff == 1:
        print('I am ', diff, 'year older than you')
    elif diff>1:
        print('I am ', diff, 'years older than you')
elif my_age < your_age:
    diff= your_age-my_age
    if diff == 1:
        print('You are ', diff, 'year older than me!')
    elif diff>1:
        print('You are ', diff, 'years older than me!')
else:
    print('We are the same age!')

#3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
print('Welcome to the almighty super powerful decepticon number thingy')
a = int(input('Enter a number: '))
b = int(input('Enter a second number: '))

if a > b:
    print(a, 'is greater than', b)
elif a < b:
    print(a, 'is smaller than', b)
else:
    print(a, 'and', b, 'are equal')

# Exercises: Level 2
#1 Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```
score = int(input('What mark did you get: '))
if score >= 90:
    print('You scored an A! WOW!')
elif score >= 80:
    print('You scored a B. Nice!')
elif score >= 70:
    print('You scored a C. Nice!')
elif score >= 60:
    print('You scored a D. Nice!')
else:
    print('You scored a F. Unlucky :(')

#2 Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, the season is Summer
input_month = input(('What month are you thinking: '))
user_month = input_month.lower()

if user_month in ['september','october','november']:
    print('The season is Autumn. Expect a bit of rain')
elif user_month in ['december','january','february']:
    print('The season is Winter. Chilly!')
elif user_month in ['march','april','may']:
    print('The season is Spring. Ah just right!')
elif user_month in ['june','july','august']:
    print('The season is Summer. Do not forget sunscreen!')
else:
    print('Please enter a valid month!!')


#3 The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input('Please enter a fruit: ').lower()
if user_fruit in fruits:
    print('This fruit already exists in the list!')
else:
    fruits.append(user_fruit)
    print(fruits)

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name':'John',
    'last_name':'Doe',
    'gender': 'Male',
    'age':'19',
    'marital_status':'Married',
    'skills':['Kungfu', 'Karate', 'Boxing', 'Grappling', 'Swimming', 'React', 'JavaScript', 'MongoDB'],
    'country':'Uzbekistan',
    'address':'8 Fighter Street'
     }


#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills_list = person['skills']
    middle_index = len(skills_list)//2
    print(skills_list[middle_index])
else:
    print('This person has no skills section!!')
    
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print('This person has python as a skill')
else:
    print('This person does not have python skills!!')

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
user_skill = set(person['skills'])
if 'skills' in person:
    if user_skill == {'Javascript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(user_skill):
        print('He is a backend developer')
    elif {'React', 'Node','MongoDB'}.issubset(user_skill):
        print('He is a fullstack developer')
    else:
        print('Unknwon title (u sure he is a dev?)')
else:
    print('No skills key found')

#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if person.get('marital_status') == 'Married' and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']} (not Finland).")