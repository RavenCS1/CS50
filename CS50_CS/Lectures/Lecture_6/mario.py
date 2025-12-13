def main():
    while True:
        while True:
            try:
                n=int(input("Width: "))
                break
            except ValueError:
                pass
        if n>0:
            break

    print("?"*n, end="")
    print()



if __name__=="__main__":
    main()