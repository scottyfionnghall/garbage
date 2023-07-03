# PROBLEM 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2 , the first 10 terms will be:
#
#               1,2,3,5,8,13,21,34,55,89
#
# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the sum of the even-valued terms.



fib = [1,1]
even_fib = []
i = 0
sum = 0
while fib[-1] <= 4_000_000:
    fib.append(fib[i]+fib[i+1])
    if fib[-1] % 2 == 0:
        even_fib.append(fib[-1])
    i +=1
for i in even_fib:
    sum += i
print(sum)