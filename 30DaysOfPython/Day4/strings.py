#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word_one = 'Thirty '
word_two ='Days '
word_three = 'Of '
word_four = 'Python'
print(word_one+word_two+word_three+word_four)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
w1, w2, w3 = 'Coding ', 'For ', 'All'
print(w1+w2+w3)

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4 Print the variable company using print().
print(company)

#5 Print the length of the company string using len() method and print().
print(len(company))

#6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string.
sliced_company= company[0:6]
print(sliced_company)

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))

#11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

#12 Change "Python for Everyone" to "Python for All" using the replace method or other methods.
word1 = 'Python for Everyone'
print(word1.replace('Everyone', 'All'))

#13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

#15 What is the character at index 0 in the string Coding For All.
first_char = company[0]
print(first_char)

#16 What is the last index of the string Coding For All.
total_length= len(company)
print(total_length)
last_index= len(company)-1
print(last_index)
#17 What character is at index 10 in "Coding For All" string.
char10= company[10]
print(char10)

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
words = company.replace('Coding', 'Python').split()
print(words)
acronym = words[0][0]+ words[1][0]+words[2][0]
print(acronym)

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
words = company.split()
print(words)
acronym = words[0][0]+ words[1][0]+words[2][0]
print(acronym)

#20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
new_word= 'Coding For All People'
print(new_word.rfind('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new_sentence = 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.index('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.rindex('because'))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced_new_sentence = new_sentence[31:54]
print(sliced_new_sentence)

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.index('because'))

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sliced_new_sentence)

#28 Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

#29 Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
word_new ='   Coding For All      '
#print(word_new.strip('  '))
print(word_new.strip())

#31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
statement1 = '30DaysOfPython'
statement2 = 'thirty_days_of_python'
print(statement2.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
random = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(random))

#33 Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I am enjoying this challenge.
print('I am enjoying this challenge. \nI am enjoying this challenge.')

#34 Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')


#35 Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius= 10
pi = 3.14
area = pi*radius**2
format_version = 'The area of circle with a radius %d is %d metres square.' %(radius, area)
print(format_version)

#36 Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a= 8
b= 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')
