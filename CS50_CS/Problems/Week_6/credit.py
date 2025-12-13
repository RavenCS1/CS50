def main():
    number = input("Number: ")
    n = str(len(number))
    cards = ['13', '15', '16']
    master=['51','52','53','54','55']
    if n not in cards:
        return print("INVALID")
    if (number[0:2] == '34' or number[0:2] == '37') and validate(number) == True:
        return print("AMEX")
    elif number[0:2] in master and validate(number) == True:
        return print("MASTERCARD")
    elif number[0] == '4' and validate(number) == True:
        return print("VISA")
    else:
        return print("INVALID")


def validate(number):
    number=number[::-1]
    digits = []
    counter = 1
    for digit in number:
        if counter % 2 == 0:
            if int(digit)*2 >= 10:
                second = int(digit)*2 % 10
                first = 1
                digits.append(first)
                digits.append(second)
            else:
                digits.append(int(digit)*2)
        counter += 1
    odds = []
    counter = 1
    for digit in number:
        if counter % 2 == 1:
            odds.append(int(digit))
        counter += 1
    final = sum(digits)+sum(odds)
    if final % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
