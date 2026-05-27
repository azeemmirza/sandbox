from node import SinglyNode

class SinglyLinkedList:
  # ---- constructor ----
  def __init__(self, head: SinglyNode, capacity: int = 5):
    self.__head = head
    self.__capacity = capacity
    self.__size = 0 if head == None else 1
  
  
  # --- to print the linked list ---
  def print(self):
    temp = self.__head
    eol = '->'
    
    while temp != None:
      eol = '\n' if temp.get_next() == None else eol
      print(f'[{temp.get_data()}]', end=eol)
      temp = temp.get_next()
    
    # print blank line
    print()
  
  
  # --- to add the node in the linked list ---
  def insert(self, data, position: int = None):
    node = SinglyNode(data)
    
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
        if temp.get_next() == None:
          temp.set_next(node)
        
        # if adding to the mid or other position
        else:
          node.set_next(temp.get_next())
          temp.set_next(node.get_next())
        
        done = True
      
      temp = temp.get_next()  
      current += 1
    
    self.__size += 1
    print('node has been added')
    
  
  # --- to delete from any position in the linked list (default is last) ---
  def delete(self, pos: int = None):
    if self.__size == 0:
      print('List is empty')
      return
    
    if pos == None:
      pos = self.__size - 1
      
    
    if pos == 0:
      self.__head = self.__head.get_next()
      self.__size -= 1
      print('node is deleted')
      return
    
    
    done = False
    temp = self.__head
    current = 0
    
    while not done:
        
      if current == (pos - 1):
        temp.set_next(temp.get_next().get_next())
        self.__size -= 1
        done = True
        print('node is deleted')
        return
      
      temp = temp.get_next()
      current += 1
  
  
  # ---- to increase the size of the linked list ----
  def increase_size(self, addition: int = 5):
    self.__capacity += addition
    
  
  # --- to get the size of linked list ---
  def get_size(self):
    return self.__size
  
  
  # --- to reverse the linked list ---
  def reverse(self):
    curr_node, prev_node = self.__head, None
    
    while curr_node:
      next_node = curr_node.get_next()
      curr_node.set_next(prev_node)
      
      # incrementor
      prev_node = curr_node
      curr_node = next_node
    
    self.__head = prev_node
    # --- end: reverse() ---   

# ---- end of class ----
