class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = collections.defaultdict(set)
        pres = collections.defaultdict(set)
        res = []
        for course, pre in prerequisites:
            courses[course].add(pre)
            pres[pre].add(course)
        stack=[n for n in range(numCourses) if not courses[n]]
        count = 0
        while stack:
            no_pre = stack.pop()
            res.append(no_pre)
            count+=1
            for course in pres[no_pre]:
                courses[course].remove(no_pre)
                if not courses[course]:
                    stack.append(course)
        return res if count==numCourses else []
        
        