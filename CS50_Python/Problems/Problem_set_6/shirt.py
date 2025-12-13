import sys
import os
from PIL import Image, ImageOps
def main():
    try:
        if len(sys.argv)<3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>3:
            sys.exit("Too many command-line arguments")
        else:
                split1=sys.argv[1].split(os.extsep)
                ext1=split1[1].lower()
                split2=sys.argv[2].split(os.extsep)
                ext2=split2[1].lower()
                if ext1!="jpg" and ext1!="jpeg" and ext1!="png":
                    sys.exit("Invalid input")            
                elif  ext2!="jpg" and ext2!="jpeg" and ext2!="png":
                    sys.exit("Invalid output")
                elif ext1!=ext2:
                    sys.exit("Input and output have different extensions")
        with Image.open("shirt.png") as shirt, Image.open(f"{sys.argv[1]}") as img:
            size = shirt.size
            img=ImageOps.fit(img,size)
            img.paste(shirt,shirt)
            img.save(sys.argv[2])    
    except FileNotFoundError:
        sys.exit("Input does not exist")

main()