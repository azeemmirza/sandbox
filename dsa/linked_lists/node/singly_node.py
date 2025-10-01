class SinglyNode:
  def __init__(self, data = None, next: 'SinglyNode' = None):
    self.__data = data
    self.__next = next
  
  def set_data(self, data):
    self.__data = data
    
  def get_data(self):
    return self.__data
  
  def set_next(self, next: 'SinglyNode'):
    self.__next = next
  
  def get_next(self):
    return self.__next
