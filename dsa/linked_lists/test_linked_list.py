import unittest
from linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.node1 = Node('001')
        self.ll = LinkedList(self.node1, capacity=5)

    def test_initialization(self):
        self.assertEqual(self.ll.get_size(), 1)
        self.assertEqual(self.ll._LinkedList__head.data, '001')

    def test_insert_end(self):
        self.ll.insert('002')
        self.assertEqual(self.ll.get_size(), 2)
        self.assertEqual(self.ll._LinkedList__head.next.data, '002')

    def test_insert_at_position(self):
        self.ll.insert('002')
        self.ll.insert('003', 1)
        self.assertEqual(self.ll._LinkedList__head.next.data, '003')

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
        self.assertEqual(self.ll._LinkedList__head.data, '002')
        self.assertEqual(self.ll.get_size(), 1)

    def test_delete_last(self):
        self.ll.insert('002')
        self.ll.insert('003')
        self.ll.delete()
        self.assertEqual(self.ll.get_size(), 2)
        self.assertIsNone(self.ll._LinkedList__head.next.next)

    def test_delete_empty(self):
        self.ll.delete(0)
        self.ll.delete(0)
        self.assertEqual(self.ll.get_size(), 0)
        self.ll.delete(0)  # Should not raise

    def test_increase_size(self):
        old_capacity = self.ll._LinkedList__capacity
        self.ll.increase_size(3)
        self.assertEqual(self.ll._LinkedList__capacity, old_capacity + 3)

if __name__ == '__main__':
    unittest.main()
