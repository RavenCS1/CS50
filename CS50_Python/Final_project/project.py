from pytube import YouTube
import csv
import sys
from pyfiglet import Figlet
from tabulate import tabulate
import os
import re
import os.path
import unicodecsv 

def main():
    exit=0
    print(welcome(),end="")
    print(starting_menu())
    while True:
        name=input("What is the name of a file with your playlist?: (.csv extension) ").strip()
        if validate_name(name)==False:
            print("You chose invalid name for your file! Please try again.")
        else:
            break
    while True:
        action=input("Action: ").strip().lower()
        if validate_action(action)==False:
            print("You chose an invalid operator! There is no such action. Input valid operator.")
            continue
        if action=="view":
            action_view(name)
            continue
        elif action=="find":
            action_find(name)
            continue
        elif action=="add":
            action_add(name)
            continue
        elif action=="change":
            name=action_change(name)
            continue
        elif action=="create":
            action_create(name)
            continue
        elif action=="remove":
            action_remove(name)
            continue
        elif action=="clear":
            action_clear(name)
            continue
        elif action=="delete":
            action_delete(name)
            continue
        else:
            action_exit()

def welcome():
    nameFront="digital"
    figlet = Figlet()
    figlet.setFont(font=nameFront)
    text = "What would you like to do?"
    return f"{figlet.renderText(text)}"

def starting_menu():
    with open(f"starting_menu.csv", "r") as table:
        reader=csv.reader(table)
        return tabulate(reader, headers="firstrow",tablefmt="grid")

def validate_action(action):
    list_of_action=["view","find","add","remove","exit","clear","change", "delete","create"]
    if action not in list_of_action:
        return False
    else:
        return True

def validate_url(url):
    format=r"^https?://(www\.)?youtube.com/.+?$"
    if re.search(format,url)==None:
        return False
    else:
        return True

def validate_name(name):
    format=r"^.*?\.csv$"
    if re.search(format,name)==None:
        return False
    else:
        return True

def set_global_exit():
    global exit
    exit=1

def action_view(name):
    if not os.path.isfile(f"{name}"):
        print("File with such name does not exist! Nothing can be done.")
        return
    with open(f"{name}", "rt", encoding='utf-8') as file:
        if os.path.getsize(f"{name}")==0:
            print("Your playlist is empty at the moment. Add some songs to see results.")
            return
        else:
            reader=csv.reader(file)
            print(tabulate(reader, headers="firstrow",tablefmt="grid"))
            return

def action_find(name):
    if not os.path.isfile(f"{name}"):
        print("File with such name does not exist! Nothing can be done.")
        return
    with open(f"{name}", encoding="utf-8") as f:
        lines=sum(1 for line in f)
    with open(f"{name}", "a+",newline="") as file:
        if os.path.getsize(f"{name}")==0 or lines==1:
            print("There are no songs in this file, therefore nothing can be found.")
            return
    with open(f"{name}", "ab+") as file:
        author=input("What is the name of the author whose song you would like to find on your playlist?: ") 
        title=input("What is the title of that particular song?: ") 
        reader=unicodecsv.reader(file, encoding='utf-8')
        file.seek(0)
        for row in reader:
            oldid,oldauthor,oldtitle,oldurl=row
            if oldauthor==author and oldtitle==title:
                print(f"URL address of that song is: {oldurl}")
                return
        print("It looks like the song you are looking for is not on your playlist.")
        return
    
