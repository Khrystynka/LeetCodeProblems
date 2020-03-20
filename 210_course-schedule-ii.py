# Problem Title: Course Schedule II
from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        '''indegree=defaultdict(lambda: 0)
        edges=defaultdict(lambda:[])
        for pair in prerequisites:
            #print edges[pair[1]],pair[0]
            edges[pair[1]].append(pair[0])
            indegree[pair[0]]+=1
        without_in_edges=[]
        for i in range(numCourses):
            if indegree[i]==0:
                without_in_edges.append(i)
        res=[]
        while without_in_edges:
            node=without_in_edges.pop()
            res.append(node)
            for dependent in edges[node]:
                indegree[dependent]-=1
                if indegree[dependent]==0:
                    without_in_edges.append(dependent)
        return res if len(res)==numCourses else[]   '''
        processing = set()
        processed = set()
        res = []
        edges = defaultdict(lambda: [])
        for pair in prerequisites:
            edges[pair[1]].append(pair[0])

        def dfs(node):
            if node in processing:
                return False
            if node in processed:
                return True
            processing.add(node)
            for neighbor in edges[node]:
                if dfs(neighbor) == False:
                    return False
            processing.remove(node)
            processed.add(node)
            res.append(node)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res[::-1]

