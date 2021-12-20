from anytree import Node, RenderTree
from anytree import AnyNode, RenderTree
import copy

moznosti = [1, 2]


root = AnyNode(id="root")

moz = copy.copy(moznosti)

for m in moznosti:
    AnyNode(parent=root)

print(RenderTree(root))
