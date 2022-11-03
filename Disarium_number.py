n=int(input())
m=str(n)
l=len(m)
temp=n
s=0
r=0
while temp>0:
    r=temp%10
    s=s+int(r**l)
    temp=temp//10
    l=l-1
if s==n:
    print("True")
else:
    print("False")