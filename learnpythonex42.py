## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self,name):
        self.name = name

    def run(self):
        print("output is -:",self.name)

# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # self.name has-a name
        self.name = name
# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # self.name has-a name
        self.name = name

# person is-a object
class Person(object):

    def __init__(self, name):
        # self.name has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

 # Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee is-a name
        super(Employee, self).__init__(name)
        # self.salary has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

rover.run()

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet (called satan)
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

print(frank.__dict__)
# frank has-a pet (called rover)
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()