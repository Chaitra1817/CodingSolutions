'''
690. Employee Importance
Solved
Medium
Topics
Companies

You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees employees where:

    employees[i].id is the ID of the ith employee.
    employees[i].importance is the importance value of the ith employee.
    employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.

Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.

 

Example 1:

Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11

'''

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, query_id):
        emap={e.id:e for e in employees}
        ans=0
        def dfs(eid):
            nonlocal ans
            employee=emap[eid]
            ans+=employee.importance
            for eid in employee.subordinates:
                dfs(eid)
            return ans
        
        return dfs(query_id)
