def main():
    while True:
        try:
            height = int(input("Height: "))
            if height < 1 or height > 8:
                continue
            break
        except ValueError:
            pass
    counter = height
    for row in range(height):
        print(f"{' '*(counter-1)}{'#'*(row+1)}  {'#'*(row+1)}")
        counter -= 1


if __name__ == "__main__":
    main()
