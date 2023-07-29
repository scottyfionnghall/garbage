def rps(p1, p2):
    rules = {'scissors':'paper','paper':'rock','rock':'scissors'}
    if rules[p1] == p2:
        return 'Player 1 won!'
    elif rules[p2] == p1:
        return 'Player 2 won!'
    else:
        return 'Draw!'