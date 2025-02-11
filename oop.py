class animal:
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        print('My name is ' + self.name)


class bird(animal):
    def __init__(self,name):
        super().__init__(name)
    
    def fly(self):
        self.introduce()
        print('Flying')


unicorn = animal('Purple')
unicorn.introduce()

theCrow = bird('Fast Crow')
theCrow.fly()