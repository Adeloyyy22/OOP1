from pydoc import Doc


class Builder:
    def can_build(self):
        print('i can build')


class Doctor:

    def can_help(self):
        print('i can help!')

class Programmer:

    def can_write_code(self):
        print('i can write code on Python !')

    def can_build(self):
        print('I am a programmer but i can build')

class Person( Programmer,Builder,Doctor ):
    pass

class Kairat(Person):
    pass

class Amir(Kairat):
    pass

jack = Person()
jack.can_build()
jack.can_build()