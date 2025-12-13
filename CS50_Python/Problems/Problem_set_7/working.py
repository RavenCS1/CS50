import re
import sys


def main():
    hours=input("Hours: ").strip()
    validate=convert(hours)
    print(validate)

def convert(hours):
    try:
        format=r"^(?P<hour1>\d{1,2})(?:\:(?P<minutes1>\d{2}))? (?P<time1>AM|PM) to (?P<hour2>\d{1,2})(?:\:(?P<minutes2>\d{2}))? (?P<time2>AM|PM)$"    
        matches=re.search(format,hours)
        hour1=int(matches.group("hour1"))
        hour2=int(matches.group("hour2"))
        try:
            minutes1=int(matches.group("minutes1"))
        except TypeError:
            minutes1=0
        try:
            minutes2=int(matches.group("minutes2"))
        except TypeError:
            minutes2=0
        time1=matches.group("time1")
        time2=matches.group("time2")
        if ((0<hour1<13 and 0<=minutes1<=59) and 
            (0<hour2<13 and 0<=minutes2<=59)):
            if hour1==12 and hour2==12:
                validate=f"{(hour2-12):02}:{minutes2:02} to {(hour1):02}:{minutes1:02}"          
                return validate
            if time1=="AM" and time2=="AM":
                validate=f"{hour1:02}:{minutes1:02} to {hour2:02}:{minutes2:02}"
            elif time1=="AM" and time2=="PM":
                validate=f"{hour1:02}:{minutes1:02} to {(hour2+12):02}:{minutes2:02}"
            elif time1=="PM" and time2=="AM":
                validate=f"{(hour1+12):02}:{minutes1:02} to {hour2:02}:{minutes2:02}"
            elif time1=="PM" and time2=="PM":
                validate=f"{(hour1+12):02}:{minutes1:02} to {(hour2+12):02}:{minutes2:02}"          
            return validate
        else:
            raise ValueError
    except AttributeError:
        raise ValueError

if __name__ == "__main__":
    main()