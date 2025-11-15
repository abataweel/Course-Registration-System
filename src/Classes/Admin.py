import bcrypt
import sqlite3
import random
import time
from User import BaseUser
class Admin(BaseUser):
    def __init__(self,fname,mname,lname,email,password,id=0000000):
        super().__init__(fname,mname,lname,id,email,password,role="Admin")
        
        
    def addNewCourse(self,regSystem,course):
        pass
    def updateExistingCourse(self,regSystem,courseCode,updates):
        pass
    def deleteCourse(self,regSystem,coursecode):
        pass
    def loadBulkData(self,type,regSystem,file):
        pass
    def addUser(self,User):
        pass
    
        
        