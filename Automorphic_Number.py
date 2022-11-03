n=int(input())
a=n**2
b=len(str(n))
d=(10)**b
if a%d==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