def action_add(name):
    if not os.path.isfile(f"{name}"):
        print("File with such name does not exist! Nothing can be done.")
        return
    url=input("What is the url youtube address of the song which you would like to add?: ")
    if validate_url(url)==False:
        print("Your url address is incorrect! Please try once again.")
        return
    with open(f"{name}", "a+",newline="") as file:
        if os.path.getsize(f"{name}")==0:
            writer=csv.DictWriter(file, fieldnames=["id", "author", "title","url"])
            writer.writeheader()
    with open(f"{name}", encoding="utf-8") as f:
        lines=sum(1 for line in f) 
    with open(f"{name}", "ab+") as file:
        id=0
        reader=unicodecsv.reader(file, encoding='utf-8')
        yt=YouTube(url)
        title=yt.title
        author=yt.author
        if lines!=1:
            file.seek(0)
            for row in reader:
                id,oldauthor,oldtitle,oldurl=row
                if oldauthor==author and oldtitle==title:
                    print("You already have that song in your playlist.")
                    set_global_exit()
                    return  
        global exit
        if exit==1:
            exit-=1
            return
        id=int(id)      
        data=[id+1,author,title,url]
        writer=unicodecsv.writer(file,encoding='utf-8')
        writer.writerow(data)
        return

def action_change(name):
    while True:
        newname=input("What is the name of a file with your playlist?: (.csv extension) ").strip()
        if validate_name(newname)==False:
            print("You chose invalid name for your file! Please try again.")
        else:
            break
    return newname

def action_create(name):
    if not os.path.isfile(f"{name}"):
        open(f"{name}", "w", newline="") 
        print("File with a given name has been created.")
        return
    else:
        print("File with such name already exists! New file with the same name cannot be created.")
        return
    
def action_remove(name):
    if not os.path.isfile(f"{name}"):
        print("File with such name does not exist! Nothing can be done.")
        return
    with open(f"{name}", encoding="utf-8") as f:
        lines=sum(1 for line in f)
    with open(f"{name}", "a+",newline="") as file:
        if os.path.getsize(f"{name}")==0 or lines==1:
            print("There are no songs to be removed!")
            return
    with open(f"{name}", "ab+") as file:
        author=input("What is the name of the author whose song you would like to remove from your playlist?: ") 
        title=input("What is the title of that particular song?: ") 
        reader=unicodecsv.reader(file, encoding='utf-8')
        data=[]
        file.seek(0)
        for row in reader:
            oldid,oldauthor,oldtitle,oldurl=row
            check=oldauthor+oldtitle
            condition=author+title
            if check!=condition:
                    plot=[oldid,oldauthor,oldtitle,oldurl]
                    data.append(plot)
    with open(f"{name}", encoding="utf-8") as f:
        lines=sum(1 for line in f) 
    with open(f"{name}", "wb+") as file:
        lines-=1
        counter=0
        id=1
        writer=unicodecsv.writer(file,encoding='utf-8')
        for _ in range(lines):
            if counter==0:
                oldid,oldauthor,oldtitle,oldurl=data[_]
                copy=[oldid,oldauthor,oldtitle,oldurl]
                writer.writerow(copy)
                counter+=1
            else:
                oldid,oldauthor,oldtitle,oldurl=data[_]    
                copy=[id,oldauthor,oldtitle,oldurl]
                id+=1
                writer.writerow(copy)
        return

def action_clear(name):
    if not os.path.isfile(f"{name}"):
        print("File with such name does not exist! Nothing can be done.")
        return
    with open(f"{name}", encoding="utf-8") as f:
        lines=sum(1 for line in f) 
    if os.path.getsize(f"{name}")==0 or lines==1:
        print("There are no songs in this file, therefore nothing can be done.")
        return
    else:
        answer=input("Are you sure that you want to continue?: (yes/no) ").strip().lower()
        if answer=="yes":
            open(f"{name}", "w", newline="")  
            print("File has been cleared!")
        elif answer=="no":
            print("Nothing has been done.")
        else:
            print("You chose invalid option! Please try once again.")
        return

def action_delete(name):
    if not os.path.isfile(f"{name}"):
        print("File with such name does not exist! It cannot be deleted.")
        return
    else:
        answer=input("Are you sure that you want to continue?: (yes/no) ").strip().lower()
        if answer=="yes":
            file_name=f"{name}"
            os.remove(file_name)
            print(f"{file_name} has been deleted.")
        elif answer=="no":
            print("Nothing has been done.")
        else:
            print("You chose invalid option! Please try once again.")
        return

def action_exit():
    sys.exit()  

if __name__ == "__main__":
    main()