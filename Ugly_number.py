def u(n):
    t=[2,3,5]
    for i in t:
        while n%i==0:
            n=n/i
    return n==1
n=int(input())
if u(n)==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")