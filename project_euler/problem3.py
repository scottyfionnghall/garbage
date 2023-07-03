# The prime factors of 13195 are 5,7,13 and 29
# What is the largest prime factor of the number 600851475143

from math import sqrt
number =  600851475143
last_factor = 0

if number % 2 == 0:
    last_factor = 2
    number = number/last_factor
else:
    last_factor = 3

max_factor = sqrt(number)
all_factors = []

while number > 1 and last_factor < max_factor:
    if number % last_factor == 0:
        all_factors.append(last_factor)
        number = number / last_factor
    last_factor += 2

if last_factor == 2:
    print(last_factor)
else:
    print(all_factors[-1])
