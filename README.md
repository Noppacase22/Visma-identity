# Visma-identity
 
This repository is done as a programming task for Visma Solutions - Summer Trainee 2023: Software Developer

### Problem:
Visma Solutions Oy is developing an application for identity management. With the application, users can login to integrated applications, confirm payments and sign documents. Identity management is a mobile application, and other apps can call its services through deep linking. When this is used, the identity management application would open automatically from the right in-app location. In this assignment, you will be implementing a part of this logic.

### Task:
Your task is to design and implement a class which is responsible for identifying what kind of requests it receives. Other apps can call the identity app using the scheme visma-identity.

A uri consists of three parts:
Example: visma-identity://login?source=severa
Scheme: visma-identity
Path: login
Parameters: source=severa

The class needs to satisfy the following requirements:
1. It takes the following information as input
    URI (type: string)
    Example: visma-identity://login?source=severa
2. It has to parse and validate that:
    Used URI scheme is right: visma-identity
    Path is one of the allowed: login, confirm or sign
3. All parameters for a path are valid
4. Requirements for the parameters:
      - Path login:
      source(type:string)
      Example: visma-identity://login?source=severa
      - Path confirm:
      source(type:string)
      payment number(type:integer)
      Example: visma-identity://confirm?source=netvisor&paymentnumber=102226
      - Path sign:
     source(type: string)
     documentid(type:string)
     Example: visma-identity://sign?source=vismasign&documentid=105ab44
5. Class returns:
     Path
     Parameters as key value pairs
6. Is designed using the practises of object-oriented programming
7. Implementation needs to have a client, which uses the new class. You can for example implement the client as another class that uses the relevant methods.

# The code
## visma-identify.py
This is the main interface used to run and test different inputs.
It has a main function, a menu, and two options for testing.
The main purpose is to allow the use of the identify class with a CLI.

### menu
The menu runs a loop until the user gives '1' or '2' as input, and then returns the value as integer

### main
Two paths depending on menu input
1: Simple tests that I wrote to check different parts of functionality
2: Using user input to test validity of a string, and therefore the code.

## identify.py
The "main" class of the task.
Calling Identify.identify creates a URI-class object, which is used to store parts of the given uri and check for incorrect inputs.
Method wrongID is called when the given uri string is found to be incorrect.
Takes errorCode: int, returns message as string

## uri.py
Used to store given uri data and check it's validity.

Methods checkScheme, checkPath and checkParameters each check their named part of the uri and return False if found incorrect.
Has conflicting logic: checkParameters sets self.parameters value, while checkScheme and checkPath are called after setting their respective variables in Identify.identify.

Method returnString(self) returns a correct uri's Path and Parameters in the following format:
Path: {self.path} \nParameters: {self.parameters[0]}{self.parameters[1]}
Can be easily tweaked to remove redundant strings and return only the parameters, or change the visuality of parameters, which are given as 2-slot lists.

Method getPath(self) returns self.path. Currently no use, but can be useful at some point.

Method getParameters(self) returns list of parameters and their values. Currently not in use.


# Self reflection
The problem seemed a bit daunting at first since it's been a while since I've done any object oriented programming, but I think my end product is somewhat satisfactory. Wether it is or not, I'll surely get good feedback on what went wrong.

After I got over my initial overreaction and anguish, I realized this is a "rather simple" task of string parsing. My initial thoughts of structure were blown away by the realization that it couldn't be functional programming, which is what I'm most recently familiar with. I don't know if my final structure is that good. I started with a single class that then branced to two classes. Some methods could be in either class and I'm not sure if the split was even necessary. The URI-class can't even be accessed outside the identify-method, though it's not exactly necessary at the moment.


## Time estimates
The time limit was about 2-3 hours.
Effective thinking time: 15-20 minutes
Effective coding time: ~2 hours or slightly more
Effective documenting time: ~30 minutes

It is possible that I've spent more than the allocated 3 hours on this. If I were to try again I'd start planning the code with examples immediately, cutting the initial thinking time. Writing mediocre code and improving it later is faster than trying to optimize it beforehand.

## Improvements
If I had unlimited time on the project, first thing I'd do is get feedback on how to organize my files and methods. I am still unsure if my design is within good OOP guidelines. Another thing to do better is testing. I have never done assert tests on my own, and implementing them could be useful and fun. They would also help catch the few bugs I undoubtedly missed on my own.