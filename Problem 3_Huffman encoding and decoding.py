import sys
import operator
import heapq

class Node(object):
        
    def __init__(self, letter = None, frequency = None):
        self.letter = letter
        self.frequency = frequency
        self.value_pair = [letter, frequency]
        self.binary_code = ""
        self.left = None
        self.right = None
        
    def set_value(self, letter = None, frequency = None):
        self.letter = letter
        self.frequency = frequency
        self.value_pair = [letter, frequency]
        
    def get_value(self):
        return [self.letter, self.frequency]
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object. Adapted from course work
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    # defining comparators less_than and equals
    # ref: https://stackoverflow.com/questions/47912064/typeerror-not-supported-between-instances-of-heapnode-and-heapnode
    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.frequency == other.frequency

class Tree:
    def __init__(self,node):
        self.root = node
    def get_root(self):
        return self.root 


def huffman_tree_building(data):
    
    # rule out edge case:
    if not isinstance(data, str):
        print ("Data type error, please enter strings")
        return None
    elif len(data) == 0:
        print ("empty string, please enter again")
        return None
    else:
    
    # main function
    
        # 1. determine letter frequency and sort them in ascending order of the values
        # Ref: https://www.geeksforgeeks.org/python-string-count/
        dic = {}
        for i in data:
            dic[i] = data.count(i)
        sorted_x = sorted(dic.items(), key=operator.itemgetter(1))
        #print ("sorted_x", sorted_x)

        converted_node_dict = []
        for i in range(len(sorted_x)):
            letter = sorted_x[i][0]
            freq = sorted_x[i][1]
            converted_node_dict.append(Node(letter, freq))

        #print("converted_node_dict: ", converted_node_dict)

        #create new heap
        new_heap = converted_node_dict
        #print("new_heap", new_heap)

        heapq.heapify(new_heap)


        while len(converted_node_dict) != 1:
            new_node = Node()
            left = heapq.heappop(new_heap)
            new_node.set_left_child(left)

            right = heapq.heappop(new_heap)
            new_node.set_right_child(right)

            new_node.frequency = left.frequency + right.frequency
            heapq.heappush(new_heap, new_node)

        #print("new_heap now", new_heap)

        # 4. Return the tree
        #for i in list_of_nodes3:
        for i in new_heap:
            tree = Tree(i)
            #print ('\n root is: ', tree.get_root())
            #print ('\n', tree.get_root().get_right_child())#should return "l"
            return tree

# 5. Encode the data
# 5.1 Find the binary codes for each letter:
def post_order_traverse(huffman_tree,visit_pathway):
    
    visit_order = {}
    
    # edge case: if the tree is a single node(meaning it must have a letter stored in {letter: frequency}),
    #we name the visit order as '1' .
    if huffman_tree.get_root().letter is not None:
        visit_order[huffman_tree.get_root().letter] = '1'
        return visit_order
    
    # normal traversing:
    def traverse(node,visit_pathway):
        #node = huffman_tree
        #print (node.letter)
        #print (node.get_right_child())

        if node.get_left_child() is None and node.get_right_child() is None:
            visit_order[node.letter] = visit_pathway
        else:
            
            # traverse left subtree
            #'0' for 'left'
            #print ('else started')
            traverse(node.get_left_child(),visit_pathway + '0')
            
            # traverse right subtree
            #'1' for 'right'
            traverse(node.get_right_child(),visit_pathway + '1')
            
            # visit node
            #visit_order.append(node.get_value())
    
    traverse(huffman_tree.get_root(),visit_pathway)
    
    return visit_order

# 5.2 Encode the original message:
def huffman_encode(data, codes):
    encoded_message = ''
    for letter in data:
        #print (letter)
        if letter not in codes.keys():
            return "data doesn't match the tree!"
        else:
            encoded_message += codes[letter]
    return encoded_message
    print ('Encoded message is: ', encoded_message)

# 6. Decode the message
def huffman_decoding(encoded_message, root):
    decoded_message = ''
    
    upper_limit = len(encoded_message)
    itera = 0
    
    #create a variable to deal with repetitive inputs
    case = 0
    
    while itera < upper_limit:
        
        current_node = root
        
        while current_node.left is not None and current_node.right is not None:
            #if input is not a repetitive string:
            case = 1
            if encoded_message[itera] == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right
            itera += 1 
        decoded_message += current_node.letter
        
        # if input is a repetitive string
        if case == 0:
            itera += 1
             
    return decoded_message
    #print ("decoded_message: ", decoded_message)

# 7. define test function
def test_huffman(input_msg):
    print ("input message: ", input_msg)
    huffman_tree = huffman_tree_building(input_msg)
    if huffman_tree is None:
        print ("waiting for new input...")
    else:
        codes = post_order_traverse(huffman_tree,'')
        huffman_encoded = huffman_encode(input_msg, codes)
        print ("encoded into: ", huffman_encoded)
        decoded = huffman_decoding(huffman_encoded, huffman_tree.get_root())
        print ("decoded message: ", decoded)


# Test case 1:
print("test started...\n")
print("test 1:----------")
test_huffman('i am a boy')
#input message:  i am a boy
#encoded into:  011111010011110111010100000
#decoded message:  i am a boy

# Test case 2:
print("\ntest 2:----------")
test_huffman("today'sweatherisgood")
#input message:  today'sweatherisgood
#encoded into:  0011011001110000001111111010111011110001110011010110000111110100101101100
#decoded message:  today'sweatherisgood

# Test case 3:
print("\ntest 3:----------")
test_huffman("ihave    some  message to say&**()")
#input message:  ihave    some  message to say&**()
#encoded into:  000000011111111110111100101010110000101011110010110111101001001111000111100100110001001100111100001111010101010101110000010
#decoded message:  ihave    some  message to say&**()

# more edge case test according to reviewer's suggestion
# Test case 4:
print("\ntest 4:----------")
test_huffman("aaaaa")
#input message:  aaaaa
#encoded into:  11111
#decoded message:  aaaaa

# Test case 5:
print("\ntest 5:----------")
test_huffman(21)
#input message:  21
#Data type error, please enter strings
#waiting for new input...

# Test case 6:
print("\ntest 6:----------")
test_huffman(14020033)
#input message:  14020033
#Data type error, please enter strings
#waiting for new input...

# Test case 7:
print("\ntest 7:----------")
test_huffman("")
#input message:  
#empty string, please enter again
#waiting for new input...