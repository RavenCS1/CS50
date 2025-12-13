from datetime import date
from datetime import timedelta
import sys
import inflect

def validate(start):
    try:
        list=start.split("-")
        year=int(list[0])
        month=int(list[1])
        day=int(list[2])
        start=date(year, month,day)
    except ValueError:
        sys.exit("Invalid date")
    except IndexError:
        sys.exit("Invalid date")
    return start

def counting(birth):
    today=date.today()
    minutes=date.__sub__(today,birth)
    minutes=round(minutes.total_seconds()/60)
    return minutes

def main():
    start=input("Date of Birth: ")
    birth=validate(start)
    minutes=counting(birth)
    p=inflect.engine()
    print(f"{p.number_to_words(minutes, andword="").capitalize()} minutes")


if __name__ == "__main__":
    main()
