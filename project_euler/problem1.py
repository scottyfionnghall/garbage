# PROBLEM 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3,5,6 and 9. The sum of these multiplse is 23.
# Find the sum of all multiples of 3 or 5 below 1000.

numbers = list(range(1,1000))
sum_of_numbers = 0
for i in numbers:
    if i % 3 == 0 or i % 5 == 0:
        sum_of_numbers += i
print(sum_of_numbers)