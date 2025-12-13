def main():
    while True:
        try:
            x=int(input("x: "))
            break
        except ValueError:
            continue
    while True:
        try:
            y=int(input("y: "))
            break
        except ValueError:
            continue
    print(f"{(x/y):.50f}")

if __name__=="__main__":
    main()