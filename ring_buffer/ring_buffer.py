from doubly_linked_list import DoublyLinkedList, ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        counter = 0
        while self.current:
            list_buffer_contents.append(self.current.value)
            if self.current.next:
                self.current = self.current.next
            counter += 1
            if counter == len(self.storage):
                break


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

""" test code"""

buffer = RingBuffer(5)
buffer.append('a')
print(buffer.get())
buffer.append('b')
print(buffer.get())
buffer.append('c')
print(buffer.get())
buffer.append('d')
print(buffer.get()) # ['a', 'b', 'c', 'd'])
buffer.append('e')
print(buffer.get()) # ['a', 'b', 'c', 'd', 'e']
buffer.append('f')
print(buffer.storage.length) # 5)
print(buffer.get()) # ['f', 'b', 'c', 'd', 'e'])
