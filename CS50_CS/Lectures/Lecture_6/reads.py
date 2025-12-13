import csv
books=[]

with open('books.csv',"r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        books.append(row)

for book in books:
    print(f"{book["author"]} wrote {book["title"]}.")
    