import emoji


def main():
    text = input("Input: ")
    print(emoji.emojize(f"Output: {text}", language="alias"))


main()
