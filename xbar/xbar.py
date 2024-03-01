
"""
Definition of tree objects (with arbitrarily many children).
"""

# This class is a modification/extension of https://stackoverflow.com/a/28015122.


class Tree(object):
    """Generic tree node."""

    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        self.parent = None
        if children is not None:
            for child in children:
                child.parent = self
                self.add_child(child)

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.printout_oneline()

    # --------------
    # Traversals
    # --------------

    def preorder(self):
        """Pre-order traversal:
        First yield the node itself, then recurse through its children.

        :return: A list of tree nodes in pre-order.
        :rtype lst(Tree)"""
        result = []
        stack = [self]

        while stack:
            current_node = stack.pop()
            result.append(current_node)

            # Add children to the stack in reverse order to simulate pre-order traversal
            stack.extend(reversed(current_node.children))

        return result
        # pass

    def postorder(self):
        """Post-order traversal:
        First recurse through the node's children, then yield the node itself.

        :return: A list of tree nodes in post-order.
        :rtype lst(Tree)"""

        result = []
        stack1 = [self]
        stack2 = []

        while stack1:
            current_node = stack1.pop()
            stack2.append(current_node)

            # Add children to the first stack to simulate post-order traversal
            stack1.extend(current_node.children)

        while stack2:
            result.append(stack2.pop())

        return result

        # pass

    def inorder(self):
        """In-order traversal:
        First recurse through into the left child, then visit the node itself, then recurse into the other children in
        order.

        :return: A list of tree nodes in in-order.
        :rtype lst(Tree)"""
        res = []
        if len(self.children) > 0:
            res += self.children[0].inorder()
        res.append(self)
        for i in range(1, len(self.children)):
            res += self.children[i].inorder()
        return res

    @staticmethod
    def names(nodelist):
        """Given a list of nodes, return a list consisting of the names of the nodes.

        :param nodelist: A list of tree nodes to extract the names from.
        :type nodelist: lst(Tree)
        :return: A list of the names of the tree nodes.
        :rtype lst(str)"""
        return [node.name for node in nodelist]

    # --------------
    # Printout methods
    # --------------

    def printout_oneline(self):
        """One-line string representation.

        :return a one-line printout of the tree structure
        :rtype str"""
        return "[" + self.name + " " + ", ".join([child.printout_oneline() for child in self.children]) + "]"

