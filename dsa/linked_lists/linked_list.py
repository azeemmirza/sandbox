# print
# add at any location 
# delete
# increase size


class Node:
  def __init__(self, data = None, next: 'Node' = None):
    self.data = data
    self.next = next
    pass



class LinkedList:
  # ---- constructor ----
  def __init__(self, head: Node, capacity: int = 5):
    self.__head = head
    self.__capacity = capacity
    self.__size = 0 if head == None else 1
  
  # ---- to print the linked list ----
  def print(self):
    temp = self.__head
    eol = '->'
    while temp != None:
      eol = '\n' if temp.next == None else eol
      print(f'[{temp.data}]', end=eol)
      temp = temp.next
    
    print()
  
  # ---- to add the node in the linked list ----
  def insert(self, data, position: int = None):
    node = Node(data)
    
    if self.__size == self.__capacity:
      raise IndexError('LinkedList is full')
    
    if position == None:
      position = self.__size
    
    current = 1
    temp = self.__head
    done = False
    
    while not done:
      # print(f'{current}:{position}')
      
      if current == position:
        # if adding to the last node
        if temp.next == None:
          temp.next = node
        
        # if adding to the mid or other position
        else:
          node.next = temp.next
          temp.next = node
        
        done = True
        
      temp = temp.next
      current += 1
    
    self.__size += 1
    print('node has been added')
    
  
  # ---- to delete from any position in the linked list (default is last) ----
  def delete(self, pos: int = None):
    if self.__size == 0:
      print('List is empty')
      return
    
    if pos == None:
      pos = self.__size - 1
      
    
    if pos == 0:
      self.__head = self.__head.next
      self.__size -= 1
      print('node is deleted')
      return
    
    
    done = False
    temp = self.__head
    current = 0
    
    while not done:
        
      if current == (pos - 1):
        temp.next = temp.next.next
        self.__size -= 1
        done = True
        print('node is deleted')
        return
      
      temp = temp.next
      current += 1
  
  
  # ---- to increase the size of the linked list ----
  def increase_size(self, addition: int = 5):
    self.__capacity += addition
    
  
  def get_size(self):
    return self.__size
  
  def reverse(self):
    curr_node, prev_node = self.__head, None
    
    while curr_node:
      next_node = curr_node.next
      curr_node.next = prev_node
      
      # incrementor
      prev_node = curr_node
      curr_node = next_node
    
    self.__head = prev_node
  
  def reverse_recursive(self, ):
    
      

# ---- end class ----

