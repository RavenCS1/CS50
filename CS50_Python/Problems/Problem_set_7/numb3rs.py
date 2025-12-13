import re

def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))
    

def validate(ip):
    try:
        format = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
        match = re.search(format, ip)
        if (
            0<=int(match.group(1))<256 and
            0<=int(match.group(2))<256 and
            0<=int(match.group(3))<256 and
            0<=int(match.group(4))<256
        ):
            return True
        else:
            return False
    except AttributeError:
            return False

if __name__ == "__main__":
    main()
