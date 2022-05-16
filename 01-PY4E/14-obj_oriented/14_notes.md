__Course:__ Python 4 Everybody
__Instructor:__ Charles Severance
__Source:__ n/a
__Student:__ surge55
__Book:__ Python for Everybody
__Author:__ Charles Severance


# Chapter 14 Notes
## Object-Oriented Programming

\

\

\

From Lecture

## Python Objects



**- Warning -**

- This lecture is about definitions and mechanics for objects
- This lecture is a lot more about "how it works" and less about "how you use it"
- You won't get the entire picture until this is all looked at in the context of a real problem
- So please suspend disbelief and learn technique for the next 50 or slides...





### Review of Programs

**Object Oriented**

- A program is made up of many cooperating objects
- Instead of being the "whole program" - each object is a little "island" within the program and cooperatively working with other objects
- A program is made up of one or more objects working together - objects make use of each other's capabilities



**Object**

- An object is a bit of self-contained Code and Data
- A key aspect of the object approach is to break the problem into smaller understandable parts (divide and conquer)
- Objects have boundaries that allow us to ignore un-needed detail
- We have been using objects all along: String Objects, Integer Objects, Dictionary Objects, List Objects...
- Objects hide details - they allow the "rest" of the program to ignore the detail about "us"



<u>**Definitions**</u>

**Class** = a template (Dog) - it is a cookie cutter template, not the object itself

​			Defines the abstract characteristic of a thing (object), including thing's characteristics (its attributes, fields or properties) and the thing's behaviors (the things it can do, or methods, operations or features). One might say that a class is a blueprint or factory that describes the nature of something. For example, the class DOG would consists of traits shared by all dogs, such as breed and fur color (characteristics), and the ability to bark and sit (behaviors).

**Method or Message** = a defined capability of a class (`bark()`) - a function that lives inside of a class

​			An object's abilities. In language, methods are verbs. Lassie, being a Dog, has the ability to bark. So `bark()` is one of Lassie's methods. She may have other methods as well for example `sit()` or `eat()` or `walk()` or `save_timmy()`. Within the program, using a method usually affects only one particular object; add Dogs can bark, but you need only one particular dog to do the barking.

**Field or attribute** = a bit of data in a class (length/weight of dog ) 

**Object or Instance** = A particular instance of a class - Lassie

​			One can have an instance of a class or particular object. The instance is the actual object created at runtime. In programmer jargon, the Lassie object is an instance of the DOG class. The set of values of the attributes of a particular object is called its **state**. The object consists of state and the behavior that's defined in the object's class.



### A Sample Class 

```python
class PartyAnimal:
    x = 0
    
    def party(self):
        self.x=self.x + 1
        print("So far", self.x)
an = PartyAnimal()

an.party()
an.party()
an.party()
```



**Playing with dir() and type()**

- The `dire()` command lists capabilities
- Ignore the ones with underscores - these are used by python itself
- The rest are real operations that the object can perform
- It is like `type()` - it tells us something "about" a variable



### Object Lifecycle

The act of creating and destroying objects.

- Objects are created, used and discarded
- We have special blocks of code (methods) that get called
  - At the moment of creation (constructor)
  - At the moment of destruction (destructor)
- Constructors are used a lot
- Destructors are seldom used



**Constructor**

- The primary purpose of the constructor is to set up some instance variables to have the proper initial values when the object is created

```python
class PartyAnimal:
    x = 0
    
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x=self.x + 1
        print("So far", self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal() # construct the object to 'an'

an.party()
an.party()
an = 42
print('an contains', an)
```

PRINTS:

**I am constructed**
**So far 1**
**So far 2**
**I am destructed 2**
**an contains 42**



The constructor and destructor are optional. The constructor is typically used to set up variables. The destructor is seldom used.



**Many Instances**

- We can create lots of objects - the class is the template for the object
- We can store each distinct object in its own variable
- We call this having multiple instances of the same class
- Each instance has its own copy of the instance variable



