import tkinter as tk
from tree import build_tree
from animator import animate_tree


def parse_input(text):
    arr = text.split(',')
    res = []
    for x in arr:
        x = x.strip()
        if x.lower() == "null":
            res.append(None)
        else:
            res.append(int(x))
    return res


def run_app():
    root = tk.Tk()
    root.title("二叉树可视化系统")

    label = tk.Label(root, text="请输入层序序列（例如：1,2,3,4,5,null,7）")
    label.pack()

    entry = tk.Entry(root, width=40)
    entry.pack()

    def submit():
        data = parse_input(entry.get())
        tree = build_tree(data)
        animate_tree(tree)

    btn = tk.Button(root, text="生成二叉树动画", command=submit)
    btn.pack()

    root.mainloop()
