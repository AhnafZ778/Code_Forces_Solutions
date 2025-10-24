import sys

input = sys.stdin.readline

def solve(inorder, preorder):
    if len(inorder) == 0:
        return []
    root = preorder[0]
    idx = inorder.index(root)
    lst_inorder = inorder[:idx]
    rst_inorder = inorder[idx+1:]
    lst_preorder = preorder[1: idx + 1]
    rst_preorder = preorder[idx+1:]
    
    left = solve(lst_inorder, lst_preorder)
    right = solve(rst_inorder, rst_preorder)
    
    return left + right + [root]


nodes = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

print(*solve(inorder, preorder))