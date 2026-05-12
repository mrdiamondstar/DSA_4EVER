class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_beg(self , data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def insert_at_end(self , data):
        new_node=Node(data)
        
        if not self.head:
            self.head=new_node
            return 
        
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        
    def userdefine_insert(self):
        print("Enter the n value:")
        n=int(input())
        i=1
        while i<n:
            data=int(input("Enter the node value:"))
            new_node=Node(data)
            if not self.head:
               self.head=new_node
               continue 
            temp=self.head
            while temp.next:
              temp=temp.next
            temp.next=new_node
            i += 1   
        
    def reverse_list(self):
        prev=None
        curr=self.head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
            
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data ,end="->")
            temp=temp.next
        print("Done")
l1=Linkedlist()
l1.userdefine_insert()
l1.display() 
l1.insert_at_beg(5)
l1.insert_at_end(3)
l1.display()    
l1.reverse_list()
l1.display()       