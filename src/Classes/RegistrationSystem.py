import bcrypt
import sqlite3
import random
import time
from Student import Student
from Course import Course 
from User import BaseUser

class RegistrationSystem():
    def __init__(self,dbFile):
        self.dbFile = dbFile
        self.conn = sqlite3.connect(self.dbFile)
        
    def addStudent(self,student):
        pass
    def getStudent(self,id):
        pass
    def addCourse(self,course):
        pass
    def getCourse(self,code):
        pass
    def registerStudentInCourse(self,stuID,courseCode):
        pass
        
        
        