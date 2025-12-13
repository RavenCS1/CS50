def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    letters = []
    for _ in range(len(plate)):
        letters.append(plate[_])
    if len(plate) >= 2 and len(plate) <= 6:
        if letters[0].isalpha() and letters[1].isalpha():
            if (
                plate.rfind(" ") == -1
                and plate.rfind(",") == -1
                and plate.rfind(".") == -1
            ):
                x = 0
                for rest in range(len(plate) - 2):
                    if letters[rest + 2].isnumeric():
                        if x == 0:
                            if letters[rest + 2] == "0":
                                return False
                        x = x + 1
                    if x > 0 and letters[rest + 2].isalpha():
                        return False
                return True
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
