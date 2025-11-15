import random
import bcrypt
import sqlite3
import random
import time
class BaseUser():
    def __init__(self,fname:str,mname:str,lname:str,*id:int,email:str,password:str,role:str):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.email = email
        self.id = id
        self.role = role
        self._password = password
        
    # authentication methods
    def login(self,id:int,password:str):
        #validation
        #get hashed password from db and compare it with the hashed entered password
        self.id==id and self._password==password
    def set_password(self,newpassword:str):
        #validation later
         self._password = newpassword
         #save new pass to db
    def getFullName(self):
        return f"{self.fname} {self.mname} {self.lname}"
    def getID(self):
        return self.id
    def getRole(self):
        return self.role
    