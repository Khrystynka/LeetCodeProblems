# Problem Title: Graph Valid Tree
from collections import defaultdict


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if edges == []:
            return n < 2
        d = defaultdict(lambda: [])
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        visited = set()
        node = edges[0][0]
        exploring = [node]

        while len(exploring) > 0:
            node = exploring.pop()
            if node in visited:
                return False
            for neighbor in d[node]:
                if neighbor in exploring or neighbor == node:
                    return False
                d[neighbor].remove(node)
                exploring.append(neighbor)
            visited.add(node)
        return len(visited) == n

