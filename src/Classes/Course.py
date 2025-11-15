class Course():
    def __init__(self,code,name,credits,lectureHours,*grade,labHours=None,prerequisites=[],capacity=0,lecturer="",program="",schedule=[]):
        self.courseCode = code
        self.name = name
        self.labHours = labHours
        self.credits = credits
        self.grade = grade
        self.lectureHours = lectureHours
        self.prerequisites = prerequisites
        self.capacity = capacity
        self.lecturer = lecturer
        self.program = program
        self.schedule = schedule
    def checkPrerequisites(self,trnascript):
        pass
    def isFull(self,currentSemester):
        pass
    def isConflict(self,course):
        pass
    def checkDuplicatedCode(self):
        pass
    
    