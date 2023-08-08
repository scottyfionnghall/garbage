def duplicate_encode(word):
    word = word.lower()
    answer = ''
    for letter in word:
        if word.count(letter) > 1:
            answer += ')'
        else:
            answer += '('
    return(answer)

print(duplicate_encode('oDpDzI OpvHuNz'))