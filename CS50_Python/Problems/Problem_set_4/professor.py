import random


def main():
    level = get_level()
    list = generate_integer(level)
    score = 0
    for equation in range(len(list)):
        counter = 0
        momentum = list[equation].split("+")
        x = int(momentum[0])
        y = int(momentum[1])
        solution = x + y
        while True:
            try:
                prompt = int(input(f"{list[equation]} = "))
                if solution == prompt:
                    score += 1
                    break
                else:
                    print("EEE")
                    counter += 1
                    if counter == 3:
                        print(f"{list[equation]} = {solution}")
                        break
                    continue
            except ValueError:
                print("EEE")
                counter += 1
                if counter == 3:
                    print(f"{list[equation]} = {solution}")
                    break
                continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n != 1 and n != 2 and n != 3:
                continue
            else:
                return n
        except ValueError:
            pass


def generate_integer(level):
    list = []
    for _ in range(10):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            equation = f"{x} + {y}"
            list.append(equation)

        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            equation = f"{x} + {y}"
            list.append(equation)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            equation = f"{x} + {y}"
            list.append(equation)
    return list


if __name__ == "__main__":
    main()
