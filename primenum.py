i=int(input("Enter any number"))
j=int(input("Enter any number"))
p=i
while i<=p<=j:
    k=2
    a=0
    while k<p and a==0:
        if p%k==0:
            a=1
        k=k+1
    if a==0:
        print(p)
    p=p+1
20
