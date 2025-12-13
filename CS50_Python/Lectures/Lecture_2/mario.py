def main():
    print_square(3)


def print_column(height):
    print("#\n" * height, end="")


def print_row(widht):
    print("#" * widht)


def print_square(size):
    for i in range(size):
        print_row(size)



main()
