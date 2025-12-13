def main():
    menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total_cost=0.00
    while True:
        try:     
            item=input("Item: ").strip().title()
            if item in menu.keys():
                money=round(float(menu[str(item)]),2)
                total_cost=total_cost+money
                print("Total ""{:.2f}".format(total_cost))
                continue
        except KeyError:
            pass
        except EOFError:
            quit()
main()

















main()