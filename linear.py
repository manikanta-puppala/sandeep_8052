a=int(input("Enter Length of the list"))
l=[]
for i in range(a):
    l=l+[int(input("Enter any number"))]
print(l)
key=int(input("Enter any number to search"))
flag=0
for i in range(a):
    if l[i]==key:
        print("Element is found at",i)
        flag=1
        break
if flag==0:
    print("ELement is not found in the list")
