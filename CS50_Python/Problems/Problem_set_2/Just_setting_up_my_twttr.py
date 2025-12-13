def main():
    text=input("Input: ").strip()
    position=[]
    numbers=[]
    list=[]
    for letter in text:
       if (letter=="A" or letter=="a" or
           letter=="E" or letter=="e" or
           letter=="I" or letter=="i" or
           letter=="O" or letter=="o" or 
           letter=="U" or letter=="u"):
                
            position.append(letter)
    for number in range(len(position)):
        numbers.append(text.find(position[number]))
    for _ in range(len(text)):
        list.append(text[_])
    for next in range(len(position)):
        list.remove(position[next])
        list.insert(numbers[next],"")
    x=""
    for final in range(len(list)):
        x=x+list[final]
    print("Output: "+x)
main()
