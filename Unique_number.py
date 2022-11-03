n=int(input())
n=str(n)
n=list(n)
m=[]
for i in n:
    if i not in m:
        m.append(i)
if n==m:
    print("Unique Number")
else:
    print("Not Unique Number")