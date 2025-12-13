def main():
    fun=input("camelCase: ").strip()
    position=[]
    numbers=[]
    list=[]
    for letter in fun:
       if letter.isupper():
            position.append(letter)
    for change in range(len(position)):
        numbers.append(fun.find(position[change]))
    for _ in range(len(fun)):
        list.append(fun[_])
    for nwm in range(len(position)):
        list.remove(position[nwm])
        list.insert(numbers[nwm],f"""_{position[nwm].lower()}""")
    x=""
    for final in range(len(list)):
        x=x+list[final]
    print("snake_case: "+x)
main()

