largestPoli = 909

def isPolindrome(num):
    num = str(num)
    if num ==  num[::-1]:
        return True
    else:
        return False

for a in range(100,999):
    for b in range(a,999):
        if isPolindrome(a*b) and a*b > largestPoli:
            largestPoli = a *b
print(largestPoli)