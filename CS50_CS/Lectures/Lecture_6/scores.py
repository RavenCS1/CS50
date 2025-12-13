scores=[]
for _ in range(3):
    while True:
        try:
            score=int(input("Score: "))
            scores=scores+[score]
            break
        except ValueError:
            pass
average=sum(scores)/len(scores)
print(f"Average: {average}")
print(scores)
