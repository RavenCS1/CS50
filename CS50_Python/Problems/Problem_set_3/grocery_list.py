def main():
    shopping=[]
    while True:
        try:
            item=input().strip().lower()
            shopping.append(item)
            continue
        except EOFError:
            break
        except KeyError:
            pass
    name=sorted(shopping)
    _=0
    while _<=(len(name)-1):
        counter=1
        key=name[_]
        if len(name)==0:
            quit()
        elif len(name)==1:
                return print(f"{counter} {key.upper()}")
        else:
            rest=_+1
            while rest<=(len(name)-1):
                if key==name[rest]:
                    counter+=1
                else:
                    break
                rest=rest+1
        print(f"{counter} {key.upper()}")
        if counter>1:
            _=_+counter
        else:
            _=_+1
        
    
    
main()
