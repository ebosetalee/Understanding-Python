class TreeNode:
    def __init__(self, value):
        """
        Initialize the Tree Node here
        """
        self.value = value
        self.children = None


class Tree:
    def __init__(self, value):
        """
        Initialize the Tree here
        """
        self.value = value
        self.parent = None
        self.children = []

    def levels(self):
        """"
        Takes account of the number of parents in the tree
        :returns: the number of lineage before the child
        """
        level = 0
        parents = self.parent
        while parents:
            level += 1
            parents = parents.parent
        return level

    def add_child(self, child):
        """"
        Adds descendant to the tree
        :param child: value or node to be added
        """
        try:
            child.parent = self
        except AttributeError:
            child = TreeNode(child)
            child.parent = self
        finally:
            self.children.append(child)

    def display(self):
        """"
        Prints the values in the tree
        """
        spaces = ' ' * self.levels() * 2
        prefix = spaces + "|-" if self.parent else ""
        print(prefix + self.value)
        if self.children:
            for child in self.children:
                try:
                    child.display()
                except AttributeError:
                    print("  " + prefix + child.value)


root = Tree("Electronics")

laptop = Tree("Laptop")

mac = Tree("Mac")
mac.add_child("Air")
mac.add_child("pro")

laptop.add_child(mac)
laptop.add_child("Surface")
laptop.add_child("Thinkpad")

cellphone = Tree("Cell Phone")
cellphone.add_child("iPhone")
cellphone.add_child("Google Pixel")
cellphone.add_child("Vivo")

tv = Tree("TV")
tv.add_child("Samsung")
tv.add_child("LG")

root.add_child(laptop)
root.add_child(cellphone)
root.add_child(tv)

root.display()
