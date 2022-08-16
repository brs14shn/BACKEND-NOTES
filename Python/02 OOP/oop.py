# import os
# os.system('cls' if os.name == 'nt' else 'clear')

print("-"*30)


def print_types(data):
    for i in data:
        print(i, type(i))


test = [122, "victor", [1, 2, 3], (1, 2, 3), {1, 2, 3}, True, lambda x: x]

print_types(test)


print("-"*30)


class Person:
    name = "Victor"
    age = 32


# ? Person class'ından obje (instance) üretiyoruz 👇
person1 = Person()
person2 = Person()

# print(person1.name)  # Victor

# ? Class'ımıza yeni bir attribute ekledik. Bu class'tan üretilmiş instance'larda bu özellik geçerli oluyor.
Person.job = "Developer"

# print(person2.job)

person1.location = "Turkey"
#! Instance'larda yaptığımız değişiklikler diğer instance'ları etkilemez 👇
# print(person2.location)  # * 'Person' object has no attribute 'location'

person2.age = 25
# print(person1.age)  # 32
# print(person2.age)  # 25

# ? İlk önce instance'a bakıyor. Orada yoksa class'a gidip bakıyor 👆

#! class attributes and instance attributes

# person1.location="Turkey" diğerlerini etkilemez


class Person:
    company: "Clarusway"

    def test(self):
        print("test")


person1 = Person()

person1.test()
# Person.test(person1)  python arkada bu şekle dönüştürüyor ve o yüzden üstteki çalışmıyor.(arguman gönderdin diyor) def tanımlamasına self ekleyerek sorunu çözebiliriz.
