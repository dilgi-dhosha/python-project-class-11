import random
from countries import *
from haversine import haversine

C=random.choice(list(countries.keys()))

print('''In this game, a random country will be selected from the 195 recognized nations, and it will be your
task to guess which country has been chosen. If your guess is incorrect, a hint will be provided in
the form of the distance between the correct country and the one you guessed.

If you're unable to make a correct guess, you can type "reveal" to see the answer.''')
print()
YN = input("Ready to play?")
yn = YN.lower()
if yn == 'yes':
    n=0
    while 1>0:
        g = input("Enter your guess:")
        Guess = alias(g.lower())
        if Guess in countries:
            n=n+1
            if Guess == C:
                print("Good job, The correct country was", C)
                print("It took", n," attempts")
                break
            else:
                d =  haversine(countries[C], countries[Guess])
                print("Not quite but try again, Your guess is",d,"km further from the actual country")
                print()
        elif Guess not in countries:
            if Guess == "reveal":
                n=n+1
                print("The correct country was", C)
                print("It took", n," attempts")
                break
            else:
                print("thats not a real country")
                print()
else:
    print("come back when you change your mind")
