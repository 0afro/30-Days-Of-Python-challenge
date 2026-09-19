fruit = ['banana', 'orange', 'mango', 'lemon', 'apple', 'mango', 'pear', 'grapefruit']
animal_products = ['milk', 'meat', 'butter', 'cheese']
print('Animal products are ', animal_products)
print('There are ', len(animal_products), 'in the list')

fruit1, fruit2, fruit3, *rest = fruit
print(fruit2) 
print(rest)

#all_fruit = fruit[0:8]
all_fruit = fruit[-7:-1]
twos = fruit[::2]
negative = fruit[::-1]
print(twos)
print(all_fruit)
print(negative)
