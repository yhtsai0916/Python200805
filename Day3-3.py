scr=[]
s=[]
i=avg

def x(total,n):
    j=total
    total=0
    for k in scr:
        j=j+k
    i=j/n
    return i

n=input("輸入人數:")
n=int(n)

for y in range(n):
    scores=input("輸入分數:")
    scores = int(scores)
    scr.append(scores)
    names=input("輸入名字:")
    s.append(names)
ans=x(total,n)
print(ans)




