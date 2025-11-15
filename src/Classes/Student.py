import bcrypt
import sqlite3
import random
import time
from User import BaseUser
from Transcript import TranscriptEntry
class Student(BaseUser):
    def __init__(self,fname,mname,lname,id,email,password,program:str,transcript:list[TranscriptEntry],currentLevel:int=None,gpa:float=None,completedCourses:list=[],currentRegisteredCourses:list=[]):
        super().__init__(fname,mname,lname,id,email,password,role="Student")
        self.program = program
        self.level = currentLevel
        self.transcript = transcript
        self.gpa = gpa
        self.regCourses = currentRegisteredCourses
        self.completedCourses = completedCourses
      
    def addCompletedCourse(self,course):
        pass  
    def getCompletedCredits(self):
        pass
    def addToTranscript(self,course):
        pass
    def getTranscript(self):
        pass
    def registerCourse(self,courseCode):
        pass