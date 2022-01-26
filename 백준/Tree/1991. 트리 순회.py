import sys

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

# 전위 순회 : 루트 - 왼쪽 - 오른쪽
def pre_order(node):
    print(node.item, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])

# 중위 순회 : 왼쪽 - 루트 - 오른쪽
def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        in_order(tree[node.right])

# 후위 순회 : 왼쪽 - 오른쪽 - 루트
def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.item, end='')

if __name__ == "__main__":

    N = int(sys.stdin.readline())
    tree = {}

    for _ in range(N):
        node, left, right = map(str, sys.stdin.readline().split())
        tree[node] = Node(item=node, left=left, right=right)

    pre_order(tree['A'])
    print()
    in_order(tree['A'])
    print()
    post_order(tree['A'])