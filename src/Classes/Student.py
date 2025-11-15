from User import BaseUser
class Student(BaseUser):
    def __init__(self,fname,mname,lname,id,email,password,program,role="student",transcript=None,currentLevel=1,gpa=0.0,semesters=None,completedCourses=[]):
        super().__init__(fname,mname,lname,id,email,password,role)
        self.program = program
        self.level = currentLevel
        self.transcript = transcript
        self.gpa = gpa
        self.semester = semesters
        self.completedCourses = completedCourses
        
    def getCompletedCredits(self):
        pass
    def addToTranscript(self,course):
        pass
    def getTranscript(self):
        pass
    
        