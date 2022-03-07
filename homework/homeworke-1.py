class Dog:
    def __init__(self, name, breed, size, voice):
        self.name = name
        self.breed = breed
        self.size = size
        self.voice = voice

    def golos(self):
        print(f'{self.voice}')

class Cat:
    def __init__(self, name, breed, size, voice):
        self.name = name
        self.breed = breed
        self.size = size
        self.voice=voice

    def golos(self):
        print(f'voice:{self.voice}')

class Cow:
    def __init__(self, name, breed, size, voice):
        self.name = name
        self.breed = breed
        self.size = size
        self.voice = voice
    def golos(self):
        print(f'{self.voice}')

class Bear:
    def __init__(self, name, breed, size, voice):
        self.name = name
        self.breed = breed
        self.size = size
        self.voice = voice
    def golos(self):
        print(f'voice:{self.voice}')

dog = Dog('Chika', 'human', 170, 'kto chto bral?')
dog.golos()

cat = Cat('Adahan', 'human', 30, 'miyyy')
cat.golos()

cow = Cow('Maruf', 'human', 170, 'windows')
cow.golos()

bear = Bear('Beka', 'human', 177, 'dalete')
bear.golos()