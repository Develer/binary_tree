from binary_tree_renderer import PILTreeRenderer


class Node():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add(self, value):
        if (value > self.data):
            if (self.right is None):
                self.right = Node(value)
            else:
                self.right.add(value)
        if (value < self.data):
            if (self.left is None):
                self.left = Node(value)
            else:
                self.left.add(value)

    def get_node(self, value):
        if (value == self.data):
            return self.data
        elif (self.right and value > self.data):
            return self.right.get_node(value)
        elif (self.left and value < self.data):
            return self.left.get_node(value)
        else:
            return None

    def __str__(self):
        return str((self.data, str(self.left), str(self.right)))


def main():
    bin_tree = Node(10)
    chain = [6,2,8,1,3,7,9, 14,12,16,11,13,15,17]

    for i in chain:
        bin_tree.add(i)

    renderer = PILTreeRenderer()
    renderer.render_tree(bin_tree)

if __name__ == "__main__":
    main()