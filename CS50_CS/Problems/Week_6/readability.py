def main():
    text=input("Text: ")
    letters=0
    words=1
    sentences=0
    for sign in text:
        if sign.isalpha()==True:
            letters+=1
        elif sign==" ":
            words+=1
        elif sign=="!" or sign=="." or sign=="?":
            sentences+=1
    L=(letters*100)/words
    S=(sentences*100)/words
    index=round(0.0588*L-0.296*S-15.8)
    if index<1:
        return print("Before Grade 1")
    elif index>16:
        print("Grade 16")
    else:
        print(f"Grade {index}")
    

if __name__=="__main__":
    main()