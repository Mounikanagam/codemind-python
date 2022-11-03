def p(n):
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
def pre(n):
    while p(n)==False:
        n=n-1
    return n
def nex(n):
    while p(n)==False:
        n=n+1
    return n
l=int(input())
a=pre(l)
b=nex(l)
if p(l)==True:
    print(pre(l-1),nex(l+1))
elif(l-a)<(b-l):
    print(a)
elif(l-a)>(b-l):
    print(b)
elif (l-a)==(b-l):
    print(a,b)