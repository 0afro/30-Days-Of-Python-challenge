import numpy
{
    'firstname' : 'Muhammed',
    'Surname' : 'Marong',
    'Age' : '20',
    'Location' : 'England',
    'isMarried' : False,
    'Skills' :['roblox', 'brawl stars', 'football', 'gym']
} #Dictionary

('Goku', 'Vegeta', 'Piccolo', 'Trunks', 'Gohan', 'Tien') #names example of tuple(noneditable list)

{4,67,856,1,99,45} #set (order does not matter)

print(2 + 3) #addition
print(3 - 1) #subtract
print(2 * 3) #multiply
print(50 / 10) #divide
print(3 ** 7) #exponential **
print(90 // 7) #floor division operative //
print(19 % 2) #modulos %

print(type(10))
print(type(2.5))
print(type('aaaa'))
print(type(-67))
print(type(True))
print(type({'firstname' : 'bee'}))
print(type(('goku', 'vegeta', 'piccolo', 'Tien')))
print(type({23,59,42,1,10,29}))
print(type(4 - 4j))

a = numpy.array((2,3))
b = numpy.array((10,8))

distance = numpy.linalg.norm(b-a)
print(distance)