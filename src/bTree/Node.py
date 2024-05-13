class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


    def __str__(self):
        return f"VALUE: {self.value} LEFT: {self.left} RIGHT: {self.right}"

if __name__ == '__main__':
    n = Node(1)
    print(n)


