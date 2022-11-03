n=int(input())
s=5*n*n+4
q=5*n*n-4
t=int(s**0.5)
m=int(q**0.5)
if s==t*t or q==m*m:
    print("True")
else:
    print("False")