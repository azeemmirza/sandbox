from node import DoublyNode

class DoublyLinkedList:
  # --- constructor ---
  def __init__(self, head: DoublyNode, capacity: int = 5):
    self.__head = head
    self.__capacity = capacity
    self.__size = 0 if head == None else 1
  
  
  # --- insert node in linked list
  def insert(self, data, position: int = None):
    self.__check_size()
    
    if position == None:
      position = self.__size
    
    node = DoublyNode(data)
    temp = self.__head
    done = False
    current = 1
    
    while not done:
      print(f'{temp.get_data()}')
      
      if current == position:
        temp.set_next(node)
        node.set_prev(temp)
        done = True
        break
      
      temp = temp.get_next()
      current += 1
    
    self.__size += 1
    print('node is added')
    # --- end: insert() ---
  
  
  # --- to delete the node from the position ---
  def delete(self, position: int = None):
    # if position is none, set the last node as default
    if position == None:
      position = self.__size - 1
    
    # if position is 0, simple case, delete right away
    if position == 0:
      self.__head = self.__head.get_next()
      self.__size -= 1
      print('node is deleted.')
      return
    
    temp = self.__head
    done = False
    current = 0
    
    while not done:
      if current == (position - 1):
        next_next = temp.get_next().get_next()
        
        temp.set_next(next_next)
        next_next.set_prev(temp)
        done = True
        
        print('node is deleted')
        return
        
      temp = temp.get_next()
      current += 1
    
    self.__size -= 1
    # --- end: delete() ---
  
  
  # ---- method for printing linked list ---
  def print(self):
    temp = self.__head
    eol = '<=>'
    while temp != None:
      eol = '\n' if temp.get_next() == None else eol
      print(f'[{temp.get_data()}]', end=eol)
      temp = temp.get_next()
    
    print()
    # --- end: print() ---
  
  # --- method to reverse the linked list
  def reverse(self):
    first = self.__head
    
    
    pass
  
  
  # --- to get the size of the linked list
  def get_size(self):
    return self.__size
    # --- end: get_size() ---
  
  
  # --- to increase the capacity of the linked list ---
  def increase_size(self, addition: int = 5):
    self.__capacity += addition
    # --- end: increase_size() ---
  
  
  # --- method for checking is list has a size ---
  def __check_size(self):
    if self.__size == self.__capacity:
      raise IndexError('LinkedList is full')
    
    # --- end: __check_size() ---

# --- end class --- #
