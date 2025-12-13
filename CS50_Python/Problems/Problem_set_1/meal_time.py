def main():
    time=input("What time is it? ").strip()
    time=convert(time)
    if time>=7 and time<=8:
        print("breakfast time")
    elif time>=12 and time<=13:
        print("lunch time") 
    elif time>=18 and time<=19:
        print("dinner time")
        

def convert(time):
    if len(time)==5:
        hours=float(time[0:2])
        minute=float(time[3:5])*1/60
    else:
        hours=float(time[0])
        minute=float(time[2:4])*1/60
    time=hours+minute
    return time



if __name__ == "__main__":
    main()