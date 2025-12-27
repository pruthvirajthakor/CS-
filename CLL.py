# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Delete a node
    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head
        prev = None

        # If head node is to be deleted
        if curr.data == key:
            # Only one node
            if curr.next == self.head:
                self.head = None
                return

            # More than one node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            self.head = curr.next
            temp.next = self.head
            return

        prev = curr
        curr = curr.next

        while curr != self.head:
            if curr.data == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print("Value not found")

    # Display circular linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")
        

# -------- Main Program --------
cll = CircularLinkedList()

cll.insert_end(10)
cll.insert_end(20)
cll.insert_begin(5)
cll.insert_end(30)

cll.display()

cll.delete(20)
cll.display()
