class animal():
    def sound(self):
        print ("Animal makes sound")
class dog(animal):
    def sound(self):
        print ("dog barks")
class bird(dog):
    def sound(self):
        print ("bird sings")
crow = bird()
crow.sound()