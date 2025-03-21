class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.size() > 0:
            return self.items[-1]
        return None

    def pop(self):
        if self.size() > 0:
            return self.items.pop()
        return None
    
    def sort_stack(self):
        temp_stack = Stack()

        while not self.is_empty():
            # Pop the top element from the original stack
            temp = self.pop()

            # Move elements from temp_stack back to self until we find the right place for temp
            while not temp_stack.is_empty() and temp_stack.peek() > temp:
                self.push(temp_stack.pop())

            # Place temp in its correct position
            temp_stack.push(temp)

        # Move elements back to self so it's sorted
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        
