from random import randint

while True:
    level = input("Level: ")
    try:
        level = int(level)
        number = randint(1,level)
    except TypeError:
        continue
    except ValueError:
        continue
    else:
        break

while True:
    guess = input("Guess: ")

    try:
        guess = int(guess)
        if guess == number:
            print("Just right!")
            break
        elif guess > number:
            print("Too large!")
            continue
        elif guess < number:
            print("Too small!")
            continue
    except:
        continue