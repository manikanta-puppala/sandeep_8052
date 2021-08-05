#Singly Linked List
#In SLL we can travel in only one direction
#We will write two classes here 
#1. For creating node
#2. Appending(Inserting at the end), Deleting, Printing List 
#   and Inserting in middle

class node:
    def __init__(self,data):
        #for SLL we have only next part 
        #while creating a node we will initialize next part to "None"
        self.data=data
        self.next=None
#Node class is completed

class Linked:
#In this class we will intialize head pointer to NONE by default
    def __init__(self):
        self.head=None
    
#Appending or Inserting at the end
    def append(self,data):# Append Function is working fine!!!!
        newNode=node(data)
        if self.head==None:
            #If Linked list is empty, We will append the new node
            #to head Pointer
            self.head=newNode
        else:
            #If Linked list is not empty, we will append the new node at 
            #last for that we need to travel through the linked list until we 
            #reach the last node i.e, "self.next==None"
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            # Here we have the last node in temp Beacause, while loop condition 
            # became false i.e, temp.next==None
            # so we will append new node to temp.next
            temp.next=newNode
    def insertafter(self,prev_data,data):#No Error. Working Fine!!!
        #Create a Newnode to the new data
        newNode=node(data)
        #Here we will travel through the list until we get the Pre_data node
        # after getting that node we will assign newnode to that node and next 
        # part of newnode to the next node
        temp=self.head
        while temp.data!=prev_data:
            temp=temp.next
        #Here we will get temp node as the previous node
        #We need to link the newnode after temp node 
        # for that total 2 operations we should do
        newNode.next=temp.next
        temp.next=newNode

    def printlinked(self):#No Error. Working Fine!!!
        temp=self.head
        print(temp.data,end="->")
        #We will tavel through the linked list and print the data
        while temp.next!=None:
            temp=temp.next
            print(temp.data,end="->")
    def delete(self,data):
        #In deletion we will have three cases
        #Case-1. Deletion of first node
        #Case-2. Deletion of middle node
        #Case-3. Deletion of last node
        temp=self.head
        if temp.data==data:
            #If it is the first node i.e., Case-1
            self.head=temp.next
            #here temp is the first node
            temp.next=None

        else:
            #For case 2 and 3 we need previous node for that we take another 
            #temporary variable prev
            prev=self.head
            while prev.next.data!=data:
                prev=prev.next
            while temp.data!=data:
                temp=temp.next
            #We will get out of loop if the condition become
            #false i.e., temp.data=data and we need to delete temp node
            if temp.next!=None:
                #If it is middle node i.e., Case-2
                prev.next=temp.next
                temp.next=None
            else:
                #If it is Last node
                prev.next=None







obj=Linked()
obj.append(5)
obj.append(6)
obj.append(7)
obj.append(8)
obj.append(9)
obj.insertafter(6,10)
obj.printlinked()
obj.delete(5)
obj.delete(9)
print()
obj.printlinked()
print()