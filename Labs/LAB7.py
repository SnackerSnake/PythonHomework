#Lab #7
#Due Date: 10/11/2019, 11:59PM 
########################################
#                                      
# Name:David Hernandez
# Collaboration Statement: Course Material
#https://stackoverflow.com/questions/35559632/insert-a-node-at-the-tail-of-a-linked-list-python-hackerrank
#^Same as lecture's adding at end of tail except slightly more code
#https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class OrderedLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        return self.count

    def __del__(self):
        pass

    def add(self, value):
        if self.head==None:
            self.head=Node(value)
            self.tail=Node(value)

        elif Node(value).value <= self.head.value:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

        elif Node(value).value > self.head.value and Node(value).value < self.tail.value:
            new_node = Node(value)
            current = self.head

            while (current.next != None):
                if current.next.value>new_node.value:
                    new_node.next=current.next
                    current.next=new_node
                    break
                current = current.next
        #add duplicate of tail
        else:
            new_node=Node(value)
            current=self.head

            while (current.next != None):
                current=current.next

            current.next=new_node
            self.tail=Node(value)

    def pop(self):
        if self.tail == None:
            pass

        elif self.tail.value==self.head.value:
            value_of_tail = self.tail.value
            del self.tail
            self.head=None
            self.tail=None

            return value_of_tail

        elif self.head.next.value== self.tail.value:
            value_of_tail = self.tail.value
            del self.head.next
            self.head.next=None
            self.tail=self.head
            #self.tail=self.head
            #self.tail = None
            return value_of_tail

        else:
            value_of_tail=self.tail.value
            previous=None
            temp=self.head

            while (temp.next.value != self.tail.value):
                temp=temp.next
                previous=temp
                continue
            del temp.next
            temp.next = None
            self.tail = previous

            return value_of_tail


    def remDuplicates(self):
        pass
        #current=self.head.next
        #while (current.next!=self.tail):
            #if Node(1).value==1:
                #del current
            #current = current.next
        # --- Your code starts here
'''
        >>> x=OrderedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.remDuplicates()
        >>> x.pop()
        8.76
        >>> x
        Head:Node(1)
        Tail:Node(5)
        List:1 3 5
    '''

""""
Archive of add and pop:
current = self.head
            new_tail=0

            while (current.next != None):
                if current.next==self.tail:
                    new_tail=current
                current=current.next

            delete(self.tail)
            self.tail=new_tail
            
 new_node=Node(value)
            current=self.head
            if current.next != None:
                if current.next.value > Node(value).value:
                    new_node.next = current.next
                    current.next = new_node

            while (current.next != None):
                current=current.next
                if current.next!=None:
                    if current.next.value > Node(value).value:
                        new_node.next=current.next
                        current.next=new_node
                        break
            current.next=new_node
            self.tail=Node(value)
            
            
            
            
        if self.head==None:
            self.head=Node(value)
            #self.tail=Node(value)

        elif Node(value).value > self.tail.value:
            current=self.head
            while (current.next != None):
                current.next=None
            current.next=Node(value)
            self.tail=Node(value)

        elif Node(value).value < self.head.value:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            
            
        elif Node(value).value > self.tail.value:
            current=self.head
            while (current.next != None):
                current.next=None
            current.next=Node(value)
            self.tail=Node(value)

            # new_node = Node(value)
            # new_node.next=self.tail
            # self.tail=new_node
            # current=new_node
            
        self.count += 1
        if self.count==1:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail= new_node
            
             self.count+=1
        if self.count == 1:
            self.tail=self.head
        else:
            self.tail= new_node
    """