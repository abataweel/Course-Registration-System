import random
class BaseUser():
    def __init__(self,fname,mname,lname,*id,email,password,role):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.email = email
        self.role = role
        self.password = password
        if not id:
            self.id = "24"+random.randint(5)
    # authentication methods
    def login(self,id,password):
        pass
    def set_password(self,newpassword):
        pass
    def getFullName(self):
        return str(self.fname+self.mname+self.lname)
    def getID(self):
        return self.id
    def getRole(self):
        return self.role
    