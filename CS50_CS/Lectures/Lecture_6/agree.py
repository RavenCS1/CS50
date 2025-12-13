def main():
    s=input("Do you agree? ").lower()
    if s in ["y","yes"]:
        print("Agreed")
    elif s in ["n","no"]:
        print("Not agreed")


if __name__=="__main__":
    main()