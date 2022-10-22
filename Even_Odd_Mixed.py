n=int(input())
c=d=0
while n>0:
    r=n%10
    if r%2==0:
        c+=1
    elif r%2!=0:
        d+=1
    n=n//10
if d==0:
    print("Even")
elif c==0:
    print("Odd")
else:
    print("Mixed")