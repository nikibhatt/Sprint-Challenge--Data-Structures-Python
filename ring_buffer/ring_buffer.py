from doubly_linked_list import DoublyLinkedList, ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current:
            self.storage.value = item
        else:
            self.storage.head = self.current
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        for i in range(0, self.capacity):
                if current_node:
                    list_buffer_contents.append(current_node.value)
                    current_node = current_node.next

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

buffer = RingBuffer(3)
print(buffer.get())

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())
