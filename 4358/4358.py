from sys import stdin

"https://www.acmicpc.net/problem/4358 생태학 <Silver I>"

tree_list = stdin.read().split("\n")
tree_total = 0
tree_selectivity = {}
for name in tree_list:
    if name == "":
        continue
    tree_total += 1
    selectivity = tree_selectivity.get(name)
    if selectivity == None:
        selectivity = 0

    tree_selectivity[name] = selectivity + 1

for name in sorted(tree_selectivity.keys()):
    print(f"{name} {tree_selectivity[name]/tree_total * 100:.4f}")

