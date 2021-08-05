a=[]
b=int(input("Enter the size of the stack: "))
#Stack Means Last in First Out
#Using List we can create stack by pushing Element at last and popping element at last
#Here we will take length of the stack as an input from the user 
#Stack Overflow Error: When we try to insert an element after the stack is full
#Stack Underflow Error: When we try to delete an element if the stack is empty

c=int(input("If you want to continue Enter 1 or else Enter 0 : "))

while c!=0:
    d=int(input("For Pushing Enter 1, For Popping Enter 0 : "))
    if d==1:
        if len(a)<=b:
            a=a+[input("Enter an element: ")]
            print("Current Stack is: ",a)
        else:
            print("Stack Overflow")
    elif d==0:
        if len(a)>0:
            print(a.pop())
            print("Current Stack is: ",a)
        else:
            print("Stack Underflow")
    c=int(input("If you want to continue Enter 1 or else Enter 0: "))