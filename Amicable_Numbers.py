n1=int(input())
n2=int(input())
s=0
m=0
for i in range(1,n1):
    if n1%i==0:
        s+=i
for j in range(1,n2):
    if n2%j==0:
        m+=j
if n1==m and n2==s:
    print("Amicable")
else:
    print("Not Amicable")