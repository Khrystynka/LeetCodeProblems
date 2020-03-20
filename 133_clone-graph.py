# Problem Title: Clone Graph
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        def dfs(node, visited={}):
            node_clone = Node(node.val, [])
            visited[node] = node_clone
            for neighbor in node.neighbors:
                if neighbor in visited:
                    node_clone.neighbors.append(visited[neighbor])
                else:
                    node_clone.neighbors.append(dfs(neighbor, visited))
            return node_clone
        return dfs(node)

