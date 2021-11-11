# count leaves in subtree
def DFS(node, tree, diverges):
    for next in tree[node]:
        diverges[node] += DFS(next-1, tree, diverges)
    if diverges[node] == 0:
        diverges[node] = 1
    return diverges[node]


def findRoot(numNodes, tree):
    parents = []
    for i in range(numNodes):
        parents.append(0)
    for i in range(numNodes):
        for j in tree[i]:
            parents[j-1] += 1
    for i in range(numNodes):
        if parents[i] == 0:
            return i
    return numNodes  # NA


numNodes = int(input())
tree = [[]]
tree.clear()
for i in range(numNodes):
    tree.append(list(map(int, input().strip().split())))
root = findRoot(numNodes, tree)
diverges = []
for i in range(numNodes):
    diverges.append(0)
DFS(root, tree, diverges)
for i in range(numNodes):
    print(diverges[i])
