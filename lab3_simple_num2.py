class Student:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group

    def show_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Группа:", self.group)


student1 = Student("Анастасия", 19, "221141")
student1.show_info()