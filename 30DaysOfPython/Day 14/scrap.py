def double_it(num):
    doubled= (num*2)
    return doubled
print(double_it(10))

def is_long_word(word):
    default = 5
    if len(word) > default:
        return(True)
    else:
        return(False)
    
is_long_word('Sonic')
is_long_word('Piccolo')

def multiply_two(x, y):
    product = x*y
    return product
print(multiply_two(9, 5))
        