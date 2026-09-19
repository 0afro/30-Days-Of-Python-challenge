# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
#1 Find the length of the set it_companies
print(len(it_companies))

#2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3 Insert multiple IT companies at once to the set it_companies
extra_it =('Adobe', 'Intel', 'Nvidia', 'Dell', 'HP')
it_companies.update(extra_it)
print(it_companies)

#4 Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

#5 What is the difference between remove and discard
#Remove takes out a value but will give an error if not found discard gives no error

# Exercises: Level 2
#1 Join A and B
joint_set = A.union(B)
print(joint_set)

#2 Find A intersection B
print(A & B)

#3 Is A subset of B
print(A.issubset(B))

#4 Are A and B disjoint sets
print(A.isdisjoint(B))

#5 Join A with B and B with A
a_joint = A.union(B)
b_joint = B.union(A)
print(a_joint)
print(b_joint)

#6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#7 Delete the sets completely
del A
del B

# Exercises: Level 3
#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Ages = set(age)
if len(Ages) > len(age):
    print('The set length is longer than the list version')
elif len(age) > len(Ages):
    print('The list version is longer than the set version')
else:
    print('They are the same length')

#2 Explain the difference between the following data types: string, list, tuple and set
# A string is an immutable sequence of characters written in quotes. 
# A list is ordered, mutable, and defined with square brackets [].
# A tuple is ordered, immutable, and defined with parentheses ().
# A set is an unordered, mutable collection of unique items defined with curly braces {}

#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
lower = sentence.lower()
words = lower.split()
new_sentence = list(words)
set_version = set(new_sentence)
print(len(set_version))

