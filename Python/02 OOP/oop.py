# # import os
# # os.system('cls' if os.name == 'nt' else 'clear')

# print("-"*30)


# def print_types(data):
#     for i in data:
#         print(i, type(i))


# test = [122, "victor", [1, 2, 3], (1, 2, 3), {1, 2, 3}, True, lambda x: x]

# print_types(test)


# print("-"*30)


# class Person:
#     name = "Victor"
#     age = 32


# # ? Person class'ından obje (instance) üretiyoruz 👇
# person1 = Person()
# person2 = Person()

# # print(person1.name)  # Victor

# # ? Class'ımıza yeni bir attribute ekledik. Bu class'tan üretilmiş instance'larda bu özellik geçerli oluyor.
# Person.job = "Developer"

# # print(person2.job)

# person1.location = "Turkey"
# #! Instance'larda yaptığımız değişiklikler diğer instance'ları etkilemez 👇
# # print(person2.location)  # * 'Person' object has no attribute 'location'

# person2.age = 25
# # print(person1.age)  # 32
# # print(person2.age)  # 25

# # ? İlk önce instance'a bakıyor. Orada yoksa class'a gidip bakıyor 👆

# #! class attributes and instance attributes

# # person1.location="Turkey" diğerlerini etkilemez


# # class Person:
# #     company: "Clarusway"

# #     def test(self):
# #         print("test")

# #     def set_details(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def get_details(self):
# #         print(self.name, self.age)


# # person1 = Person()

# # person1.test()
# # Person.test(person1)  python arkada bu şekle dönüştürüyor ve o yüzden üstteki çalışmıyor.(arguman gönderdin diyor) def tanımlamasına self ekleyerek sorunu çözebiliriz.

# # person1.set_details("Ahmet", 32)
# # person1.get_details()

# # ? static methods
# #! instance göre değişmeten self olmazlar


# @staticmethod
# def salute():
#     print("Static method")


# ? special methods (__init__,str)//Dunger-Magic methods

#! ============İNİT===========================
# class Person:
#     company: "Clarusway"

#     def __init__(self, name, age=34, gender="Male"):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def get_details(self):
#         print(self.name, self.age, self.gender)


# person1 = Person("Henry", 18)
# # person1.get_details()
# print(person1)  # <__main__.Person object at 0x7f8f113a6040>


#! ============STR===========================
# class Person:
#     company: "Clarusway"

#     def __init__(self, name, age=34, gender="Male"):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def get_details(self):
#         print(self.name, self.age, self.gender)

#     def __str__(self):
#         return f"{self.name} - {self.age}"


# person1 = Person("Henry", 18)
# #print(person1.__str__()) #👇
# print(person1)  # Henry - 18


# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self._id = 5000
#         self.__id = 123

#     def __str__(self):
#         return f"{self.name} - {self.age}"

#     def get_details(self):
#         print(self.name, self.age, self.gender)


# person1 = Person("Henry", 15, "Male")
# print(person1._id)
# # print(person1.__id) AttributeError: 'Person' object has no attribute '__id'
# print(person1._Person__id)


# liste = [2, 4, 5, 3, 1]

# liste.sort()

# ? İNHERİTANCE AND POLYMORPHİSM


class Person:
    company = "Clarusway"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name} - {self.age}"

    def get_details(self):
        return self.name, self.age, self.gender, self.path


class Employee(Person):
    def __init__(self, name, age, gender, path):
        super().__init__(name, age, gender)
        self.path = path


emp1 = Employee("vixctor", 23, "Male", "Developer")

print(emp1.get_details())


# * polymorhism   => parent'tan gelen yapı ihtiyacımızı tam karşılamıyorsa update edebilmemiz.
