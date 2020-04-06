# singly linked list framework
#
class Node:  # creating a class
    # constructor "method" (a function)
    def __init__(self, node_value):
        # attributes: just 2,
        # 1. the value this nodes holds, and
        # 2. a link to another node
        self.node_value = node_value
        self.next_1 = None

# example for how to
# make a linked list
# step 1: set values
# step 2: connect the nodes
node1 = Node([])
node2 = Node([])
node3 = Node([])
node4 = Node([])
node5 = Node([])
node6 = Node([])
node7 = Node([])
node8 = Node([])
node9 = Node([])
node10 = Node([])

node1.next_1 = node2
node2.next_1 = node3
node3.next_1 = node4
node4.next_1 = node5
node5.next_1 = node6
node6.next_1 = node7
node7.next_1 = node8
node8.next_1 = node9
node9.next_1 = node10
node10.next_1 = None


# a normal list...not  linked list...version

# Function to display hashtable
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end = " ")
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
        print()

hashtable_length_you_want = 10

# Create a Hashtable as a nested list.
hash_table = [[] for _ in range(hashtable_length_you_want)]

# hashing function that works on any ascii input
def string_or_int_hash(string1, hashtable_length_you_want = 64):
    # # First Part:
    # # turning a string or int into an int

    # set variable
    int_output = 0
    # iterate through input string
    for i in string1:
        # convert each letter to a number
        # and add that to the output
        int_output += (ord(i) - 96)
        # make sure number is positive
        int_output = abs(int_output)
        # make sure number is an integer
        int_output = int(int_output)

    # # Second Part:
    # # making a hash of that input (string or int)
    # note: modulus and hash table size
    # using %x means that your array will be x in size
    hash_output = int_output%hashtable_length_you_want

    return hash_output


# Insert Function to add values to the hash table
def insert_chained_hashtable(Hashtable, value1):
    # this function takes in the hash table and the value
    # the function then generates the key (using the hash function on the value)
    # which works even if the function is a string
    #
    hash_key = string_or_int_hash(value1,hashtable_length_you_want)
    # and simply adds each input item
    # to the hash table

    # if that hash table slot is empty: use it!
    if len(hash_table[hash_key]) is 0:
        # make the new node
        vars()[f'hashkey_{hash_key}__node_number_{len(hash_table[hash_key])+1}'] = Node([])

        # add the input value to the new node
        vars()[f'hashkey_{hash_key}__node_number_{len(hash_table[hash_key])+1}'].node_value.extend([value1])

        # and put that node into the hash-table-array-list
        # make a mask
        mask_1 = vars()[f'hashkey_{hash_key}__node_number_{len(hash_table[hash_key])+1}']
        hash_table[hash_key].append( [mask_1] )

    else: #
        # make the new node
        vars()[f'hashkey_{hash_key}__node_number_{len(hash_table[hash_key])+1}'] = Node([])

        # add the input value to the new node
        vars()[f'hashkey_{hash_key}__node_number_{len(hash_table[hash_key])+1}'].node_value.extend([value1])
        # vars()[f'hashkey_{hash_key}__node_number_{len(hash_table[hash_key])}'].next_1 = vars()[f'hashkey_{hash_key}__node_number_{len(hash_table[hash_key])+1}']

        # make a mask
        mask_3 = vars()[f'hashkey_{hash_key}__node_number_{len(hash_table[hash_key])+1}']

        # template: node2.next_1 = node3
        hash_table[hash_key][len(hash_table[hash_key])-1][0].next_1 = mask_3

        # and put that node into the hash-table-array-list
        hash_table[hash_key].append( [mask_3] )

# Table
insert_chained_hashtable(hash_table, 'Tom')
insert_chained_hashtable(hash_table, 'Tomato')
insert_chained_hashtable(hash_table, 'Potato')
insert_chained_hashtable(hash_table, 'Eggs')
insert_chained_hashtable(hash_table, 'Harris')
insert_chained_hashtable(hash_table, 'Matilda')

display_hash (hash_table)

def get_hash_chain_value(hash_table,hash_key, node_number):
    if node_number is 1:
        return hash_table[hash_key][0][0].node_value

    else:
        for i in range(node_number):
            this_node = hash_table[hash_key][0][0]
            next_node = hash_table[hash_key][0][0].next_1
            this_node = next_node

        return this_node.node_value

print(get_hash_chain_value(hash_table, 0, 1))
print(get_hash_chain_value(hash_table, 0, 2))
