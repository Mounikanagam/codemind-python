a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    is_p=True
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            is_p=False
            break
    if is_p==True and n!=1:
        print(n)