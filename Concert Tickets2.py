# second try. wrong. Time limit error

from typing import Union, List


class Node:
    def __init__(self, key):
        self.key = key
        # initially, no children of the node.
        # These left and right point to Tree class, in which there is a node.
        self.left = None
        self.right = None
        self.multiplicity = 1
        # if the same key is inserted in the tree below,
        # then multiplicity is incremented

    def __str__(self):
        s = f"{self.__class__.__name__}({self.key})"  # Node(10)
        return s

    def __repr__(self):
        cls_name = self.__class__.__name__
        rep = (f"{cls_name}({self.key});"
               f"\n{cls_name}({self.key}).left = {self.left !s};"
               f"\n{cls_name}({self.key}).right = {self.right !s};")
        return rep


class BinaryTree:

    def __init__(self, nodes: Union[List[Node], Node, None] = None):
        """
        the structure of this class:
        it contains a root, whose type is Node (or None if empty tree).
        the root has left and right children
        those children are again tree, containing their roots.

        :param nodes:
            list of nodes to include
            or a single node
            or None. this case is for place holder of a leaf
        """
        self.root = None  # one tree has one node called self.root, which connects to children
        self.height = -1  # due to place holder for AVL tree
        self.balance = 0
        # height difference, or balance factor
        # = height of the left child - height of the right child

        # insert the input nodes into the tree
        if type(nodes) is list:
            for node_elem in nodes:
                self.insert_node(node_elem)
        elif type(nodes) is Node:
            self.insert_node(nodes)
        else:  # None
            pass

    def __str__(self):
        # BinaryTree's root is Node(10)
        s = f"{self.__class__.__name__} with {self.root !s} root"
        return s

    def __repr__(self):
        cls_name = self.__class__.__name__
        try:
            rep = (f"{str(self)};"
                   f"\n{cls_name}({self.root !s}).left = {self.root.left !s};"
                   f"\n{cls_name}({self.root !s}).right = {self.root.right !s};")
        except AttributeError:
            # when the self.root is None.
            # This happens when the tree cls was created without nodes arguments
            # or for tree cls located below the leaves
            rep = (f"{str(self)};"
                   f"\nEmpty {cls_name};")
        return rep

    def __len__(self):
        """
        returns the sum of nodes, including multiplicity of each node
        """
        _root = self.root
        if _root is None:  # empty tree case
            return 0

        assert type(_root) is Node, f"{_root} is not the right type"  # sanity check
        l = _root.left
        r = _root.right
        result = _root.multiplicity + len(l) + len(r)
        return result

    @classmethod
    def gen_empty_tree(cls):
        new_inst = cls()  # make new instance of tree with empty node
        return new_inst

    def calibrate_height(self) -> None:
        """
        when a node is updated (i.e. added or deleted) within the tree cls,
        self.height is updated accordingly.
        this method updates the heights of a node,
        which is the root of a particular subtree.
        """
        # empty tree
        _root = self.root
        if _root is None:  # empty tree
            self.height = -1
            return

        # for non-empty tree
        left_tree = self.root.left
        right_tree = self.root.right

        self.height = 1 + max(left_tree.height, right_tree.height)
        return

    def calibrate_balance_factor(self):
        """
        when a node is updated (i.e. added or deleted) within the tree cls,
        self.balance is updated accordingly.
        this method updates the balance factor of a node,
        which is the root of a particular subtree.
        """
        # empty tree
        _root = self.root
        if _root is None:  # empty tree
            self.balance = 0
            return

        # for non-empty tree
        left_tree = self.root.left
        right_tree = self.root.right

        self.balance = left_tree.height - right_tree.height
        return

    def insert_node(self, new_node: Node) -> None:

        # sanity check
        assert type(new_node) is Node, f"wrong input type: {new_node}"

        _root = self.root
        if _root is None:  # empty tree
            self.root = new_node
            _root = self.root
            # empty tree as children
            _root.left = self.gen_empty_tree()
            _root.right = self.gen_empty_tree()
            self.calibrate_height()
            self.calibrate_balance_factor()
        elif new_node.key < _root.key:  # left child
            left_tree = _root.left
            # sanity check
            assert isinstance(left_tree, self.__class__), "wrong input type"
            left_tree.insert_node(new_node)
            self.calibrate_height()
            self.calibrate_balance_factor()
        elif new_node.key > _root.key:  # right child
            right_tree = _root.right
            # sanity check
            assert isinstance(right_tree, self.__class__), "wrong input type"
            right_tree.insert_node(new_node)
            self.calibrate_height()
            self.calibrate_balance_factor()
        else:  # same value
            _root.multiplicity += 1

        return

    def get_max(self) -> Union[None, Node]:
        """
        :returns
            the node with maximum key
            or None if empty tree
        """

        current_node = self.root
        if current_node is None:  # empty tree itself
            return current_node

        right_tree = current_node.right
        if len(right_tree) == 0:  # empty right tree
            return current_node
        else:  # non-empty right tree
            return right_tree.get_max()

    def get_min(self) -> Union[None, Node]:
        """
        :returns
            the node with minimum key
            or None if empty tree
        """

        current_node = self.root
        if current_node is None:  # empty tree itself
            return current_node

        left_tree = current_node.left
        if len(left_tree) == 0:  # empty right tree
            return current_node
        else:  # non-empty right tree
            return left_tree.get_min()

    def get_middle(self) -> Union[None, Node]:
        """
        :returns
            one of the following:
            1. the node with the largest key among those with smaller than self.root
            2. the node with the smallest key among those with larger than self.root
            3. None if empty tree
            4. None if the tree has 1 element: leaf case
        """
        current_node = self.root

        # return case 3
        if current_node is None:  # empty tree itself
            return current_node

        # return case 1
        middle_node = current_node.left.get_max()
        if middle_node is not None:
            return middle_node

        # return case 2
        middle_node = current_node.right.get_min()
        if middle_node is not None:
            return middle_node

        # return case 4
        assert len(self) == 0, "wrong implementation"
        return

    def delete_node(self, del_key: int) -> None:
        """
        we wish to remove or decrement the multiplicity of a node with key = del_key
        raise ValueError if del_key is not present in the whole tree
        """
        _root = self.root
        if _root is None:  # empty tree reached.
            raise ValueError(f"{del_key} is not present")

        if del_key == _root.key:
            _root.multiplicity -= 1
            if _root.multiplicity == 0:  # need to delete the node from the tree
                if _root.left.root is None and _root.right.root is None:  # _root is a leaf node
                    self.root = None
                    self.calibrate_height()
                    self.calibrate_balance_factor()
                else:  # _root has at least one child
                    middle_node = self.get_middle()
                    # sanity check
                    assert isinstance(middle_node, Node), f"middle_node is {middle_node}"

                    # use the attributes of middle_node to replace the _root Node
                    mid_key = middle_node.key
                    mid_mul = middle_node.multiplicity

                    # completely delete the middle_node located at the leaf
                    middle_node.multiplicity = 1
                    self.delete_node(mid_key)

                    # replace the root with the new middle_node value
                    self.root.key = mid_key
                    self.root.multiplicity = mid_mul
        elif del_key < _root.key:  # left child
            _root.left.delete_node(del_key)
            self.calibrate_height()
            self.calibrate_balance_factor()
        elif del_key > _root.key:  # right child
            _root.right.delete_node(del_key)
            self.calibrate_height()
            self.calibrate_balance_factor()
        else:
            raise ValueError(f"{del_key} is not present")

        return

    def search_node(self, node_key: int) -> Union[int, Node]:
        """
        :param node_key:
            key value of a node that we wish to search
        :return:
            -1 if _node_key is not present in the tree cls
            Node instance with the key = node_key
        """

        _root = self.root
        if _root is None:
            return -1
        elif _root.key == node_key:
            return _root
        elif node_key > _root.key:  # right child
            return _root.right.search_node(node_key)
        elif node_key < _root.key:  # left child
            return _root.left.search_node(node_key)
        else:  # sanity check
            raise ValueError()

    def tree_print(self, level=0, prefix=''):

        _root = self.root
        if _root is not None:
            print('-' * level * 2,
                  prefix,
                  _root.key,
                  "[" + str(self.height) + ":" + str(self.balance) + "]")
            left_tree = _root.left
            right_tree = _root.right
            left_tree.tree_print(level + 1, "<")
            right_tree.tree_print(level + 1, ">")


