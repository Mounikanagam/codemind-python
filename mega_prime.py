def p(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f=f+1
    if f==2:
        return True 
    else:
        return False
a=int(input())
m=True
if p(a)==True:
    while a>0:
        r=a%10
        if p(r)==False:
            m=False
            break
        a=a//10
    if m==True:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
    