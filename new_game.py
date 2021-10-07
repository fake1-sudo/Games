answer = 58

print("Please guess a number between 0 - 100 : ")
guess =int(input())

if guess < answer:
    print("Please Guess Higher.")
    guess = int(input())
    if guess == answer:
        print("Well Done.")
        print("Thanks For Playing.")
    else:
        print("Sorry, You Have Not Guessed Correctly.")
elif guess > answer:
    print("Please Guess Lower.")
    guess = int(input())
    if guess == answer:
        print("Well Done.")
        print("Thanks For Playing.")
    else:
        print("Sorry, You Have Not Guessed Correctly.")
else:
    print("You Win.")
    print("Thanks For Playing.")
    
