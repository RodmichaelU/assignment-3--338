import sys

class Stack:
    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next_node = next_node

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = self.Node(data, self.head)
        self.head = new_node

    def pop(self):
        if not self.head:
            raise Exception("Stack is empty")
        data = self.head.data
        self.head = self.head.next_node
        return data

    def peek(self):
        if not self.head:
            raise Exception("Stack is empty")
        return self.head.data

    def is_empty(self):
        return not bool(self.head)

def evaluate_expression(expr):
    stack = Stack()

    for token in reversed(expr):
        if token.isdigit():
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 / operand2)
        else:
            pass

    if stack.is_empty():
        raise Exception("Expression is empty")
    else:
        return stack.pop()

if __name__ == '__main__':
    expr = sys.argv[1]
    print(expr)
    result = evaluate_expression(expr)
    print(result)
