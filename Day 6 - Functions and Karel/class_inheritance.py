class Animal:
    def __init__(self):
        self.number_eyes = 2

    def breathe(self):
        print("Inhale... Exhale...")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater")

    def swim(self):
        print("One stroke... two strokes...")


nemo = Fish()
rodger = Animal()

rodger.breathe()
nemo.breathe()
nemo.swim()
