n=int(input())
a=abs(n)
rev=0
r=0
while a>0:
    r=a%10
    rev=rev*10+r
    a=a//10
if n>0:
    print(rev)
else:
    print(-rev)