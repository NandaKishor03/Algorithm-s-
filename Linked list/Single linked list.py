###  Node Class
class Node:
    def __init__(self, data):
        self.data = data  # The value or data of the node
        self.next = None  # Pointer to the next node in the list


###  LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None         # Head of the list, initially empty


    def Count_nodes(self):
        count = 0                     # Initialize count with 0
        current = self.head   
        while current:
            count += 1                # Increment count by 1
            current = current.next    # Move pointer to next node
        return count                  # Return the count of nodes



    def display(self,head=None):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")               # Indicate the end of the list


    def InsertAtEnd(self, data):
        new_node = Node(data)            # Create a new node
        if not self.head:
            self.head = new_node         # If the list is empty, set head to new node
            return
        temp = self.head
        while temp.next:
            temp = temp.next             # Traverse to the last node
        temp.next = new_node             # Insert the new node

    
    def InsertAtFront(self, data):
        new_node = Node(data)       # Create a new node with the given data
        new_node.next = self.head   # Point the new node to the current head
        self.head = new_node        # Update the head to the new node


    def DeleteAtFront(self):
        if self.head is None:
            return
        current = self.head.next        # Point Current to the next node
        self.head = current             # Update the head to the next node
    

    def DeleteAtEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next      # Traverse to the second last node
        current.next = None             # Delete the last node


    def DeleteAtPosition(self,position):
        current = self.head
        if current is None:
            return self.head
        if position == 1:           
            self.DeleteAtFront()
        for i in range(1, position - 1):        # Traverse to the node just before the position
            current = current.next
            if current or current.next:
                print("Position out of range")
                return self.head
        current.next = current.next.next        # Jump over the node to be deleted
        return self.head


    def Search_key(self, key):
        current = self.head
        while current:
            if current.data == key:       # If the current node's value is equal to key,
                return True               # return True
            current = current.next        # Move to the next node
        return False                      # If there is no node with value as key, return false

 
    def reverse(self):
        prev = None
        current = self.head
        while  current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            self.head = prev
        return self.display(prev)


# Create a linked list
linked_list = LinkedList()

# Append some elements
linked_list.InsertAtEnd(1)
linked_list.InsertAtEnd(2)
linked_list.InsertAtEnd(3)

# Append Number At front
# linked_list.InsertAtFront(10)  # Output: 10 -> 1 -> 2 -> 3 -> 4 -> None

# Reverse the LinkedList 
# linked_list.reverse()  # Output: 3 -> 2 -> 1 -> None

# Delete Number at front of LinkedList
# linked_list.DeleteAtFront()

# Delete Number at end of LinkedList
# linked_list.DeleteAtEnd()

# Search the element
# print(linked_list.Search_key(2))   # Output: True

linked_list.DeleteAtPosition(2)

# Length of the Linked list
print(linked_list.Count_nodes())

# Display the linked list
linked_list.display()  
