# class student:
#     def __init__(self):
#         print("this is a non parameterised constructor")
#     def show(self,name):
#         print("hello ",name)
# s=student()
# s.show("arshad")

class student:
    def __init__(self,name):
        print("this is a parametarized constructor")
        self.name=name
    def show(self):
        print("hello ",self.name)
s=student("arshad")
s.show()