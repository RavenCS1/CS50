import sys

def main():
    if len(sys.argv)==2:
        print(f"Hello, {sys.argv[1]}")
    else:
        print("Hello, world")

if __name__=="__main__":
    main()