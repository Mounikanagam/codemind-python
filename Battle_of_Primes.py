def p(u):
    f=0
    for i in range(1,u+1):
        if u%i==0:
            f=f+1
    if f==2:
        return True 
    else:
        return False
def nx(u):
    while p(u)==False:
        u=u+1
    return u
n=int(input())
m=int(input())
a=n+m
pa=nx(a)
if p(a)==True:
    pa=nx(a+1)
    print(pa-a)
else:
    print(pa-a)