class LinkedList:
    def __init__(self):
        """
            Create a new LinkedList
        """
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, element, pos):
        """
            Insert an element into this list

            element: The element to insert
            pos: The position to insert (0 being the start)
            return: The modified LinkedList
            raise: IndexError if pos is outside of the list
        """
        if pos < 0 or pos > self.length:
            raise IndexError("Position ausserhalb der Liste")
        
        element.list = self
        
        if self.length == 0:
            element.previous = None
            element.next = None
            self.head = element
            self.tail = element
        elif pos == 0:
            element.previous = None
            element.next = self.head
            self.head.previous = element
            self.head = element
        elif pos == self.length:
            element.previous = self.tail
            element.next = None
            self.tail.next = element
            self.tail = element
        else:
            current = self.head
            for _ in range(pos):
                current = current.next
            prev = current.previous
            element.previous = prev
            element.next = current
            prev.next = element
            current.previous = element
        
        self.length += 1
        return self

    def remove(self, pos):
        """
            Remove an element from this list

            pos: The position of the element to remove
            returns: The modified LinkedList
            raise: IndexError if pos is outside of the list
        """
        if pos < 0 or pos >= self.length:
            raise IndexError("Position ausserhalb der Liste")
        current = self.head
        for _ in range(pos):
            current = current.next
        
        current.remove()
        return self

    def find(self, value):
        """
            Find an element in this list

            value: The value of the element to find
            returns: The position of the first occurrence of such an element or -1 if not found
        """
        node = self.head
        idx = 0
        while node is not None:
            if node.value == value:
                return idx
            node = node.next
            idx += 1
        return -1

    def __getitem__(self, pos):
        """
            Return an element at a specific position in the list

            pos: The position of the element to return (0 being the first)
            return: The element 
            raise: IndexError if pos is outside of the list
        """
        if pos < 0:
            raise IndexError("Position ausserhalb der Liste")
        if pos >= self.length:
            raise IndexError("Position ausserhalb der Liste")

        node = self.head
        for _ in range(pos):
            node = node.next
        return node

class LinkedListElement:
    # Pointer to next element in LinkedList
    next = None
    
    # Pointer to previous element in LinkedList
    previous = None

    def __init__(self, value):
        """
            Create a new LinkedListElement with value "value"
        """
        self.value = value

    def remove(self):
        """
            Remove this item from a LinkedList
        """
        lst = self.list
        
        if self.previous is not None:
            self.previous.next = self.next
        if self.next is not None:
            self.next.previous = self.previous
        
        if lst is not None:
            if lst.head is self:
                lst.head = self.next
            if lst.tail is self:
                lst.tail = self.previous
            lst.length -= 1
        
        self.list = None
        self.next = None
        self.previous = None

    def insert(self, element):
        """
            Insert an element after this element

            element: The element to insert
        """
        lst = self.list
        
        element.previous = self
        element.next = self.next
        if self.next is not None:
            self.next.previous = element
        self.next = element
        
        if lst is not None:
            element.list = lst
            if lst.tail is self:
                lst.tail = element
            lst.length += 1


if __name__ == "__main__":
    # Create a new LinkedList
    l = LinkedList()

    # Create a new LinkedListElement
    e1 = LinkedListElement(23)
    assert e1.value == 23, "LinkedListElement e1 does have the wrong value."

    # Insert LinkedListElement to beginning of l
    l.insert(e1, 0)
    assert l.find(23) >= 0, "Cannot find element with value '23' in l"
    assert l[0] == e1, "Element l[0] is not e1"

    # Insert another LinkedListElement at the start
    e2 = LinkedListElement(42)
    l.insert(e2, 0)
    assert l.find(42) >= 0, "Cannot find element with value '42' in l"
    assert l[0] == e2, "Element l[0] is not e2"
    assert l[1] == e1, "Element l[1] is not e1"

    # Remove e1 from LinkedList
    e1.remove()
    assert l.find(42) >= 0, "Cannot find element with value '42' in l"
    assert l.find(23) < 0, "Element with value '23' is still in l"
    assert l[0] == e2, "Element l[0] is not e2"
    try:
        assert l[1] == e1
    except IndexError:
        pass
    else:
        raise RuntimeError("Reading out of bounds should raise IndexError!")
    print("All tests passed. lessgooo")