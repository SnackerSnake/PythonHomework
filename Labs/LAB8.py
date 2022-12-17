#Lab #8
#Due Date: 10/25/2019, 11:59PM 
########################################
#                                      
# Name:David Hernandez
# Collaboration Statement:             
#
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> x.reverse()
        >>> x
        Head:Node(3)
        Tail:Node(2)
        Queue:3 2
    '''
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            #print(temp.value)
            out.append(str(temp.value))
            temp=temp.next


        out=' '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        return (self.head and self.tail)==None

    #Use Node's value and next
    #Make values/inputs nodes
    def enqueue(self, x):
        if self.count==0:
            self.tail = Node(x)
            self.tail.next=None
            self.count+=1

        elif self.count ==1:
            self.head=self.tail
            self.tail=Node(x)
            self.head.next = self.tail
            self.count += 1

        else:
            self.tail.next = Node(x)
            self.tail = Node(x)
            #No idea how to deal with four enqueues w/o using previous tails

            self.count+=1
        """
        
         self.tail.next=Node(x)
        self.tail=Node(x)
        
        
        storage=self.tail
            #self.tail=
            self.tail = Node(x)
            self.tail.next=storage
            print(self.tail.next)

            print(self.tail)
            #self.tail.next=None
            print(self.tail.next)
            
            
        elif self.count==2:
        self.tail.next=self.tail
            self.tail=Node(x)
            self.tail.next=None
        stuff
        else:

            self.tail.next = None

            self.count += 1"""

    def dequeue(self):
        if self.count==0:
            pass

        elif self.count==1:
            storage=self.head
            self.count-=1
            self.head=None
            self.tail=None

            return storage

        else:
            storage = self.head
            self.count -= 1
            self.head=self.head.next

            return storage

    def __len__(self):
        return self.count

    def reverse(self):
        if self.count==0:
            pass
        else:
            pass

        """else:
            storage_list=[]
            list_count=0

            while len(storage_list)!=self.count:
                if storage_list==[]:
                    storage_list.append(self.head)
                elif len(storage_list)==1:
                    storage_list.append(self.head.next)
                else:
                    storage_list.append(self.tail)

            while storage_list!=[]:
                if len(storage_list)
                    self.head=storage_list[list_count]
                    storage_list.remove(list_count)
                #Supposed to make the new node list"""


    """ storage=self.head
            self.head=self.tail
            self.tail=storae
            
            list_count+=1
                if len(storage_list)==1:
                    self.head=storage_list[0]
                    storage_list
                    list_count+=1
                else:
                    self.head.next=storage_list[2]
            
                        while storage_list!=[]:
                if len(storage_list)==1:
                    self.head=storage_list[0]
                elif len(storage_list)==2:
                    self.head.next=storage_list[1]
                else:
                    self.tail=storage_list[2]"""