def solution(number):
    numbers = range(0,number)
    multiple = []
    for i in numbers:
        if i % 3 == 0 or i % 5 == 0:
            multiple.append(i)
    return(sum(multiple))

print(solution(10))