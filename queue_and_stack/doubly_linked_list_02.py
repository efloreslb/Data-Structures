"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
      return str(self.value)


class DoublyLinkedList:
   def __init__(self, node=None):
      self.head = node
      self.tail = node
      self.length = 1 if node is not None else 0

   def __len__(self):
      return self.length

   def __str__(self):
      if self.head is None and self.tail is None:
         return 'empty'
      curr_node = self.head
      output = ''
      output += str(curr_node) + ''
      while curr_node.next is not None:
         curr_node = curr_node.next
         output += str(curr_node) + ''
      return output
         
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
      if self.head is None:
         return

      node_to_remove = self.head
      # Assign new head as DLL head
      new_head = node_to_remove.next
      self.head = new_head
      # Sever connection to previous head
      node_to_remove.next = None
      
      self.length -= 1

      # If DLL is now empty, sever tail connection also
      if self.head is None:
         self.tail = None
      else:
         self.head.prev = None

      return node_to_remove.value

   def add_to_tail(self, value):
      pass

   def remove_from_tail(self):
      pass
        
