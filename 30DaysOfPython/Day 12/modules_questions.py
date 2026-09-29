import random
import string
# Exercises: Day 12
# Exercises: Level 1
#1 Write a function which generates a six digit/character random_user_id.
#   print(random_user_id()random_user_id()) 
#   '1ee33d'
def random_user_id():
    char = string.ascii_letters + string.digits
    random_char = random.choices(char,k=6)
    random_id = "".join(random_char)
    return random_id
print(random_user_id())

#2 Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
def user_id_gen_by_user():
    num_char = int(input('Enter number of characters: '))
    num_ids = int(input('Enter number of IDs to generate: '))

    char = string.ascii_letters + string.digits
    random_char = random.choices(char,k=num_char)
    for _ in range(num_ids):
        random_char = random.choices(char, k=num_char)
        random_id = "".join(random_char)
        print(random_id)
user_id_gen_by_user()

#3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())


# Exercises: Level 2
#1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(count):
    colors = []
    hex_pool = "0123456789abcdef" 
    for _ in range(count):
        random_hex = "".join(random.choices(hex_pool, k=6))
        colors.append(f"#{random_hex}")
    return colors
list_of_hexa_colors(3)

#2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(count):
    colors=[]
    for _ in range(count):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r},{g},{b})")
    return colors
print(list_of_rgb_colors(120))

#3 Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
def generate_colors(color_type, count):
    if color_type == 'hex':
        return list_of_hexa_colors(count)
    elif color_type == 'rgb':
        return(list_of_rgb_colors(count))
    else:
        return "Invalid color type! Choose 'hex' or 'rgb'."

print(generate_colors('hex',6))

# Exercises: Level 3
#1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    shuffle = random.sample(lst, len(lst))
    return shuffle

print(shuffle_list(["Goku", "Shockwave", "Gohan", "Piccolo", "Brawl", "Mindwipe"]))

#2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_ran_nums():
    lst =[]
    while len(lst) < 7:
        num = random.randint(0,9)
        if num not in lst:
            lst.append(num)
    return lst
print(seven_ran_nums())


