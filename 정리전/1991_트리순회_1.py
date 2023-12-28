import sys

n = int(sys.stdin.readline())
tree = dict()

for i in range(n):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = left, right

#전위순회
def preorder(v):
    #자식이 있으면
    if v != ".":
        print(v, end="")
        preorder(tree[v][0])
        preorder(tree[v][1])

#중위순회
def inorder(v):
    #자식이 있으면
    if v != ".":
        inorder(tree[v][0])
        print(v, end="")
        inorder(tree[v][1])

#후위순회
def postorder(v):
    #자식이 있으면
    if v != ".":
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end="")
        
preorder('A')
print()
inorder('A')
print()
postorder('A')