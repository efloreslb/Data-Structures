"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        # Case 1: Empty List
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # Case 2: Not Empty
        else: 
            # Save old head to local variable
            old_head = self.head
            # Link both nodes
            new_node.next = old_head
            old_head.prev = new_node
            # Assign new node as DLL head
            self.head = new_node

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        new_node = ListNode(value) 
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        self.length -= 1
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
        self.add_to_head(value)

    def move_to_end(self, node):
        if node is self.tail:
          return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def delete(self, node):
        if not self.head and not self.tail:
          return
        if self.head == self.tail:
          self.head = None
          self.tail = None
          self.length -=1
        elif self.head == node:
          self.head = node.next
          self.length -= 1
          node.delete()
        elif self.tail == node:
          self.tail = node.prev
          self.length -= 1
          node.delete()
        else:
          self.length -= 1
          node.delete()

    def get_max(self):
        pass
