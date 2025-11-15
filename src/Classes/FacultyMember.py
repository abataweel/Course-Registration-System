import bcrypt
import sqlite3
import random
import time
from User import BaseUser
class FacultyMember(BaseUser):
    validDepartments = ["Computer","Communications","Power","Biomedical"]
    def __init__(self,fname,mname,lname,id,email,password,department:str,courseTaught:list=[]):
        super().__init__(fname,mname,lname,id,email,password,role="Faculty")
        self._department = self.validateDepartment(department)
        self._courseTaught = courseTaught
    def validateDepartment(self,department):
        if department not in self.validDepartments:
            raise ValueError("Invalid department")
        return department
    def getDepartment(self):
        return self._department
    def getCourseTaught(self):
        return self._courseTaught
    def assignCourse(self,course):
        pass