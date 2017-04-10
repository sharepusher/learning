## Expression Trees
# Arithmetic expressions such as (9+3)*(8-4) can be represented using an expression tree.
# An expression Tree is a binary Tree, in which the operators are stored in the interior nodes
# and the operands(the variables or constant values) are stored in the leaves.
# Once constructed, an expression tree can be used to evaluated the expression or 
# for converting an infix expression to either prefix or postfix notation.

# NOTE: The structure of the expression tree is based on the order in which the operations are evaluated.

# The operator in each internal node is evaluated after both its left and right subtrees have been evaluated.
# Thus, the lower an operator is in a subtree, the earlier it will be evaluated.

# The root node contains the operator to be evaluated.

# while Python provides the eval() function for evaluating an arithmetic expression stored as a string
# The string must be parsed each time it's evaluated.
# This means the Python interpreter has to determin the order in which the operators are evaluated and then 
# perform each of the corresponding operations.
# One way it can do this is with the use of an expression tree.
# After the expression has been parsed and the tree constructed, the evaluation step is quite simple.
# This realtime evaluation of expression strings is not commonly available in compiled languages.
# When using such language and a user-supplied expression has to be evaluated, an express tree can be 
# constructed and evaluated to obtain the result.

## Expressioin Tree Abstract Data Type
# Arithmetic expressions can consist of both unary(-a, n!) and binary operators(a+b).
# We only consider expressions containing binary operators.

# 
