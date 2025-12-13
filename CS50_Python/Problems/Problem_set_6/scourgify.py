import sys
import csv
def main():
    try:
        if len(sys.argv)<3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>3:
            sys.exit("Too many command-line arguments")
        with open(f"{sys.argv[1]}", "r") as before, open(f"{sys.argv[2]}", "w",newline="") as after:
            create=[]
            reader=csv.DictReader(before)
            for row in reader:
                last,first=row["name"].replace(" ","").split(",")
                create.append([first,last,row["house"]])
            writer=csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for _ in range(len(create)):
               line=create[_]
               writer.writerow({"first": line[0], "last":line[1],"house":line[2]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

main()