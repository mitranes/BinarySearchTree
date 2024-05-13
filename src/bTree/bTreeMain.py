from src.bTree.Node import Node


class BTree:
    def __init__(self):
        self.root = None

    def add(self, localRoot, val):
        if localRoot is None:
            localRoot = Node(val)
            return localRoot
        elif localRoot.value > val:
            localRoot.left = self.add(localRoot.left, val)
            return localRoot
        elif localRoot.value < val:
            localRoot.right = self.add(localRoot.right, val)
            return localRoot


    def insert(self, val):
        if self.root is not None:
            self.add(self.root, val)
        else:
            self.root = Node(val)

    def preOrder_traverse(self, localRoot):
        if localRoot is None:
            return print("Tree is empty or no children")
        else:
            print("Node: ", localRoot.value)
            self.preOrder_traverse(localRoot.left)
            self.preOrder_traverse(localRoot.right)

    def inOrder_traverse(self, localRoot):
        #go left subtree until you can't go anymore, visit root, go right subtree.
        if localRoot is None:
            return print("Tree is Empty or no children")
        else:
            self.inOrder_traverse(localRoot.left)
            print("InOrder Node: ", localRoot.value)
            self.inOrder_traverse(localRoot.right)

    def postOrder_traverse(self,localRoot):
        #go left subtree, then go right subtree, then visit root
        if localRoot is None:
            return print("Tree is Empty or no children")
        else:
            self.postOrder_traverse(localRoot.left)
            self.postOrder_traverse(localRoot.right)
            print("PostOrder Node: ", localRoot.value)


    def delete(self, localRoot, val):
        if localRoot is None:
            return None
        if val < localRoot.value:
            localRoot.left = self.delete(localRoot.left, val)
        elif val > localRoot.value:
            localRoot.right = self.delete(localRoot.right, val)
        else:
            if localRoot.left is None:
                return localRoot.right
            elif localRoot.right is None:
                return localRoot.left
            else:
                #search for largest child in Left Subtree
                localRoot.value = self.findLargestChildInLT(localRoot.left)
                return localRoot

    def findLargestChildInLT(self, localRoot):
        #largest item in left subtree
        if localRoot.right is not None:
            localRoot = localRoot.right
        self.delete(localRoot, localRoot.value)
        return localRoot.value

    def search(self, localRoot, val):
        if localRoot is None:
            return False
        if val == localRoot.value:
            return True
        elif val < localRoot.value:
            return self.search(localRoot.left, val)
        else:
            return self.search(localRoot.right, val)

    


if __name__ == "__main__":
    tree = BTree()
    tree.insert(10)
    tree.insert(7)
    tree.insert(15)
    tree.insert(17)
    tree.insert(4)
    tree.insert(9)
    tree.insert(8)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.preOrder_traverse(tree.root)
    print("INORDER TRAVERSE")
    tree.inOrder_traverse(tree.root)
    tree.delete(tree.root, 7)
    print("The NEW Tree looks like this: ")
    tree.preOrder_traverse(tree.root)
    print("Search Answer: ", tree.search(tree.root,18))



