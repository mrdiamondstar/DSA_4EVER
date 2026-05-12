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
        
        if not self.head :
            new_node=self.head
            return 
        
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data ,end="->")
            temp=temp.next
        print("Done")
l1=Linkedlist()
l1.insert_at_beg(5)
l1.insert_at_end(3)
l1.display()        