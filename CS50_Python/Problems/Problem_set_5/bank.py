def main():
    greeting = input("Greeting: ").strip()
    result = value(greeting)
    print(f"{result}$")


def value(greeting):
    if greeting.find("Hello")!=-1 or greeting.find("hello")!=-1:
        money = 0
    elif greeting.find("H") == 0 or greeting.find("h") == 0 :
        money = 20
    else:
        money = 100
    return money


if __name__ == "__main__":
    main()
