#LAB 12
#Due Date: 11/22/2019, 11:59PM
########################################
#                                      
# Name:David Hernandez
# Collaboration Statement:Course Materials
# from Lab 9:
# Piazza, course materials
# https://stackoverflow.com/questions/50626648/heap-order-in-python
# Note of above: No actual code, just helps with concept of assignment
#
########################################

class MinHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return f'{self.heap}'

    __repr__ = __str__

    # Pseudocode for myself
    # Do parents/children based on index position?
    # [2, 5, 11, 10, 9, 14, 14, 20, 20]
    # index (starting at one):
    # [1, 2, 3, 4, 5, 6, 7, 8]
    # [parent, left child/secondparent1, right child/secondparent2, left child of secondparent1/thirdparent 1, right child of secondparent1/thirdparent2, left child of secondparent2/thirdparent3,
    # right child of secondparent2/thirdparent4, left child of thirdparent1, right child of thirdparent 1]

    # Defines what a parent is in the list.
    def parent(self, index):
        if index >= 1 and index <= len(self.heap):
            if index == 1:
                return self.heap[index - 1]
            else:
                return self.heap[(index // 2) - 1]

        elif index > len(self.heap) or index <= 1:
            return None

    # Defines who is the leftChild in the list.
    def leftChild(self, index):
        if index >= 1 and index <= len(self.heap):
            try:
                self.heap[(index * 2) - 1]
            except:
                return None
            return self.heap[(index * 2) - 1]
        else:
            return None

    # Defines who is the rightChild in the list.
    def rightChild(self, index):
        if index >= 1 and index <= len(self.heap):
            try:
                self.heap[(index * 2)]
            except:
                return None
            return self.heap[(index * 2)]
        else:
            return None

    # Gives len of the heap.
    def __len__(self):
        return len(self.heap)

    # Adds x into the heap list.
    def insert(self, x):
        # Adds the something into the heap if it's empty.
        if len(self.heap) == 0:
            self.heap.append(x)

        # Handles adding values when the list has at least 1 value.
        else:
            self.heap.append(x)
            place_of_parent = len(self.heap)
            while place_of_parent != 0:
                if x < self.parent((self.heap.index(x)) + 1):
                    place_of_parent = self.heap.index(self.parent((self.heap.index(x) + 1)))
                    place_of_input = self.heap.index(x)
                    parent = self.parent((self.heap.index(x)) + 1)

                    self.heap.insert(place_of_input, parent)
                    self.heap.insert(place_of_parent, x)
                    del self.heap[place_of_parent + 1]
                    del self.heap[place_of_input + 1]
                else:
                    place_of_parent = 0

    @property
    def deleteMin(self):
        #Checks if heap is empty.
        if self.heap==[]:
            return None
        else:

            #Takes out the first thing in the heap.
            value_to_return=self.heap.pop(0)
            # Variable to use later
            temporary_heap=[]

            #Takes input and adds its values to a new temporary heap so that it can be in the right heap order.
            for numbers in range(len(self.heap)):
                temporary_heap.append(self.heap.pop())

            #Adds the values of the temporary heap into the new self.heap.
            for numbers in range(len(temporary_heap)):
                x=temporary_heap.pop()
                self.insert(x)

            #Returns deleted number.
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

def heapSort(numList):
    #Checks if input is a list.
    if type(numList)==list:
        pass
    else:
        return None

    #Sets variables to use them later.
    temporary_heap=MinHeap()
    sort_heap = []

    #Takes the input and turns it into a heap.
    for numbers in range(len(numList)):
        temporary_heap.insert(numList.pop())

    #Takes items from the heap and turns it back into a list.
    for same_numbers in range(len(temporary_heap)):
        sort_heap.append(temporary_heap.deleteMin)

    #Output
    return sort_heap
'''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
'''