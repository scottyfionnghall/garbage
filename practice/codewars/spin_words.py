def spin_words(sentence):
    sentence = sentence.split(' ')
    result = []
    for word in sentence:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)
print(spin_words("Hey fellow warriors"))