class AVLTree(BinaryTree):

    # search, insert, delete operation
    # to ensure self-balancing, we need rotation based on height difference

    def __init__(self, nodes: Union[List[Node], Node, None] = None):
        super(AVLTree, self).__init__(nodes)

    def right_rotate(self):
        # Rotate X, which is left on self to right of Y
        # this method also calibrates heights and balances
        Y = self.root
        X = Y.left.root
        B = X.right.root

        # rotate by assigning variables
        self.root = X
        X.right.root = Y
        Y.left.root = B

        # calibrate height and balance factor of the three trees (X self, Y, B)
        Y_tree = X.right
        B_tree = Y.left
        B_tree.calibrate_height()
        Y_tree.calibrate_height()
        self.calibrate_height()
        B_tree.calibrate_balance_factor()
        Y_tree.calibrate_balance_factor()
        self.calibrate_balance_factor()

    def left_rotate(self):
        # Rotate X, which is right on self to left of Y
        # this method also calibrates heights and balances
        Y = self.root
        X = Y.right.root
        B = X.left.root

        # rotate by assigning variables
        self.root = X
        X.left.root = Y
        Y.right.root = B

        # calibrate height and balance factor of the three trees (X self, Y, B)
        Y_tree = X.left
        B_tree = Y.right
        B_tree.calibrate_height()
        Y_tree.calibrate_height()
        self.calibrate_height()
        B_tree.calibrate_balance_factor()
        Y_tree.calibrate_balance_factor()
        self.calibrate_balance_factor()

    def rebalance_tree(self):
        """
        Rebalance the whole tree by using rotation.
        This method only rebalance the whole tree structure.
        We need to calibrate height and balance factor for insertion and deletion.
        """

        # search the deepest
        if self.balance < -1:  # right heavy. unbalanced
            right_tree = self.root.right
            right_tree.rebalance_tree()
        elif self.balance > 1:  # left heavy. unbalanced
            left_tree = self.root.left
            left_tree.rebalance_tree()
        else:  # well balanced. No need to change
            return

        # check if we need rotate
        if self.balance < -1:  # right heavy. unbalanced
            right_tree = self.root.right
            if right_tree.balance > 0:  # right child is left heavy
                # right rotate
                right_tree.right_rotate()
            self.left_rotate()
        elif self.balance > 1:  # left heavy. unbalanced
            left_tree = self.root.left
            if left_tree.balance < 0:  # left child is right heavy
                left_tree.left_rotate()
            self.right_rotate()
        else:  # well balanced. No need to change
            return

    def insert_node(self, new_node: Node) -> None:

        # insert node
        super(AVLTree, self).insert_node(new_node)

        # calibrate height and balance of the tree
        self.rebalance_tree()

        return

    def delete_node(self, del_key: int) -> None:

        # delete node
        super(AVLTree, self).delete_node(del_key)

        # calibrate height and balance of the tree
        self.rebalance_tree()


