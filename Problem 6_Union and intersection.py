class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
# For the function of Union:
# First, we make use of python set() to both store the values of a linkedList and to dereplicate the values
# In this step, we traverse the linkedlist and get the values of each node, then store them in the set
# Then, we build a new LinkedList using values from the set()
def union(llist_1, llist_2):
    # Your Solution Here
    
    # create a list and a linkedlist
    emptylist = set()
    new_llist = LinkedList()
    
    # traversing linkedlist1:
    head1 = llist_1.head
    current_node1 = head1
    
    # traversing linkedlist2:
    head2 = llist_2.head
    current_node2 = head2
      
    if current_node1 is None:
        print("llist1 is empty, enter new list1...")
    if current_node2 is None:
        print("llist2 is empty, enter new list1...")
     
   
    while current_node1:
        emptylist.add(current_node1.value)
        current_node1 = current_node1.next
        
  
    while current_node2:
        emptylist.add(current_node2.value)
        current_node2 = current_node2.next
    
    for i in emptylist:
        new_llist.append(i)
    if new_llist.size() != 0:
        return new_llist
    else:
        return 'Two llists have No union'

# For the function of Intersection:
# First, we again use python set() to both store the values of a linkedList and to dereplicate the values
# Then, we first pick up the first value from list1, and then compare all values of list2 to it,
#if values match, we store the value in the set(), and we move the node of that value in list2 to the next node
# After we finished checking all list2 values to the first value of list1, we move to the second value of list1, 
#and do the same steps again.
# Last, we build a new linkedlist using values of the established set() mentioned above.

def intersection(llist_1, llist_2):
    # Your Solution Here

    # create a list and a linkedlist
    emptylist = set()
    new_llist = LinkedList()
    # traversing linkedlist1:
    head1 = llist_1.head
    current_node1 = head1

    head2 = llist_2.head
    current_node2 = head2

    if current_node1 is None:
        print("llist1 is empty, enter new list1...")
    if current_node2 is None:
        print("llist2 is empty, enter new list1...")
    
    # Modified code according to the reviewer's suggestion:
    # actually this is extremely brilliant, i think the most significant difference is that the improved version takes advantage of python set(), 
    # because to look up in a set only takes O(1) time complexity (ref: https://stackoverflow.com/questions/7351459/time-complexity-of-python-set-operations)
    # , and in this way, we divided the comparing process into two: first we generate a list, then we look up in the list.
    #, thus the time complexity is O(n) + O(n)*O(1) = O(n), while in my own case, i have nested while loop which generate O(n^2) time complexity
    
    # we first create a set to store llist1 value
    while current_node1:
        if current_node1.value not in emptylist:
            emptylist.add(current_node1.value)
        current_node1 = current_node1.next
    # then we compare elements of llist2 to the set
    while current_node2:
        if current_node2.value in emptylist:
            new_llist.append(current_node2.value)
            emptylist.discard(current_node2.value)
        current_node2 = current_node2.next
    
    #my previous codes:
    '''        
    while current_node1:
        #print ('cur_node1: ', current_node1.value)
        while current_node2:
            #print ('cur_node2: ', current_node2.value)
            if current_node2.value == current_node1.value:
                emptylist.add(current_node2.value)
            current_node2 = current_node2.next
        current_node2 = head2 # after reaching the end of llist2, we reset the current_node2 to the header
        current_node1 = current_node1.next  

    for i in emptylist:
        new_llist.append(i)
    '''
    
    if new_llist.size() != 0:
        return new_llist
    else:
        return 'Two llists have No intersection'

        
        
        
# Test case 1
print("test 1: ")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("union: ", union(linked_list_1,linked_list_2))
print ("intersection: ", intersection(linked_list_1,linked_list_2))
print ("-------------------------")
#
#test 1: 
#union:  32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
#intersection:  4 -> 21 -> 6 -> 
#-------------------------


# Test case 2
print("test 2: ")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("union: ", union(linked_list_3,linked_list_4))
print ("intersection: ", intersection(linked_list_3,linked_list_4))
print ("-------------------------")
#
#test 2: 
#union:  65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
#intersection:  Two llists have No intersection
#-------------------------


# Test case 3
print("test 3: ")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ("union: ", union(linked_list_5,linked_list_6))
print ("intersection: ", intersection(linked_list_5,linked_list_6))
print ("-------------------------")
#
#test 3: 
#union:  65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 23 -> 
#intersection:  Two llists have No intersection
#-------------------------

# Test case 4
print("test 4: ")
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print ("union: ", union(linked_list_7,linked_list_8))
print ("intersection: ", intersection(linked_list_7,linked_list_8))
print ("-------------------------")
#
#test 4: 
#llist1 is empty, enter new list1...
#llist2 is empty, enter new list1...
#union:  Two llists have No union
#llist1 is empty, enter new list1...
#llist2 is empty, enter new list1...
#intersection:  Two llists have No intersection
#-------------------------

# Test case 5
print("test 5: ")
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [1,3,4]
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print ("union: ", union(linked_list_9,linked_list_10))
print ("intersection: ", intersection(linked_list_9,linked_list_10))
print ("-------------------------")
#
#test 5: 
#llist2 is empty, enter new list1...
#union:  1 -> 3 -> 4 -> 
#llist2 is empty, enter new list1...
#intersection:  Two llists have No intersection
#-------------------------