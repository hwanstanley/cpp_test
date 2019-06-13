import collections
 
Node = collections.namedtuple('Node', ['left', 'right', 'value'])
 
def contains(root, value):
    if root.value == value:
        return True
    elif value > root.value and root.right is not None:
        return contains(root.right, value)
    elif value < root.value and root.left is not None:
        return contains(root.left, value)
    else:
        return False
       
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
       
print(contains(n2, 3))