def prime(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f=f+1
    if f==2:
        return True
    else:
        return False
def palin(n):
    s=0
    k=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if k==s:
        return True
    else:
        return False
def npalin(n):
    while palin(n)==False:
        n=n+1
    return n
def nppalin(n):
    while prime(npalin(n))==False:
        n=npalin(n+1)
    return n
x=int(input())
p=nppalin(x)
if prime(p)==True:
    p=nppalin(x+1)
    print(p)