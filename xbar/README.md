Project Tasks:

This project provides functionalities for constructing, analyzing, and validating tree structures based on X-bar theory principles.

**Functions:**

1. Tree Representation & Manipulation:

- The Tree class represents tree nodes with attributes like name, children, and parent.
- Methods like `add_child` and `printout_*` build and visualize the tree structure.

2. X-bar Validation:

- The `is_xbar(self)` method checks if a tree adheres to X-bar theory constraints:
  - Verifying projection levels (`X0`, `X'`, `XP`).
  - Validating structural constraints for each node (e.g., _specifiers_, _adjuncts_, _complements_).

3. Tree Traversal:

- Methods like `preorder`, `postorder`, and `inorder` allow visiting nodes in different orders for various operations.

4. Node Properties and Checks:

- Getters and setters like `get_category(self)` and `set_level(self)` access and modify node properties.
- Methods like `is_terminal(self)` and `is_binary(self)` check specific node characteristics.

5. Structural Constraint Checks:

- Specific methods verify that each node adheres to the expected structure based on its projection level:
  - XP (Phrase projection):
    - Must have a head (e.g., a noun phrase must have a noun as its head).
    - May have specifiers (determiners, adjectives) and complements (direct objects, prepositional phrases).
  - X' (Bar projection):
    - Often has a specifier and complements the head of its parent XP.
  - X (Head projection):
    - Represents the core syntactic category of a phrase (e.g., noun, verb).
