class person():
    def __init__(self,name,age):

        self.name =name
        self.age =age
    def add(self):
        print("hello my name "+ self .name)
p= person("arshad",22)
p.add()
print(p.name)
print(p.age)
#update value
p.age=21
print(p.age)
#delete value
del p.age
print(p.age)
