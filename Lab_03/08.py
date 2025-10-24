import sys

input = sys.stdin.readline

nodes = int(input())

def solve(inorder, post):
    if len(inorder) == 0:
        return []

    root = post[-1]
    idx = inorder.index(root)
    lst_inorder = inorder[:idx]
    lst_postorder = post[:idx]
    lst = solve(lst_inorder, lst_postorder)
    rst_inorder = inorder[idx+1:]
    rst_postorder = post[idx: len(post)-1]
    rst = solve(rst_inorder, rst_postorder)
    
    return [root] + lst + rst
    

inorder = list(map(int, input().split()))
post = list(map(int, input().split()))
    
print(*solve(inorder, post))