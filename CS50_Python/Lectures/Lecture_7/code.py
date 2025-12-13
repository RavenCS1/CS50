import re

def main():
    code=input("Hexadecimal color code: ").strip()
    pattern=r"^(?P<hex>#[a-fA-F0-9]{6})$"
    match=re.search(pattern,code)
    if match:
        print(f"Valid. Matched with {match.group("hex")}")
    else:
        print("Invalid.")
    
main()