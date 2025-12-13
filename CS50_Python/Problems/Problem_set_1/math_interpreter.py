def main():
    values=input("Expression: ").split(" ")
    x=int(values[0])
    y=str(values[1])
    z=int(values[2])
    if y=="+":
        score=round(float(x+z),1)
        int(print(score))
    elif y=="-":
        score=round(float(x-z),1)
        int(print(score))
    elif y=="/":
        score=round(float(x/z),1)
        int(print(score))
    else:
        score=round(float(x*z),1)
        int(print(score))
main()