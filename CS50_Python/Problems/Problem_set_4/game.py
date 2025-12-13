import random


def main():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        else:
            if int(n) > 0:
                break
    list = []
    x = 1
    while x <= int(n):
        list.append(x)
        x += 1
    number = random.choice(list)
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        else:
            if guess > int(number):
                print("Too large!")
            elif guess < int(number):
                print("Too small!")
            else:
                print("Just right!")
                quit()


main()
