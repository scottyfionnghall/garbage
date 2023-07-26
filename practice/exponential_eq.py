
# https://edabit.com/challenge/MhQbon8XzsG3wJHdP

import math 

def solve_for_exp(a,b):
    x = math.log10(b)/math.log10(a)
    return(x)

a_b = input('Enter a and b:\n')
a_b = a_b.split(',')
a_b = [int(num) for num in a_b]

print(solve_for_exp(a_b[0],a_b[1]))