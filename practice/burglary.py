
# https://edabit.com/challenge/2wQPKcSipXmK4idwD

items = { }

item = input('pet\'s name:\n')
item = item.lower()

if item in items.keys():
    print(f'{item.title()} is gone...')
else:
    print(f'{item.title()} is here!')