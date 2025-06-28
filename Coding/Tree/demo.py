class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to print inorder traversal
def inorder(root):
    if root:
        print(root.data, end=' ')
        inorder(root.left)
        
        inorder(root.right)

# Create tree with 10 nodes
'''
        1
       / \
      2   3
     / \   \
    4   5   6
   /       / \
  7       8   9
               \
               10
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.right.right.left = Node(8)
root.right.right.right = Node(9)
root.right.right.right.right = Node(10)

# Print inorder traversal
st=[]
st.append(root)
while st:
    curr=st.pop()
    print(curr.data)
    if curr.right:
        st.append(curr.right)
    if curr.left:
        st.append(curr.left)
    
