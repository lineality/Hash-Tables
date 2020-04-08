# '''
# Linked List hash table key/value pair
# '''
# when number of nodes inside is .7 of capasity, auto update:


class LinkedPair:
    def __init__(self, node_key, node_value):
        self.node_key = node_key
        self.node_value = node_value
        self.next_1 = None

    # # print method...what is this called?
    def __repr__(self):
        return f"Key is:{self.node_key}, Value is:{self.node_value}, Next Node is:{self.next_1}"


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity  # list of lists of nodes
        self.counter = 0  # for tracking max capacity for resizing 7%

    def _hash(self, node_key):
        # # First Part:
        # # turning a string or int into an int

        # set variable
        int_output = 0
        # iterate through input string
        for i in str(node_key):
            # convert each letter to a number
            # and add that to the output
            int_output += ord(i) - 96
            # make sure number is positive
            int_output = abs(int_output)
            # make sure number is an integer
            int_output = int(int_output)

        # return hash(key)
        return int_output

    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash
    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass

    def _hash_mod(self, node_key):
        # # Second Part:
        # # making a hash of that input (string or int)
        # note: modulus and hash table size
        # using %x means that your array will be x in size
        # hash_output = int_output % hashtable_length_you_want
        return self._hash(node_key) % self.capacity

    def insert(self, node_key, node_value):

        # step 1: run node_key through hashing_function
        index_to_look_in = self._hash_mod(node_key)
        node_being_checked = self.storage[index_to_look_in]
        # could be done in one line too, case by case

        # insepction
        # print("index_to_look_in", index_to_look_in)

        # 1. check if empty blucket (no collision) simple insert
        # 2. if not, check if item already there (do nothing)
        # 3. if not, put at end of last node and attach
        # 4. if you are replacing a value (overallaping key) print warning

        # make a linked list node (instance of class)
        this_node_mask = LinkedPair(node_key, node_value)

        # 1. check if there is an empty "bucket" (no collision): simple insert
        if node_being_checked is None:
            # # inspection
            # print("test print", node_being_checked)
            # put the node in the array
            node_being_checked = this_node_mask

        else:  # if the needed "bucket" is full:
            # inspection
            # print("collision!")

            # 2. if not, check if already there (do nothing)

            # traverse: as long as there is a node to check
            while node_being_checked is not None:

                # inspection
                # print("traverse")

                # while this node isn't a key/value match
                # for what you are inserting
                # then keep "traversing" ;)
                # until you get to the end, then insert:

                # Does key exist already
                if node_being_checked.node_key == node_key:
                    # inspection
                    # print("same key clicker")

                    # inspection
                    # print("key exists")

                    # if key is the same, check the value
                    if node_being_checked.node_value != node_value:
                        # print and give warning: replacing value
                        # print(
                        #    "Warning! This is replacing a value due to an overlapping key."
                        # )

                        # replaces old value only with a new one
                        node_being_checked.node_value = node_value

                        # exit loop
                        break

                    else:  # both key and value are the same: do nothing
                        break  # stop

                if node_being_checked.next_1 is None:  # if the end

                    # inspection
                    # print("putting in value")

                    # put the new node at the end of the list
                    node_being_checked.next_1 = this_node_mask

                # if this is not the end
                else:  # update the traversing pointer "node_being_checked"
                    node_being_checked = node_being_checked.next_1

    def remove(self, node_key):

        # step 1: run  node_key through hashing_function
        index_to_look_in = self._hash_mod(node_key)
        node_being_checked = self.storage[index_to_look_in]

        # check if not None
        if node_being_checked is not None:

            # 2. if not, check if already there (do nothing)

            # traverse: as long as there is a node to check
            while node_being_checked is not None:

                # if key exists:
                if node_being_checked.node_key == node_key:
                    # erase value

                    node_being_checked.node_value = None

                    # # can break because your done
                    # break

                # move forward the linked-node checking pointer
                node_being_checked = node_being_checked.next_1

        else:  # if item is not there
            return "Key is not found."

    def retrieve(self, node_key):

        # step 1: run  node_key through hashing_function
        index_to_look_in = self._hash_mod(node_key)
        node_being_checked = self.storage[index_to_look_in]

        # check if empty
        if self.storage[index_to_look_in] is not None:

            # 2. if not, check if already there (do nothing)

            # traverse: as long as there is a node to check
            while node_being_checked is not None:

                # if key exists:
                if node_being_checked.node_key == node_key:
                    return node_being_checked.node_value

                # move forward the linked-node checking pointer
                node_being_checked = node_being_checked.next_1

        else:  # if item is not there
            return None
        # return value

    def resize(self):
        # store the old data
        old_data = self.storage.copy()
        # .copy isn't needed!!

        # make storage twice as bit, and blank
        self.capacity *= 2
        self.storage = [None] * self.capacity

        # itterate through list
        for i in range(len(old_data)):
            list_node = old_data[i]
            # iterate through node linked lists
            while list_node:
                self.insert(list_node.node_key, list_node.node_value)
                list_node = list_node.next_1


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
