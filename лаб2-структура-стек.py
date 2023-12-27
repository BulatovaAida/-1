class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        """Добавляет элемент в стек."""
        self.stack.append(item)

    def pop(self):
        """Удаляет элемент из стека."""
        return self.stack.pop()

    def peek(self):
        """Возвращает первый элемент стека без его удаления."""
        if not self.stack:
            return None
        return self.stack[-1]

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.stack)

    def is_empty(self):
        """Возвращает `True`, если стек пуст."""
        return not self.stack

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # 3
print(stack.pop())  # 3
print(stack.peek())  # 2

print(stack.size())  # 2
print(stack.is_empty())  # False
