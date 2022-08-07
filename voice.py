class Dog:

    def __init__(self, name):
        self.name = name

    def voice(self):
        print(f"{self.name}: gaw gaw gaw")


dog = Dog('bobik')
dog.voice()


class Cow:
    def __init__(self, name):
        self.name = name

    def voice(self):
        print(f"{self.name}: mu mu mu")


cow = Cow('korova')
cow.voice()


class Bear:

    def __init__(self, name):
        self.name = name

    def voice(self):
        print(f"{self.name}: Roooooaaaaaaarrrrrr!")


bear = Bear("tolya")
bear.voice()


class Cat:

    def __init__(self, name):
        self.name = name

    def voice(self):
        print(f"{self.name}: myau myau myau")


cat = Cat('snezhok')
cat.voice()
