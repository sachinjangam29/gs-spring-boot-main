import random

lives = 3
score = 0

# It will display the number of lives you have and the score you have earned

while lives > 0:
    number = random.randint(1,10)

    print("\n you have ",lives,2" lives and the score is ",score)
    print("\n Guess the number between 1 to 10")

    guess = int(input())
    if guess == number:
        print("Congratulations you have guessed it right")
        score +=1
    else:
        lives-=1


print("Game over!!!!")
