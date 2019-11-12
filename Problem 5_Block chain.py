# To build a block chain, we must add several features to a Block.
# A block should have the function to calculate hash values, get current timestamps, get its own data
#and hashed information, and also importantly, the link with previous blocks.
# For hash calculation, we used the code offered in the course work, to use the hashlib library.
# To get current time, we used python datetime library
# We initialize the Block with all the above attributes, and we also initiate a self.next attribute to store the next Block

# After we well-defined a Block, we now move to define BlockChain.
# A blockchain must have a append function so that we can add single block element to it.
# Through traversing the blocks, we move to the end of the blockchain and we add the new block to it
# We will also increase the length for the built BlockChain.
# Actually these process are similar to a linked list, just with the adding of more attributes to the blocks themselves,
#i.e., the .timestamp, .hash, .data attributes.

import hashlib
import datetime

class Block:
    def __init__(self, data):
        current_time = datetime.datetime.now()
        self.timestamp = current_time
        self.data = data
        self.previous_hash = None
        self.hash = self.calc_hash(data)
        self.next = None

    def calc_hash(self,data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def get_timestamp(self):
        print (self.timestamp)
    
    def get_data(self):
        print (self.data)
    
    def get_previous_hash(self):
        print (self.previous_hash)
    
    def get_hash(self):
        print (self.hash)

    
class BlockChain:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def append(self,block):
        # edge case:
        if block.data == '':
            print ("can't add any block without any data when processing block! please add a data-filled block! \nNow return established block chain...\n")
        else:
            self.length += 1
            if self.head is None:
                self.head = block
            else: # move to the tail:
                current_block = self.head
                #print("current_block", current_block.get_data())
                while current_block.next:
                    current_block = current_block.next
                current_block.next = block

    def get_length(self):
        return self.length
    
    def get_block(self,block):
        return block
    
    def get_all_block_info(self):
        if self.head is None:
            return "empty blockchain, please add blocks!"
        else:
            current_block = self.head
            while current_block:
                
                #----print all block info
                print("existing current_block is: ")
                current_block.get_data()
                
                print("current_block created at time: ")
                current_block.get_timestamp()
                
                print("current_block has a hash of: ")
                current_block.get_hash()
                
                print("previous hash for current_block is: ")
                current_block.get_previous_hash()
                
                print("----------\n")
                #-----end of printing info
                
                # move to the next block
                current_block = current_block.next

def blockchain_building(input_list_of_blocks):
    '''
    Input: a list containing blocks, e.g., blocks_to_be_added = [block1, block2, block3]
    Output:
    '''
    blockchain = BlockChain()
    
    for blk in input_list_of_blocks:
        if blk.data == '':
            print("empty block for",blk, ", stop building blockchain!\n")
        else:
            blockchain.append(blk)
    return blockchain


# Test case 1, normal test
block1 = Block('a')
block2 = Block('b')
block3 = Block('c')

block2.previous_hash = block1.hash
block3.previous_hash = block2.hash

blocks_to_be_added = [block1, block2, block3]
blockchain = blockchain_building(blocks_to_be_added)

# print all block info in the blockchain
blockchain.get_all_block_info()
#
# return:
#existing current_block is: 
#a
#current_block created at time: 
#2019-11-01 14:03:26.294939
#current_block has a hash of: 
#ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
#previous hash for current_block is: 
#None
#----------

#existing current_block is: 
#b
#current_block created at time: 
#2019-11-01 14:03:26.294996
#current_block has a hash of: 
#3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d
#previous hash for current_block is: 
#ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
#----------

#existing current_block is: 
#c
#current_block created at time: 
#2019-11-01 14:03:26.295036
#current_block has a hash of: 
#2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6
#previous hash for current_block is: 
#3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d
#----------

# Test case 2, normal test
block1 = Block('a-cc')
block2 = Block('de0-w')
block3 = Block('gwaht')

block2.previous_hash = block1.hash
block3.previous_hash = block2.hash

blocks_to_be_added = [block1, block2, block3]
blockchain = blockchain_building(blocks_to_be_added)

# print all block info in the blockchain
blockchain.get_all_block_info()
#
#return:
#existing current_block is: 
#a-cc
#current_block created at time: 
#2019-11-01 14:04:39.094839
#current_block has a hash of: 
#17f44a04e15a0230cc67f720aaa769ffc5d850f1020d6e63d3ba607e96361a9c
#previous hash for current_block is: 
#None
#----------

#existing current_block is: 
#de0-w
#current_block created at time: 
#2019-11-01 14:04:39.094894
#current_block has a hash of: 
#e71ba7c12fb124211d9cb585985fce063ef02b9d57fba1846a671ed49b0213a3
#previous hash for current_block is: 
#17f44a04e15a0230cc67f720aaa769ffc5d850f1020d6e63d3ba607e96361a9c
#----------

#existing current_block is: 
#gwaht
#current_block created at time: 
#2019-11-01 14:04:39.094935
#current_block has a hash of: 
#73b31b76e57dbc245078125aceabde8b939d718f248b2b74adbf83a0a76b0415
#previous hash for current_block is: 
#e71ba7c12fb124211d9cb585985fce063ef02b9d57fba1846a671ed49b0213a3
#----------

# Test case 3, edge case test
block1 = Block('a')
block2 = Block('b')
block3 = Block('')


block2.previous_hash = block1.hash
block3.previous_hash = block2.hash

blocks_to_be_added = [block1, block2, block3]
blockchain = blockchain_building(blocks_to_be_added)

# print all block info in the blockchain
blockchain.get_all_block_info()
#
#return
#empty block for <__main__.Block object at 0x7f62c44e4208> , stop building blockchain!

#existing current_block is: 
#a
#current_block created at time: 
#2019-11-01 14:05:48.355482
#current_block has a hash of: 
#ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
#previous hash for current_block is: 
#None
#----------

#existing current_block is: 
#b
#current_block created at time: 
#2019-11-01 14:05:48.355564
#current_block has a hash of: 
#3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d
#previous hash for current_block is: 
#ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
#----------

# Test case 4, edge case test
block1 = Block('')
block2 = Block('')
block3 = Block('')


block2.previous_hash = block1.hash
block3.previous_hash = block2.hash

blocks_to_be_added = [block1, block2, block3]
blockchain = blockchain_building(blocks_to_be_added)

# print all block info in the blockchain
blockchain.get_all_block_info()
#
#return
#empty block for <__main__.Block object at 0x7f62c44e4630> , stop building blockchain!
#empty block for <__main__.Block object at 0x7f62c44e4cc0> , stop building blockchain!
#empty block for <__main__.Block object at 0x7f62c44e4080> , stop building blockchain!
#'empty blockchain, please add blocks!'

