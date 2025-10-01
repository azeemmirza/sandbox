from .singly_node import SinglyNode

class DoublyNode(SinglyNode):
  # --- constructor ---
  def __init__(self, data=None, prev = None, next = None):
    super().__init__(data, next)
    self.__prev = prev
    # --- end: __init__() ---
  
  
  # --- get previous node ---
  def get_prev(self):
    return self.__prev
  # --- end: get_prev() ---
  
  
  # --- set previous node ---
  def set_prev(self, prev: 'DoublyNode'):
    self.__prev = prev
    # --- end: set_node() ---