```python
class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
```

Constructors can have additional parameters. These can be used to setup instance variables for the particular instance variables for the particular instance of the class (i.e. for the particular object)



## Inheritance

- When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class. 
- Another form of store and reuse
- Write once - reuse many times
- The new class (child) has all the capabilities of the old class (parent) - and then some more
- Sometimes called Extending a class or sub-classing



"Subclasses" are more specialized versions of a class, which inherit attributes and behaviors from their parent classes, and can introduce their own.





\

\

\

From Textbook

\

\

\



## Managing Larger Programs



We started constructing programs with four basic programming patterns:

- Sequential code
- Conditional cod (if statements)
- Repetitive code (loops)
- Store and reuse (functions)
- Variables (int, string, float)
- Stata Structures (lists, tuples, dictionaries)



As programs get to be millions of lines long, it becomes increasingly important to write code that is easy to understand. If you are working on a million-line program, you can never keep the entire program in your mind at the same time. We need ways to break large programs into multiple smaller pieces so that we have less to look at when solving a problem, fix a bug, or add a new feature.

In a way, object oriented programming is a way to arrange your code so that you can zoom into 50 lines of code and understand it while ignoring the other 99,950 lines of code for the moment.



### Using Objects

```python
stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()

print(stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff,0))
```

The three lines above print out the same thing.

 You can look at the capabilities of an object by looking at the output of the `dir()` function.

```python
>>> stuff = list()
>>> dir(stuff)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```



### Starting with Programs

A program in its most basic for takes some input, does some processing, and produces some output.



### Subdividing Programs

One of the advantages of the object-oriented approach is that it can hide complexity.



### Our First Python Object

At a basic level, an object is simply code plus data structures that are smaller than a whole program. Defining a function allows us to store a bit of code and give it a name and then later invoke that code using the name of the function.

An object can contain a number of functions (which we call *methods*) as well as data that is used by those functions. We call data items that are part of the object *attributes*.

We use the *class* keyword to define the data and code that will make up each of the objects. The class keyword includes the name of the class and begins an indented block of code where we include the attributes (data) and methods (functions).

```python
class PartyAnimal:
    x = 0
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

an = PartyAnimal("Sally")
an.party()
an.party()
PartyAnimal.party(an)
```



The methods have special first parameter that we name by convention `self`.

Just as the def keyword does not cause function code to be executed, the class keyword does not create an object. Instead, the class keyword defines a template indicating what data and code will be contained in each object of type `PartyAnimal`.



### Classes as Types

All python variables have a type.



### Object Lifecycle

When the program finishes, all of the variables (and objects) are discarded. Usually, we don't think much about the creation and destruction of variables, but often as our objects become more complex, we need to take some action within the object to set things up as the object is constructed and possibly clean things up as the object is discarded.

If we want our object to be aware of these moments of construction and destruction, we add specially named methods to our object.

```python
class PartyAnimal:
    x = 0
    
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x=self.x + 1
        print("So far", self.x)

    def __del__(self):
        print('I am destructed', self.x)

```



### Multiple Instances

The real power in object-oriented programming happens when we construct multiple instances of our class.

When we construct multiple objects from our class, we might want to setup different initial values for each of the objects. We can pass data to the constructors to give each object a different initial value.

Each object has its own independent copies of data/attributes stored within the object.



### Inheritance

Another powerful features of object-oriented programming is the ability to create a new class by extending an existing class. When extending a class, we call the original class the parent class and the new class the child class. 

For this example, we move our `PartyAnimal` class to its own file. Then, we can "import" the class in a new file and extend it, as follows:

```python
from party import PartyAnimal

class CricketFan(PartyAnimal):
    point = 0
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
```

> OUTPUT
>
> Sally constructed
> Sally party count 1
> Jim constructed
> Jim party count 1
> Jim party count 2
> Jim points 6
> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'party', 'points', 'six', 'x']



