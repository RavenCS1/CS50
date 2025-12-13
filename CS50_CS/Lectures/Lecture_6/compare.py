def main():
    while True:
        try:
            x = int(input("x: "))
            break
        except ValueError:
            continue
    while True:
        try:
            y = int(input("y: "))
            break
        except ValueError:
            continue
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")


if __name__ == "__main__":
    main()
