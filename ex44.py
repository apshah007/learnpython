#class Parent(object):

#        def implicit(self):
#            print("PARENT implicit()")

#class Child(Parent):
#        pass

#dad = Parent()
#son = Child()
#dad.implicit()
#son.implicit()

#class Parent(object):


#class Child(Parent):

#    def override(self):
#        print("CHILD override()")

#son = Child()

#dad.override()
#son.override()

#class Parent(object):

#    def altered(self):
#        print("PARENT altered()")

#class Child(Parent):

#    def altered(self):
#        print("CHILD, BEFORE PARENT altered()")
#        super(Child, self).altered()
#        print("CHILD, AFTER PARENT altered()")

#dad = Parent()
#son = Child()

#dad.altered()
#son.altered()
#
#

# most of the uses of inheritance can be simplified or replaced with composition
# and multiple inheritance should be avoided at all costs
#
#inheritance is used to indicate that one class will get most or all of its
#features from a parent class
#that happens implicitly whenever you write class Foo(Bar) which says
#make a class Foo that inherits from Bar
#When you do this, the language makes any action that you do on instances of
#Foo also work as if they were done to an instance of Bar.  Doing this lets
# you put common functionality in the Bar class, then specialize that functionality
# in the Foo class as needed

#when you are doing this kind of specialization there are 3 ways that the parent
#and child classes can interact
#1. actions on the child imply an action on the parent
#2. actions on the child override the action on the parent
#3. actions on the child alter the action on the parent

# first demonstrate implicit actions that happen when you define a function
# in the parent but not in the child

# the use of pass under the class Child: is how you tell python that you want
# empty block.  This creates a class named Child but says that there is nothing
# new to define it.  instead it will inherit all of its behavior from Parent
# this shows you that if you put functions in a base class (ie Parent), then
# all subclasses (ie Child) will automatically get those features

#override explicitly
# the problem with having functions called implicitly is sometimes you want the
# child to behave differently.  In this case you want to override the function
# in the child, effectively replacing the functionality,  to do this
# just define a function with the same name in Child

# as you an see, when the line runs it runs Parent.override function because
# variable is a parent.  when the next line runs it prints out child.override
# messages because son is an instance of Child and Child overrides that function
# by defining its own version

# the 3rd way to use inheritance is a special case of overriding where you
# want to alter the behavior before or after the Parent class's version runs
# you first override the function just like in the last example, but then you
# use a python built in function named super to get the parent

# multiple inheritance is when you define a class that inherits from one or
# classes, like this
# class SuperFun(Child, Badstuff):
#   pass
# means make a class named SuperFun that inherits from the classes Child and Badstuff
# at the same time
# whenever you have implicit actions on any SuperFun instance python has to look
# up the possible function in the class hierarchy for both Child and Badstuff
# but it needs to do this in a consistent order
# to do this python uses "method resolution order"  MRO  and an algorithm called
# C3 to get it straight
# because the MRO is complex and a well defined algorithm is used.  python cant
# leave it to you to get the MRO right.  instead python give you the super() function
# which handles all of this for you in the places tha you need the altering
# type of actions
# with super() you dont have to worry about getting this right and python will
# find the right function for youself.
# using super() with __init__

# the most common use of super() is actually in __init__ functions in base
# classes.  this is usually the only place where you need to do some things
# in a child.  then complete the initialization in the parent

# class Child(Parent):

#   def__init__(self, stuff):
#       self.stuff = stuff
#       super(Child, self).__init__()

# composition
# inheritance is useful, but another way to do the exact same thing is to just
# use other classes and modules rather than rely on implicit inheritance
# if you look at the 3 ways to exploit inheritance, 2 of the 3 involve writing
# new code to replace or alter functionality.  this can be replaced by just
# calling functions in a module



#class Parent(object):

#    def override(self):

#        print("PARENT override()")


#    def implicit(self):
#        print("PARENT implicit()")

#    def altered(self):
#        print("PARENT altered()")
#
#class Child(Parent):

#    def override(self):
#        print("CHILD override()")

#    def altered(self):
#        print("CHILD, BEFORE PARENT altered()")
#        super(Child, self).altered()
#        print("CHILD, AFTER PARENT altered()")

#dad = Parent()
#son = Child()

#dad.implicit()
#son.implicit()

#dad.override()
#son.override()

#dad.altered()
#son.altered()


# composition

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def altered(self):
        print("CHILD, BEFORE OTHER, altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

# in this code I am not using the name Parent since there is not a parent child
# relationship   it is not a is - a relationship

# this is a has-a relationship where Child has-a Other that it uses to get
# its work done.

# when to use inheritance or composition
# the question of inheritance versus composition comes down to an attempt
# to solve the problem of reusable code
# you dont want to have duplicated code all over your software since thats not
# clean and efficient
# inheritance solves this problem by creating a mechanism for you to have
# implied features in base classes
# composition solves this by giving you modules and the capability to call
# functions in other classes

# if both solutions solve the problem of reuse, then which one is appropriate
# in which situations?
# the answer is incredibly subjective

# 1. avoid multiple inheritance at all costs.  as it is too complex to be
# reliable.  if you are stuck with it, then be prepared to know class
# hierarchy and spend time finding where everything is coming from

# 2. use composition to package code into modules that are used in many
# different unrelated places and situations

# 3. use inheritance only when there are clearly related reusable pieces of
# code that fit under a single common concept or if you have to because of
# something you are using

# do not be a slave to these rules.  the thing to remember about object
# oriented programming is that it is entirely a social convention programmers
# have created to package and share code.  because its a social convention
# but one that is codified in python you may be forced to avoid these rules because
# the people you work with.  in that case, find out how they use things and then
# just adapt to the situation 
