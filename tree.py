class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(level_order):
    if not level_order:
        return None

    nodes = [None if x is None else TreeNode(x) for x in level_order]

    j = 1
    for i in range(len(nodes)):
        if nodes[i]:
            if j < len(nodes):
                nodes[i].left = nodes[j]
                j += 1
            if j < len(nodes):
                nodes[i].right = nodes[j]
                j += 1

    return nodes[0]
