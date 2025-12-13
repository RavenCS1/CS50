def main():
    percent=convert_and_check()
    if percent<=1:
        print("E")
    elif percent>=99:
        print("F")
    else:
        print(f"{percent}%")




def convert_and_check():
    while True:
        try:
            amount=input("Fraction: ").strip().split("/")
            x=int(amount[0])
            y=int(amount[1])
            if x>y:
                continue
            percent=round(x*100/y,)
            return percent
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        
        
            

                      

main()
