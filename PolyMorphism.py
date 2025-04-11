#Polymorphism- having many forms
class vehicle:
    def start(self):
        print("Vehicle starting")
class car:
    def start(self):
        print("car starting")
class bike:
    def start(self):
        print("bike starting")
def begins(v):
    v.start()
begins(car())
begins(bike())
    
    
