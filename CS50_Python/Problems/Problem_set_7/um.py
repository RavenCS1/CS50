import re
import sys


def main():
    text=input("Text: ")
    number=count(text)
    print(number)


def count(text):
    format=r".*?\b(um|UM|Um|uM)\b.*?"
    matches=re.findall(format,text)
    number=len(matches)
    return number

if __name__ == "__main__":
    main()