def main():
    file=input("File name: ").lower().strip()
    if '.jpeg' in file or '.jpg' in file:
        extension='jpeg'
    else:
        extension=file[(len(file)-3):len(file)]
    if ".gif" in file or".png" in file:
        print(f"image/{extension}")
    elif ".jpg" in file or ".jpeg" in file:
        print(f"image/{extension}")
    elif ".pdf" in file:
            print(f"application/{extension}")
    elif ".txt" in file:
        print("text/plain")
    elif ".zip" in file:
        print(f"application/{extension}")
    else:
        print("application/octet-stream")

main()
