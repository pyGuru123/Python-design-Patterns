# Creational Pattern

* We use creational design patterns to build objects systematically.
* The main benefit of creational patterns is their flexibility.
* For example differnt types of objects from the same class can be created at runtime using creational patterns.
* In creational pattern, Polymorphism is often in use.

***

### Factory
Factory encapsulates object creation. It is an object specializing in creating other objects.
Factory solves the following problem
* When its uncertain what type of objects we are going to use at runtime.
* When the application needs to decide what classes to be used at runtime.

Example of factory : [Factory.py](https://github.com/pyGuru123/Python-design-Patterns/blob/main/Creational%20Pattern/factory.py)

***

### Abstract Factory
* Abstract factory builds on the factory pattern.
Abstract factory is useful when the user expects to receive a family of multiple related objects but doesn't have to know what fammily it is until runtime.
* A factory returns a single object whereas a abstract factory return two or multiple related objects, like dog and dog food in our example
* Abstract factory creates objects while concrete factories are often singletons.

Example of abstract factory : [abstractFactory.py](https://github.com/pyGuru123/Python-design-Patterns/blob/main/Creational%20Pattern/abstractFactory.py)