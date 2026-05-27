import unittest

from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList

from node import SinglyNode, DoublyNode

class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.node1 = SinglyNode('001')
        self.ll = SinglyLinkedList(self.node1, capacity=5)

    def test_initialization(self):
        self.assertEqual(self.ll.get_size(), 1)
        self.assertEqual(self.ll._SinglyLinkedList__head.data, '001')

    def test_insert_end(self):
        self.ll.insert('002')
        self.assertEqual(self.ll.get_size(), 2)
        self.assertEqual(self.ll._SinglyLinkedList__head.next.data, '002')

    def test_insert_at_position(self):
        self.ll.insert('002')
        self.ll.insert('003', 1)
        self.assertEqual(self.ll._SinglyLinkedList__head.next.data, '003')

    def test_insert_full(self):
        self.ll.insert('002')
        self.ll.insert('003')
        self.ll.insert('004')
        self.ll.insert('005')
        with self.assertRaises(IndexError):
            self.ll.insert('006')

    def test_delete_head(self):
        self.ll.insert('002')
        self.ll.delete(0)
        self.assertEqual(self.ll._SinglyLinkedList__head.data, '002')
        self.assertEqual(self.ll.get_size(), 1)

    def test_delete_last(self):
        self.ll.insert('002')
        self.ll.insert('003')
        self.ll.delete()
        self.assertEqual(self.ll.get_size(), 2)
        self.assertIsNone(self.ll._SinglyLinkedList__head.next.next)

    def test_delete_empty(self):
        self.ll.delete(0)
        self.ll.delete(0)
        self.assertEqual(self.ll.get_size(), 0)
        self.ll.delete(0)  # Should not raise

    def test_increase_size(self):
        old_capacity = self.ll._SinglyLinkedList__capacity
        self.ll.increase_size(3)
        self.assertEqual(self.ll._SinglyLinkedList__capacity, old_capacity + 3)

if __name__ == '__main__':
    # unittest.main()]
    
    print('singly linked list testing')
    node_one = SinglyNode('001')
    single_ll = SinglyLinkedList(node_one)
    
    single_ll.insert('002')
    single_ll.insert('003')
    
    single_ll.print()
    
    single_ll.reverse()
    single_ll.print()
    
    print('doubly linked list testing')
    double_node = DoublyNode('01')
    double_ll = DoublyLinkedList(double_node)
    
    double_ll.insert('02')
    double_ll.insert('03')
    
    double_ll.print()
    
    double_ll.delete()
    
    double_ll.print()
    