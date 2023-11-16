'''

1136. Parallel Courses
Solved
Medium
Topics
Companies
Hint

You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.

Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.

'''

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        in_degree = [0] * (n+1)

        for i, j in relations:
            adj_list[i].append(j)
            in_degree[j] += 1

        stack = deque([i for i in range(1, n+1) if in_degree[i] == 0])
        semester = 0
        total_courses = 0

        while stack:
            size = len(stack)
            for _ in range(size):
                current = stack.popleft()
                total_courses += 1

                for neighbor in adj_list[current]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        stack.append(neighbor)

            semester += 1
            print("sem",semester)
            print("stack",stack)

        return semester if total_courses == n else -1
