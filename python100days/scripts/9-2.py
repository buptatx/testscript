#! -*- coding:utf-8 -*-

class Person():
    def __init__(self, name, age):
         self._name = name
         self._age = age

    @property
    def name(self):
         return self._name

    @property
    def age(self):
         return self._age

    @age.setter
    def age(self, age):
        if age > 0 and age < 200:
            self._age = age
        else:
            print("invalid age")

    def play(self):
        if self._age <= 16:
            print("%s play balabala" % self._name)
        else:
            print("%s play lol" % self._name)

    def watch_tv(self):
        if self._age > 18:
            print("%s watch Tokyo hot" % self._name)
        else:
            print("%s watch balabala" % self._name)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade >= 0 and grade <=100:
            self._grade = grade
        else:
            print("invalid grade")

    def study(self, course):
        print("%s in %s is studying %s" % (self._name, course, self._grade))


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s is teaching %s" % (self._name, course))


if __name__ == "__main__":
    stu = Student('Dachui Wang', 15, 'third grade')
    stu.study('english')
    stu.watch_tv()
    stu.play()
    t = Teacher('Hao Luo', 38 , "Doctor")
    t.teach('Programming in Python')
    t.watch_tv()
    t.play()