# Python-design-Patterns

### What are Design Patterns
* Design patterns are created by Christopher Alexander and are well known solutions to recurring problems that occur in software engineering.
* These are a description or template for how to solve a problem that can be used in many different situations.
* These solutions are widely accepted by software development community.
* We should use thes design patterns so that we don't reinvent the wheel when there's already exists a perfect solutions for the problems, thus time-saver.
* Design patterns allows us to reuse the design ideas.
* Design patterns helps us to lower the development cost, time and increases quality of the software.

***

### Characterstics of Design Patterns
* Design patterns are language neutral.
* Design patterns are dynamic because there always new ones coming up.
* Design patterns are intentionally incomplete by design to promote customization.

***

### Types of Design Patterns
There are 3 types of Design patterns
* Creational
* Structural
* Behavioral

#### Creational Patterns
* We use creational design patterns to build objects systematically.
* The main benefit of creational patterns is their flexibility.
* For example differnt types of objects from the same class can be created at runtime using creational patterns.
* In creational pattern, Polymorphism is often in use.

#### Structural Patterns
* We use structural patterns to eastablish relation between software components in particular settings.
* The goal is to satisfy functional and nonfunctional requirements.
* Functional requirements refer to what the software does.
* NonFunctional requiremnets refer to how well it does its job (like how fast or slow).
* Structual patterns take advantage of inheritance.

#### Behavioral Patterns
* It refers to how you make your objects interact with each other.
* The focus here is to defining protocols between these objects when working together to achieve a common goal.
* Beahavorial patterns mostly use methods and their signatures.

***

### Understanding OOPs
* Design patterns involve use of oops.
* An object represents entity in both problem and solution domain. 
* In a sotfware environment, a component usually represents a entity interacting with the software.
* For example lets consider conference registration problem.
	Here a participant is a entity in problem domain.
	And Registration form is a entity in solution domain.
* Classes are templates to create objects to avoid recreating them from scratch.
* Classes define objects in terms of attributes and behaviors.
* Attributes represents properties of an entity. It captures the current state of the entity.
* Methods represents the behavior of the entity.

***

### Design Pattern context
A pattern context consist of the following
* Participants : It refers to classes involved to form a design pattern. Each class play a different role to accomplish the goal of the design pattern.
* Quality Attribute : It refer to nonfunctional requirements such as - usability, modifiability, reliability, performance and more.
* Forces : It refers to various factors or trade-offs.
* Consequences : It can be worst performance.
A descision maker should consider a design pattern after thoroughly considering its consequences.

***

### Design Pattern Language
A design pattern is kind of a new language which consists of
* Name : pattern names should be meaningful & memorable.
* Context : It provides a scenario in which a pattern can be used.
* Problem : It describes the design challenge the pattern is trying to address.
* Solution : It specifies a pattern itself in terms of structures and behaviors.
* Related patterns : These list other patterns used together with the current pattern.