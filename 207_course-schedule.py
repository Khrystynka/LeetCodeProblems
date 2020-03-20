# Problem Title: Course Schedule
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prereq = {x: [] for x in range(numCourses)}
        for x in prerequisites:
            prereq[x[1]].append(x[0])
        exploring_now = set()
        explored = set()

        def dfs(node):
            if node in explored:
                return True
            if node in exploring_now:
                return False
            exploring_now.add(node)
            for neighbor in prereq[node]:
                if dfs(neighbor) == False:
                    return False
            explored.add(node)
            exploring_now.remove(node)
            return True
        for i in range(numCourses):
            if i not in explored:
                if dfs(i) == False:
                    return False
        return True

