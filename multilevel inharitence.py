'''multilevel inharitence '''

# class animal:
#     def eat(self):
#         print("eating")
# class dog(animal):
#     def bark(self):
#         print("barking")
# class pappy(dog):
#     def weep(self):
#         print("weeping")
# d=pappy()
# d.eat()
# d.bark()
# d.weep()

'''python multiple inharitence'''

# class base1:
#     def name(self):
#         print("arshad")
# class base2:
#     def sname(self):
#         print("vadakkan")
# class multi(base1,base2):
#     def age(self):
#         print("22")
# a=multi()
# a.age()
# a.name()
# a.sname()


'''super class'''

# class vehicle:
#     def start(self):
#         print("starting engine")
#     def stop(self):
#         print("stop engine")
# class twowheeler(vehicle):
#     def say(self):
#         super().start()
#         print("i have two wheeler")
#         super().stop()
# pulsar=twowheeler()
# pulsar.say()
# pulsar.start()
# pulsar.stop()

'''polymorphism'''

# class english:
#     def greeting(self):
#         print("hello")
# class french:
#     def greeting(self):
#         print("bonjour")
# def intro(language):
#     language.greeting()
# e=english()
# f=french()
#
# intro(e)
# intro(f)