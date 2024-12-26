import random
from countries import countries
from haversine import haversine

C=random.choice(list(countries.keys()))


while 1>0:
    n=0
    g = input("Enter your guess:")
    Guess = g.lower()
    if Guess in countries:
        if Guess == C:
            print("Yay")
            break
        else:
            haversine(countries[C], countries[Guess])
    elif Guess not in countries:
        if Guess == "reveal":
            print(C)
            break
        else:
            print(":/")
            
