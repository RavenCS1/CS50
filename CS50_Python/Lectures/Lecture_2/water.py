from soil import sample


def main():
    moisture()=sample()
    days=0
    print(f'Day {days+1}: Moisture is {moisture}%')
    while moisture>20:
        moisture=sample()
        days+=1
        print(f'Day {days+1}: Moisture is {moisture}%')
    print("Time to water!")

    

main()