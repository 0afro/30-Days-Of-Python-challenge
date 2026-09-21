# Exercises: Day 8
#1 Create an empty dictionary called dog
dog = {}

#2 Add name, color, breed, legs, age to the dog dictionary
dog['Name'] = 'Max'
dog['Breed'] = 'Golden Retriever'
dog['Legs'] = 4
dog['Color'] = 'White'
dog['Age'] = 3
print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student= {
    'first_name':'John',
    'last_name':'Doe',
    'gender': 'Male',
    'age':'19',
    'marital_status':'Married',
    'skills':['Kungfu', 'Karate', 'Boxing', 'Grappling', 'Swimming'],
    'country':'Uzbekistan',
    'address':'8 Fighter Street'
}

#4 Get the length of the student dictionary
print(len(student))

#5 Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

#6 Modify the skills values by adding one or two skills
student['skills'].extend(['Spinjitzu', 'Airjutsu'])
print(student)

#7 Get the dictionary keys as a list
print(list(student.keys()))

#8 Get the dictionary values as a list
print(list(student.values()))

#9 Change the dictionary to a list of tuples using items() method
print(list(student.items()))

#10 Delete one of the items in the dictionary
del student['age']
print(student)

#11 Delete one of the dictionaries
del dog
#print(dog)
