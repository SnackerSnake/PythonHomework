#Lab #9
#Due Date: 11/08/2019, 11:59PM
########################################
#                                      
# Name:David Hernandez
# Collaboration Statement: Piazza, course materials
#https://stackoverflow.com/questions/50626648/heap-order-in-python
# Note of above: No actual code, just helps with concept of assignment
#  
########################################


class MinHeap:

    # -- YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR!
    def __init__(self):
        self.heap=[]
      

    def __str__(self):
        return f'{self.heap}'

    __repr__=__str__

    #Pseudocode for myself
    #Do parents/children based on index position?
    # [2, 5, 11, 10, 9, 14, 14, 20, 20]
    #index (starting at one):
    # [1, 2, 3, 4, 5, 6, 7, 8]
    #[parent, left child/secondparent1, right child/secondparent2, left child of secondparent1/thirdparent 1, right child of secondparent1/thirdparent2, left child of secondparent2/thirdparent3,
    #right child of secondparent2/thirdparent4, left child of thirdparent1, right child of thirdparent 1]

    #Defines what a parent is in the list.
    def parent(self,index):
        if index>=1 and index<=len(self.heap):
            if index==1:
                return self.heap[index-1]
            else:
                return self.heap[(index//2)-1]

        elif index>len(self.heap) or index<=1:
            return None

    # Defines who is the leftChild in the list.
    def leftChild(self,index):
        if index >= 1 and index <= len(self.heap):
            try:
                self.heap[(index*2)-1]
            except:
                return None
            return self.heap[(index*2)-1]
        else:
            return None

    # Defines who is the rightChild in the list.
    def rightChild(self,index):
        if index >= 1 and index <= len(self.heap):
            try:
                self.heap[(index*2)]
            except:
                return None
            return self.heap[(index*2)]
        else:
            return None

    #Gives len of the heap.
    def __len__(self):
        return len(self.heap)
 
    #Adds x into the heap list.
    def insert(self,x):
        #Adds the something into the heap if it's empty.
        if len(self.heap)==0:
            self.heap.append(x)

        #Handles adding values when the list has at least 1 value.
        else:
            self.heap.append(x)
            place_of_parent=len(self.heap)
            while place_of_parent!=0:
                if x<self.parent((self.heap.index(x))+1):
                    place_of_parent=self.heap.index(self.parent((self.heap.index(x)+1)))
                    place_of_input=self.heap.index(x)
                    parent=self.parent((self.heap.index(x))+1)

                    self.heap.insert(place_of_input, parent)
                    self.heap.insert(place_of_parent, x)
                    del self.heap[place_of_parent+1]
                    del self.heap[place_of_input+1]
                else:
                    place_of_parent=0

    #Deletes the first thing in the list of heap and reorganizes it.
    @property
    def deleteMin(self):

        if len(self)==0:
            return None        
        elif len(self)==1:
            out=self.heap[0]
            self.heap=[]
            return out
        else:
            previous_list = []
            for elements in self.heap:
                previous_list.append(elements)

            value_to_return=self.heap.pop(0)
            right_to_left=len(self.heap)-1
            index_to_search=0
            next_value=self.heap[right_to_left-1]
            keep_checking=1

            while keep_checking!=0:

                for value in self.heap:

                    if next_value==self.heap[right_to_left]:
                        index_to_search+=1
                    else:
                        index_to_search=0
                    if self.heap[right_to_left]<self.parent((self.heap.index(self.heap[right_to_left])+index_to_search)+1):
                        place_of_parent=self.heap.index(self.parent((self.heap.index(self.heap[right_to_left])+index_to_search)+1))
                        place_of_input=self.heap.index(self.heap[right_to_left])
                        parent=self.parent((self.heap.index(self.heap[right_to_left]))+index_to_search+1)

                        self.heap.insert(place_of_parent, self.heap[right_to_left])
                        self.heap.insert(place_of_input, parent)
                        del self.heap[place_of_parent+1]
                        del self.heap[place_of_input+1]

                        for parents in range(2, len(self.heap)):
                            if self.leftChild(parents)== None or self.rightChild(parents)==None or self.rightChild(parents+1):
                                break

                            if self.rightChild(parents+1)>self.rightChild(parents):
                                pass

                    right_to_left-=1
                    try:
                        next_value = self.heap[right_to_left - 1]
                    except:
                        pass

                    if self.parent((self.heap.index(self.heap[right_to_left])))==None:
                        break

                if previous_list == self.heap:
                    keep_checking=0

                else:
                    previous_list = []
                    for elements in self.heap:
                        previous_list.append(elements)

            return value_to_return

'''
            >>> h = MinHeap()
            >>> h.insert(10)
            >>> h.insert(5)
            >>> h
            [5, 10]
            >>> h.insert(14)
            >>> h.heap
            [5, 10, 14]
            >>> h.insert(9)
            >>> h
            [5, 9, 14, 10]
            >>> h.insert(2)
            >>> h
            [2, 5, 14, 10, 9]
            >>> h.insert(11)
            >>> h
            [2, 5, 11, 10, 9, 14]
            >>> h.insert(14)
            >>> h
            [2, 5, 11, 10, 9, 14, 14]
            >>> h.insert(20)
            >>> h
            [2, 5, 11, 10, 9, 14, 14, 20]
            >>> h.insert(20)
            >>> h
            [2, 5, 11, 10, 9, 14, 14, 20, 20]
            >>> h.parent(2)
            2
            >>> h.leftChild(1)
            5
            >>> h.rightChild(1)
            11
            >>> h.parent(8)
            10
            >>> h.leftChild(6)
            >>> h.rightChild(9)
            >>> h.deleteMin
            2
            >>> h.heap
            [5, 9, 11, 10, 20, 14, 14, 20]
            >>> h.deleteMin
            5
            >>> h
            [9, 10, 11, 20, 20, 14, 14]
'''