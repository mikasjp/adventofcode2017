input = [x for x in open('data.txt', 'r').read().split("\n")]

# Building a tree
tree = {}

for x in input:
    s = x.split(" -> ")
    name_weight = s[0].split(" ")
    name = name_weight[0]
    weight = int(name_weight[1][1:-1])
    if name not in tree:
        tree[name] = {"parent": "", "weight": 0, "childlist": []}
    tree[name]["weight"] = weight
    if s.__len__()>1:
        child = s[1].split(", ")
        for c in child:
            if c not in tree:
                tree[c] = {"parent": "", "weight": 0, "childlist": []}
            tree[c]["parent"] = name
            tree[name]["childlist"].append(c)

def CalcTreeWeight(node):
    w = tree[node]["weight"]
    for child in  tree[node]["childlist"]:
        w += CalcTreeWeight(child)
    return w

# First part

root = ""

for key,value in tree.items():
    if value["parent"]=="":
        root = key
        print("First part: " + root)
        break

# Second part

unbalanced = ""

def FindUnbalancedNode(node):
    global unbalanced

    ChildWeights = [CalcTreeWeight(x) for x in tree[node]["childlist"]]

    if ChildWeights.__len__()>0:
        occurrences = [ChildWeights.count(x) for x in ChildWeights]
        if min(occurrences)!=max(occurrences):
            unbalanced = tree[node]["childlist"][occurrences.index(min(occurrences))]
            FindUnbalancedNode(unbalanced)

FindUnbalancedNode(root)

tmp = list(map(CalcTreeWeight, tree[tree[unbalanced]["parent"]]["childlist"]))

corrected = tree[unbalanced]["weight"] - (max(tmp) - min(tmp))

print("Second part: " + str(corrected))
