import sys

def main():
    try:
        if len(sys.argv)<2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].find(".py")==-1:
            sys.exit("Not a Python file")
        with open(f"{sys.argv[1]}", "r") as file:
            lines=file.readlines()
            counter=0
            for _ in range(len(lines)):
               if lines[_].strip().find("#")==0:
                counter=counter
               elif lines[_].strip().count(" ")==len(lines[_].strip()):
                counter=counter
               else:
                counter+=1
            print(counter)
    except FileNotFoundError:
        sys.exit("File does not exist")

main()