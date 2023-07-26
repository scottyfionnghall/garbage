
# https://edabit.com/challenge/YfoKQWNeYETb9PYpw

items = {
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}

def calculate_profit(items):
    cost_price = items['cost_price']
    sell_price = items['sell_price']
    inventory = items['inventory']
    profit = sell_price *inventory - cost_price * inventory
    return(profit)

print(calculate_profit(items))