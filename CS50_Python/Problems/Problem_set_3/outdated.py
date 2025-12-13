def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        try:
            date = input("Date: ").strip()
            if date.rfind("/") == -1 and date.rfind(",") != -1:
                list = date.split(" ")
                day = list[1]
                if len(day) == 3:
                    correct = day[0:2]
                else:
                    correct = day[0:1]
                list.insert(1, correct)
                list.remove(list[2])
                if int(list[1]) > 31:
                    continue
                for _ in range(len(months)):
                    if list[0].title() == months[_]:
                        list.insert(0, _ + 1)
                        list.remove(list[1])
                        return print(
                            f"{int(list[2]):02}"
                            "-"
                            f"{int(list[0]):02}"
                            "-"
                            f"{int(list[1]):02}"
                        )
                continue
            else:
                list = date.split("/")
                if int(list[0]) > 12 or int(list[1]) > 31:
                    continue
                return print(
                    f"{int(list[2]):02}"
                    "-"
                    f"{int(list[0]):02}"
                    "-"
                    f"{int(list[1]):02}"
                )
        except ValueError:
            pass


main()
