greeting=input("Greeting: ").strip().capitalize()
if greeting=="Hello":
    print("0$")
elif greeting.find("H")==0:
    print("20$")
else:
    print("100$")