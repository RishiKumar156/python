def countLeaves(root):
    # Code here
    cnt = []
    def traverse(root):
        if not root.left and not root.right:
            cnt.append(1)
        if root.left:
            traverse(root.left)
        if root.right:
            traverse(root.right)
    traverse(root)
    return sum(cnt)