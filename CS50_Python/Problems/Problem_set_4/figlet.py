from pyfiglet import Figlet
import sys
import random


def main():
    if len(sys.argv) == 3:
        font = sys.argv[1]
        nameFront = sys.argv[2]
        figlet = Figlet()
    elif len(sys.argv) == 1:
        figlet = Figlet()
        font = "-f"
        nameFront = random.choice(figlet.getFonts())
    else:
        sys.exit("Invalid usage")
    if font != "-f" and font != "--font":
        sys.exit("Invalid usage")
    x = figlet.getFonts()
    counter = 0
    for _ in range(len(x)):
        if nameFront == x[_]:
            counter += 1
    if counter == 0:
        sys.exit("Invalid usage")
    figlet.setFont(font=nameFront)
    text = input("Input: ")
    print(f"Output: {"\n"}{figlet.renderText(text)}")


main()
