import re
import sys


def main():
    url = input("HTML: ")
    yt = parse(url)
    print(yt)


def parse(url):
    format = r".+\"https?://(?:www\.)?youtube.com/embed/(.+?)\".+"
    try:
        match = re.search(format, url)
        suffix=f"https://youtu.be/{match.group(1)}"
        return suffix
    except AttributeError:
        print("None")
        sys.exit()


if __name__ == "__main__":
    main()