#endregion

    def printout_plain(self, ind_level=0):
        """Simple two-dimensional string representation with increasing indentation and no visual edges.

        :return a plain printout of the tree structure
        :rtype str"""
        # For each level of nesting, increase the indentation by three whitespaces.
        ret = ind_level * "   " + self.name + "\n"
        for child in self.children:
            ret += child.printout_plain(ind_level + 1)
        return ret

    def printout_fancy(self, indent="", last_sibling=True):
        """Fancy two-dimensional string representation with increasing indentation and edges between siblings.

        :return a fancy printout of the tree structure
        :rtype str"""
        # Start with the root by prefixing its name with "|--".
        # Then loop through the node's children, if it has any:
        # If self has no siblings "to the right" (i.e. nodes on the same horizontal level vertically further down), then
        # for its children simply increase the indentation by three whitespaces and recursively descend into the child.
        # Otherwise, if there are more nodes on the level of self downwards the tree, include in the indentation the
        # vertical line "|" continuing downwards the tree to connect to the next sibling of self.
        # While ranging through the children, pass on to each of them the knowledge whether or not they are themselves
        # the youngest among their siblings, which is the case iff they are the last element in the list.

        # v1
        ret = indent + "|--" + self.name + "\n"
        if self.children:
            if last_sibling:
                for i, child in enumerate(self.children):
                    ret += child.printout_fancy(indent + "   ", i == len(self.children) - 1)
            else:
                for i, child in enumerate(self.children):
                    ret += child.printout_fancy(indent + "|  ", i == len(self.children) - 1)
                ret += indent + "|  " + "\n"
        return ret

        # # v2
        # ret = indent + "|  \n" + indent + "|--" + self.name + "\n"
        # if self.children:
        #     if last_sibling:
        #         for i, child in enumerate(self.children):
        #             ret += child.printout_fancy(indent + "   ", i == len(self.children) - 1)
        #     else:
        #         for i, child in enumerate(self.children):
        #             ret += child.printout_fancy(indent + "|  ", i == len(self.children) - 1)
        # return ret

        # # v3
        # ret = indent + "|--" + self.name + "\n"
        # for i, child in enumerate(self.children):
        #     if last_sibling:
        #         ret += child.printout_fancy(indent + "   ", i == len(self.children)-1)
        #     else:
        #         ret += child.printout_fancy(indent + "|  ", i == len(self.children)-1)
        # return ret

    # ----------------------
    # Properties of nodes
    # ----------------------

    def get_category(self):
        """Return the syntactic category of a node.

        :return the syntactic category of self
        :rtype str"""
        # Category of a node is given by chopping off the last character (projection level number) of its name.
        if not self.is_terminal():
            return self.name[:-1]
        else:
            return self.parent.category  # for terminal selfs, return category of parent (head)

    def set_category(self, cat):
        self.name = cat + self.name[-1]

    category = property(get_category, set_category)

    def get_level(self):
        """Return the projection level of a node.

        :return the projection level of self
        :rtype int"""
        # Projection level of a node is given by extracting as an integer the last character (= proj.level) of its name.
        if not self.is_terminal():
            return int(self.name[len(self.name) - 1])
        else:
            return self.parent.level  # for terminal selfs, return proj. level of parent (head)

    def set_level(self, lvl):
        self.name = self.name[:-1] + str(lvl)

    level = property(get_level, set_level)

    def same_cat_as_parent(self):
        """Check whether a self is of the same syntactic category as its parent.

        :return true if self is of the same syntactic category as its parent
        :rtype bool"""
        return (self.parent is None or  # to prevent None error in case self to be checked is root
                self.category == self.parent.category)
                
    # ----------------------
    # Boolean checks on nodes
    # ----------------------

    def is_terminal(self):
        """Check whether a node is a terminal node (word).
        A node is terminal iff it has no children.

        :return true if self is a terminal node
        :rtype bool"""
        return len(self.children) == 0

    def is_unary(self):
        """Check whether a node branches unary.
        A node branches unary iff it has 1 child.

        :return true if self branches unary
        :rtype bool"""
        return len(self.children) == 1

    def is_binary(self):
        """Check whether a node branches binary.
        A node branches binary iff it has 2 children.

        :return true if self branches binary
        :rtype bool"""
        return len(self.children) == 2

    # ----------------------
    # Check projection levels
    # ----------------------

    def is_xbar(self):
        """Check whether a node conforms to the definitions of an X-bar structure.
        A node conforms to X-bar structure iff it is a proper XP, X' or X.

        :return true if self conforms to X-bar structure
        :rtype bool"""

        return (
                self.is_phrase_projection() or
                self.is_bar_projection() or
                self.is_head_projection()
        )
        # pass

    def is_phrase_projection(self):
        """Check whether a node is a phrase (XP).
        A node is an XP iff it has projection level 2 and either
        - no specifier (unary branching into X') or
        - a specifier on the left (binary branching into a specifier YP and X').

        :return true if self conforms to a phrase projection
        :rtype bool"""
        return (self.level == 2 and
                (self.is_no_specifier_structure() or self.is_specifier_structure()))

    def is_bar_projection(self):
        """Check whether a node is a bar (X')
        A node is an X' iff it has projection level 1 of the same category as its XP and either
        - no adjuncts or complements (unary branching into the head X) or
        - a complement (binary branching into head X on the left and a complement YP on the right) or
        - an adjunct to the left or an adjunct to the right (binary branching into the adjunct YP and a second X'
        projection).

        :return true if self conforms to a bar projection
        :rtype bool"""

        return (self.level == 1 and
                self.parent is not None and  # Ensure there is a parent
                self.category == self.parent.category and
                (self.is_no_adjunct_or_complement_structure() or
                 self.is_complement_structure() or
                 self.is_adjunct_structure()))

    def is_head_projection(self):
        """Check whether a node is a head (X).
        A node is an X iff it has projection level 0 of the same category as its X' and unary branches into a
        terminal node.

        :return true if self conforms to a head projection
        :rtype bool"""
        return (self.level == 0 and self.category == self.parent.category and
                self.is_unary() and self.children[0].is_terminal())

    # ----------------------
    # Check structural constraints for the respective projection levels
    # ----------------------

    def is_no_specifier_structure(self): # done
        """Check whether a node is an XP structure with no specifier (unary branching into X').

        :return true if self is an XP structure with no specifier
        :rtype bool"""
        return (self.is_unary() and self.children[0].is_bar_projection() and
                self.children[0].get_category() == self.get_category())

    def is_specifier_structure(self): # done
        """Check whether a node is an XP with specifier structure (binary branching into specifier YP on left and X' on
        right).

        :return true if self is a specifier structure
        :rtype bool"""

        return (
                self.is_binary() and
                isinstance(self.children[0], Tree) and
                self.children[0].is_phrase_projection() and
                self.children[1].is_bar_projection()
        )

    def is_no_adjunct_or_complement_structure(self): # done
        """Check whether a node is an X' structure with no complementation or adjunction (unary branching into head X).

        :return true if self is a X' with no adjunct or compleement
        :rtype bool"""
        return (self.is_unary() and
                self.children[0].is_head_projection())

    def is_complement_structure(self): # done
        """Check whether a node is an X' with head-complement structure (binary branching into head X on left and
        complement YP on right).

        :return true if self is a head-complement structure
        :rtype bool"""
        return (self.is_binary() and
                # head X on left, complement YP on right
                self.children[0].is_head_projection() and self.children[1].is_phrase_projection())

    def is_adjunct_structure(self):
        """Check whether a node is an X' with adjunctive structure (binary branching into adjunct YP on left and X' on
        right or vice versa).

        :return true if self is an adjunct structure
        :rtype bool"""
        # Check if the node is binary
        if not self.is_binary():
            return False

        return self.children[0].is_phrase_projection() and self.children[1].is_bar_projection() or \
               self.children[0].is_bar_projection() and self.children[1].is_phrase_projection()

    def is_head_structure(self):
        """Check whether a node is an X head branching unary into a terminal node (word).

        :return true if self is a head structure
        :rtype bool"""
        return self.is_unary() and self.children[0].is_terminal()


if __name__ == '__main__':
    the_cat_on_the_mat = \
        Tree('N2', [
            Tree('D2', [Tree('D1', [Tree('D0', [Tree('the')])])]),
            Tree('N1', [
                Tree('N1', [Tree('N0', [Tree('cat')])]),
                Tree('P2', [Tree('P1', [
                    Tree('P0', [Tree('on')]),
                    Tree('N2', [
                        Tree('D2', [Tree('D1', [Tree('D0', [Tree('the')])])]),
                        Tree('N1', [Tree('N0', [Tree('mat')])])
                    ])
                ])])
            ])
        ])
    print(the_cat_on_the_mat.printout_fancy())
    print(the_cat_on_the_mat.is_xbar())
    # pass
