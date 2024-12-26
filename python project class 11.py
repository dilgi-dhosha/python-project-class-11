import random
from countries import countries
from haversine import haversine

C=random.choice(list(countries.keys()))

print('''Welcome! In this game, there will be a random country that is chosen from the 195 countries and
it is your job to guess which country we have picked. If your guess is incorrect, we will provide you
with a hint in the form of the distance between the correct country and the the country you guessed.
If you are a bitch ass nigga that doesn't know his geography, then you type 'reveal' to reveal the
answer.''')
print()
YN = input("Ready to play?")
yn = YN.lower()
if yn == 'yes':
    while 1>0:
        n=0
        g = input("Enter your guess:")
        Guess = g.lower()
        if Guess in countries:
            if Guess == C:
                print("Good job nigga 😘😘😘")
                break
            else:
                d =  haversine(countries[C], countries[Guess])
                print("Not quite but try again, Your guess is",d,"km further from the actual country")
                print()
        elif Guess not in countries:
            if Guess == "reveal":
                print(C)
                break
            else:
                print("thats not a real country")
                print()
else:
    print("come back when you change your mind")
