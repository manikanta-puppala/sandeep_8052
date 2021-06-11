n=int(input("Enter any number:- "))
a=0
b=1
flag=True
count=2
if n==1:
    print(0)
elif n==2:
    print(1)
else:
    while flag:
        count+=1
        c=a+b
        a=b
        b=c
        if n==count:
            flag=False
    print(c)