class ModifiedAVLTree(BinaryTree):

    def __init__(self, nodes: Union[List[Node], Node, None] = None):
        super(ModifiedAVLTree, self).__init__(nodes)

    def delete_node(self, del_key: int) -> None:
        if del_key == -1:  # do nothing
            # this is for pop_price method.
            return
        else:  # work as normal
            super(ModifiedAVLTree, self).delete_node(del_key)

    def pop_price(self, target_node_key: int) -> int:
        """
        work just like pop method in list

        :param target_node_key:
            int value of a key of a node to be decremented or deleted in the tree cls
        :return:
            target_node_key if present in the tree as root.key,
            the biggest among the smaller root.key if not present
            -1 if no smaller nodes
        """
        # initialisation
        price = -1
        _root = self.root

        # base cases
        if _root is None:  # empty tree
            return price

        while True:  # iterative method.
            if target_node_key < _root.key:  # look for left tree
                left_tree_node = _root.left.root
                if left_tree_node is None:  # empty left child. no cheaper ticket
                    self.delete_node(price)
                    return price
                else:  # non-empty left child
                    _root = left_tree_node
            elif target_node_key > _root.key:  # right child. can afford this ticket
                price = _root.key
                right_tree_node = _root.right.root
                if right_tree_node is None:  # empty right child.
                    # no more expensive ticket.
                    # price matched
                    self.delete_node(price)
                    return price
                else:  # non-empty right child
                    _root = right_tree_node
            else:  # same value as _root.key
                price = target_node_key
                self.delete_node(price)
                return price


n, m = list(map(int, input().split()))
h = list(map(int, input().split()))  # ticket price
t = list(map(int, input().split()))  # max price customers can afford


# t1 = time.perf_counter()
# with open("test_input.txt") as f:
#     input_ = f.readline
#     n, m = list(map(int, input_().split()))
#     h = list(map(int, input_().split()))  # ticket price
#     t = list(map(int, input_().split()))  # max price customers can afford

nodes_input = [Node(elem) for elem in h]
tree = ModifiedAVLTree(nodes_input)
ans = [tree.pop_price(target) for target in t]
print(*ans, sep='\n')
# t2 = time.perf_counter()
# print(t2 - t1)

# root = Node(10)
# leaf = Node(9)
# tree = AVLTree(root)
# tree.insert_node(leaf)
# for i in range(5):
#     tree.insert_node(Node(i))
# tree.tree_print()
# leaf2 = Node(30)
# tree.insert_node(leaf2)
# tree.delete_node(30)
# tree.delete_node(21)
# tree.delete_node(23)
