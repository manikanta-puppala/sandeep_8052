a=[]
b=int(input("Enter the size of the Queue: "))
#Queue Means First in First Out
#Using List we can create Queue by pushing Element at last and popping element at last
#Here we will take length of the Queue as an input from the user 
#Queue is full Error: When we try to insert an element after the Queue is full
#Queue is Empty Error: When we try to delete an element if the Queue is empty

c=int(input("If you want to continue Enter 1 or else Enter 0 : "))

while c!=0:
    d=int(input("For Pushing Enter 1, For Popping Enter 0 : "))
    if d==1:
        if len(a)<b:
            a=a+[input("Enter an element: ")]
            print("Current Queue is: ",a)
        else:
            print("Queue is Full")
    elif d==0:
        if len(a)>0:
            print(a.pop(0))
            print("Current Queue is: ",a)
        else:
            print("Queue is empty")
    c=int(input("If you want to continue Enter 1 or else Enter 0: "))