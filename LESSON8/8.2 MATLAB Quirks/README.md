# MATLAB'S Quirks

MATLAB has some "fun" quirks that you will learn to hate as you use it.

## Typing

MATLAB is a dyanmically and weakly typed language. What does this mean? Well it is like python. When you make a variable you do not need to put a type infront of it, unlike java. Here is an example:
Java
```java
int x = 0;
```
Matlab
```MATLAB
x = 0
```

This also means you can do something like this

```MATLAB
x = 0
x = "Hello"
```

This is very similiar to Python.

## Array Indexing

This is probably the WORST part of MATLAB. Arrays, vectors, matrices, are 1 indexed. That is to say, if you want to access the first entry in a vector, you would do `vector(1)` instead of `vector(0)`. This is completely against what you have learnt in C, C++, and Java. You will have to keep this in mind as you create your vectors and arrays, and the index might be meaningful for what the data represents. For example, say you define a vector that contains the amplitude of a function from `x = 0` to `x = 10`, well you would want the first entry in that vector to refer to `x = 0`, but you would access it by typing `vector(1)`. This mismatch is a very common logic error encountered when solving problems in MATLAB.
