class gratfather:
    def behavior(self):
        name_gf="x"
        value=100
        print("i have one grant child")
class father(gratfather):
    def a(self):
        name_fa="abc"
        print("iam abc")
class mother:
    def b(self):
        name_mom="susu"
        value=10
        son=2
        print("i have long hair")
class son(father,mother):
    def c(self):
        print("iam one sun")
class son2(father,mother):
    def d(self):
        print("iam second son")
class daughter(father,mother):
    def e(self):
        print("iam daughter")
class grandchild(son2):
    def gs(self):
        print("iam grand chile")
obj=grandchild()
obj.a()
obj.behavior()
