# Problem Title: Employee Importance
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        for employee in employees:
            d[employee.id] = (employee.importance, employee.subordinates)

        res = d[id][0]
        subord = [d[id][1]]
        while subord:
            persons = subord.pop()
            for person in persons:
                res += d[person][0]
                subord.append(d[person][1])
        return res

