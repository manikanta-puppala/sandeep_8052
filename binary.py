a=[]
b=int(input("Enter the length of the list"))
for i in range(b):
    a=a+[int(input("Enter a number: "))]
key=int(input("Enter any number to search"))
l=0
a.sort()
flag=0
h=(len(a)-1)
while (h-l)>1:
    mid=(l+h)//2
    if a[mid]==key:
        flag=1
        print("Element is found")
        break
    elif key>a[mid]:
        l=mid+1
    elif key<a[mid]:
        h=mid-1
if a[h]==key or a[l]==key:
    print("Element is found")
    flag=1

if flag==0:
    print("Element is not found in the list")


