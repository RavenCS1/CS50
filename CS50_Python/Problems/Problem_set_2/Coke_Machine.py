def main():
   due=50
   print("Amount Due: " + str(due))
   while due>0:
    money=int(input("Insert Coin: "))
    if money==25 or money==10 or money==5:
        due=due-money
        if due==0:
            print("Change Owed: " + str(due))
        elif due<0:
            print("Change Owed: " + str(due*(-1)))
        else:
            print("Amount Due: " + str(due))
    else:
        print("Amount Due: " + str(due))

main()