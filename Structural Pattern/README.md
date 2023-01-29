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

***

### Adapter
The Adapter pattern converts interface of a class to another the client is expecting.
* The problem here is that interfaces are incomaptible between the client and the server.
* The scenario here is that we have two methods speak_korean() for korean and speak_english() for english. The client expects to iuse a single method speak() for both.
* The solution is to use the Adapter pattern which translates between the two methods for the client.

Adapter Example : [adapter.py](https://github.com/pyGuru123/Python-design-Patterns/blob/main/Structural%20Pattern/adapter.py)

***

### Composite
A composite design pattern maintains a tree data structure.
* The problem here is to build a recursive tree data structure so that an element of the tree can have subelements
* Here the scenerio is creating menu and submenu items, which can have further submenu items.
* The solution consists of 3 major elements\
	Component : An abstract class\
	Child : A concrete class inherits from the component\
	Composite : A concrete class which also inherits from component. The composite class maintains child objects by ading and removing them to a tree data structure.

Composite Example : [composite.py](https://github.com/pyGuru123/Python-design-Patterns/blob/main/Structural%20Pattern/composite.py)

***

### Bridge
Bridge patten helps untangle a complicated class hierarchy
* The problem here is that there are two unrelated, parallel abstractions. One is implementation specific and other is implementation independent.
* The scenario involves implementation-independent circle abstraction and implementation-dependent circle abstraction. The second abstraction involves how to draw a circle, while the first one involves defining the properties of the circle and scaling it.
* The solution tries to seperate the abstraction into two different class hierarchies.

Bridge Example : [bridge.py](https://github.com/pyGuru123/Python-design-Patterns/blob/main/Structural%20Pattern/bridge.py)