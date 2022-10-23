a,b=map(int,input().split())
for i in range(max(a,b),1 +(a*b)):
    if i%a==i%b==0:
        lcm=i
        break
print(lcm)