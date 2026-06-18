import matplotlib.pyplot as plt
import time


def get_positions(root):
    pos = {}
    x = [0]

    def dfs(node, depth):
        if not node:
            return

        dfs(node.left, depth + 1)
        pos[node] = (x[0], -depth)
        x[0] += 1
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return pos


def animate_tree(root):
    pos = get_positions(root)

    fig, ax = plt.subplots()

    nodes_drawn = set()

    def draw_step(node):
        if not node:
            return

        x, y = pos[node]

        # 画当前节点
        ax.scatter(x, y, s=800)
        ax.text(x, y, str(node.val),
                ha='center', va='center',
                color='white')

        nodes_drawn.add(node)

        # 延迟制造动画效果
        plt.pause(0.6)

        # 画边
        if node.left:
            x1, y1 = pos[node.left]
            ax.plot([x, x1], [y, y1])

        if node.right:
            x1, y1 = pos[node.right]
            ax.plot([x, x1], [y, y1])

        draw_step(node.left)
        draw_step(node.right)

    ax.axis('off')
    draw_step(root)

    plt.show()