def main():
    text = input("Input: ").strip()
    word = shorten(text)
    print("Output: " + word)


def shorten(word):
    position = []
    numbers = []
    list = []
    for letter in word:
        if (
            letter == "A"
            or letter == "a"
            or letter == "E"
            or letter == "e"
            or letter == "I"
            or letter == "i"
            or letter == "O"
            or letter == "o"
            or letter == "U"
            or letter == "u"
        ):

            position.append(letter)
    for number in range(len(position)):
        numbers.append(word.find(position[number]))
    for _ in range(len(word)):
        list.append(word[_])
    for next in range(len(position)):
        list.remove(position[next])
        list.insert(numbers[next], "")
    text = ""
    for final in range(len(list)):
        text = text + list[final]
    return text


if __name__ == "__main__":
    main()
