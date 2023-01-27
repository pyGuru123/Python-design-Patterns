# Structural Patterns

* We use structural patterns to eastablish relation between software components in particular settings.
* The goal is to satisfy functional and nonfunctional requirements.
* Functional requirements refer to what the software does.
* NonFunctional requiremnets refer to how well it does its job (like how fast or slow).
* Structual patterns take advantage of inheritance.

***

### Decorator
Decorator pattern allows adding new features to an object without changing their structures.
* Here the problem is to add new features to the object without subclassing.
* In python we can additional features to a function using the inbuilt decorator

Decorator Example : [decorator.py](https://github.com/pyGuru123/Python-design-Patterns/blob/main/Structural%20Pattern/decorator.py)

***

### Proxy
Proxy is helpful when creating a very highly resource intensive object.
* The problem here is postponing object creation unless absolutely necessary due to high resource consumption
* Here we find a placeholder which creates the object when absoluetly necessary.
* The scenerio is that we create an instance of the producer class (resource intensive ) only when its available because only a fix number of producers can exist at the given time.
* Our proxy is the artist checking to see if producer becomes available.
* The proxy object is responsible for creating the resource intensive object.

Proxy Example : [proxy.py](https://github.com/pyGuru123/Python-design-Patterns/blob/main/Structural%20Pattern/proxy.py)