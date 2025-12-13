def main():
    names = []
    while True:
        try:
            name = input("Name: ").strip().title()
            names.append(name)
            continue
        except EOFError:
            break
        except KeyError:
            pass
    standard = "Adieu, adieu, to "
    x = 0
    for _ in range(len(names)):
        if x == 0:
            goodbye = f"{standard}{names[_]}"
        elif x == 1:
            concatinating = " and "
            goodbye = goodbye + concatinating + str(names[_])
        elif x == 2:
            goodbye = goodbye.replace(concatinating, ", ")
            goodbye = goodbye + "," + concatinating + str(names[_])
        else:
            place = goodbye.rfind(",")
            goodbye = goodbye[0:place] + goodbye[place + 1 : len(goodbye) + 1]
            goodbye = goodbye.replace(concatinating, ", ")
            goodbye = goodbye + "," + concatinating + str(names[_])
        x += 1
    print(goodbye)


main()
