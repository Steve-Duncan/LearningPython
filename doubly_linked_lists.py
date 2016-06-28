'''
Create Node class, which takes a value upon initalization and sets it to
Node.value. Node.next and Node.previous are none at time of instantiation.
'''


class Node(object):

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

'''
Create DoublyLinkedList class, takes no arguments upon initialization and sets
DoublyLinkedList.head and DoublyLinkedLIst.tail to none.
'''


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def Append(self, value):  # this adds node to end of list
        newnode = Node(value)
        if self.head is None:
            # means this is empty list, so this is the first node being added
            # head, tail and node values are same for first node
            self.head = self.tail = newnode
        else:  # this is not the first node, so there are already head and tail values
            newnode.prev = self.tail  # set current node value to new node
            self.tail.next = newnode  # set previous node's next link to new node

            self.tail = newnode  # set new tail to current node
            self.tail.next = None  # set new node next link to none
        return self

    # this inserts node either before or after a target node
    def Insert(self, value, position, targetvalue):
        current = self.head  # start at head node
        while current is not None:
            # look for node containing value which equal targetvalue
            if current.value == targetvalue:
                if position == "before":  # insert a new node before a target node
                    # create new node, passing current.prev Node as 'prev' and current
                    # node as 'next'
                    newnode = Node(value, current.prev, current)
                    if current == self.head:
                        current.prev = self.head = newnode
                    else:
                        current.prev.next = current.prev = newnode

                else:  # insert a new node after a target node
                    # create new node, passing current node as 'prev' and current.next
                    # node as 'previous'
                    newnode = Node(value, current, current.next)
                    if current == self.tail:
                        current.next = self.tail = newnode
                        newnode.prev = current
                    else:
                        current.next = current.next.prev = newnode
                        newnode.prev = current

                return "Successfully inserted new Node with value {0} {1} Node containing the value {2}.".format(value, position, targetvalue)
            current = current.next  # get the next node
        print "**************OOPS, target value (", targetvalue, ") not found!************"
        return False

    def Del(self, value):
        current = self.head  # start at the head node
        while current is not None:
            if current.value == value:  # look for node which has a value equal to value provided
                # Handle case if current Node is the Tail node in our list
                if current is self.tail:
                    current = current.prev
                    current.next = None
                    self.tail = current
                # Handle case if current node is Head node in our list
                elif current is self.head:
                    current = current.next
                    current.prev = None
                    self.head = current
                # Else in middle of the list, proceed to adjust pointers
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    current.next = None
                    current.prev = None
                print(
                    "Node containining value {0} was removed from "
                    "DoublyLinkedList"
                    .format(value))
                return "Node found and removed from DoublyLinkedList"
            current = current.next
        return False

    def PrintAll(self):
        current = self.head
        nodecount = 1  # Starting count at 1
        nodevals = []
        if current is None:
            return "\n!!!!!!~~~~~ No Nodes in Doubly linked list! Please insert " \
                "Nodes containing values! !!!!!!~~~~~\n\n"
        print "!!!!!!~~~~~~BEGIN DOUBLY LINKED LIST INFORMATION ~~~ ~~~!!!!!!\n"
        while current is not None:
            nodeinfostring = "Node at position {0} has a value of {1}".format(
                nodecount, current.value)
            if nodecount == 1:
                nodeinfostring = "Head " + nodeinfostring
            nodevals.append(current.value)
            current = current.next
            if current is not None:
                nodecount += 1
                nodeinfostring = nodeinfostring + " and has a next Node."
            else:
                nodeinfostring = "Tail " + nodeinfostring + "."
            print nodeinfostring
        print "\n\n---Total List Length: {}\n" \
            "---Values: {}\n".format(
                nodecount, nodevals)
        return "~~~~~~ END DOUBLY LINKED LIST INFORMATION...for now...~~~~~~\n"

    # def PrintAll2(self):
    #     current = self.head
    #     print "Prev -- Node -- Next"
    #     while current is not None:
    #         # print current.value
    #         if current.prev is not None:
    #             print current.prev.value, "--", current.value, "--",
    #         else:
    #             print current.prev, "--", current.value, "--",

    #         if current.next is not None:
    #             print current.next.value, "\n"
    #         else:
    #             print current.next, "\n"

    #         current = current.next
    #     return True


# instantiate the list
dlList = DoublyLinkedList()


# Call on PrintAll function to verify that our DoublyLinkedList exists and has
# no values
# dlList.NodeInfo()
print dlList.PrintAll()

# add values to list
dlList.Append(5)


# Validate
print dlList.PrintAll()


# Call on Append function, providing a value to insert into a new node, and
# then insert that Node at the end of the DoublyLinkedList
dlList.Append(7)


# Validate
print dlList.PrintAll()


# Call on Append function, providing a value to insert into a new node, and
# then insert that Node at the end of the DoublyLinkedList
dlList.Append(8)


# Validate
print dlList.PrintAll()


# Call on Append function, providing a value to insert into a new node, and
# then insert that Node at the end of the DoublyLinkedList
dlList.Append(3)

# Validate
print dlList.PrintAll()

# Call on Append function, providing a value to insert into a new node, and
# then insert that Node at the end of the DoublyLinkedList
dlList.Append(9)

# Validate
print dlList.PrintAll()

# Call on Append function, providing a value to insert into a new node, and
# then insert that Node at the end of the DoublyLinkedList
dlList.Append(14)

# Validate
print dlList.PrintAll()

# Delete node with value 5 (AKA testing for head node deletion success)
dlList.Del(5)


# Validate
print dlList.PrintAll()


# Delete node with value 3 (AKA testing for middle node deletion sucess)
dlList.Del(3)


# Validate
print dlList.PrintAll()

# Delete node with value 3 (AKA testing for middle node deletion sucess)
dlList.Del(14)


# Validate
print dlList.PrintAll()

# Insert after test
print dlList.Insert(22, "before", 9)

# Insert after test, tail
print dlList.Insert(33, "before", 7)

# Insert before test
print dlList.Insert(10, "after", 9)

# Insert before test, head
print dlList.Insert(1, "after", 33)

# Validate
print dlList.PrintAll()
