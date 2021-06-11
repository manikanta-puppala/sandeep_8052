# Find the number Even and Odd digits in a given input.

n=int(input("Enter any Number"))
a=str(n)
even=0
odd=0
for i in a:
    b=int(i)
    if b%2==0:
        even+=1
    else:
        odd+=1
print("No of even digits", even)
print("No of odd digits", odd)