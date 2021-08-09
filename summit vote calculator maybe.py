import math
summitMoney = int(input())
dollarVote = (summitMoney*2)

bonus25 = (summitMoney/50)
math.floor(bonus25)

bonus50 = (summitMoney/100)
math.floor(bonus50)

print(dollarVote + (bonus25*25)+(bonus50*50))