def main():
    fraction = input("Fraction: ").strip()
    percentage = convert(fraction)
    final = gauge(percentage)
    print(final)

def convert(fraction):
    try:
        parts = fraction.split("/")
        x = int(parts[0])
        y = int(parts[1])
        percent = round(x * 100 / y)
        if x>y:
            raise ValueError
        return percent
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError
    
def gauge(percentage):
    if percentage <= 1:
        state = "E"
    elif percentage >= 99:
        state = "F"
    else:
        state = f"{percentage}%"
    return state


if __name__ == "__main__":
    main()
