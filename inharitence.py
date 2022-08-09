class person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
# p = person("muhammed","arshad")
# p.printname()
class child(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)

    def printini(self,ini):
        self.ini = ini
        print(self.ini)
c=child("arshad","muhammed")
c.printname()
c.printini("vadakkan")
