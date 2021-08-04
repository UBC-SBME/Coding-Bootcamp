# MATLAB'S Quirks

MATLAB has some "fun" quirks that you will learn to hate as you use it.

## Typing

MATLAB is a dyanmically and weakly typed language. What does this mean? Well it is like python. When you make a variable you do not need to put a type infront of it, unlike java. Here is an example:

```java
int x = 0;
```

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

This is probably the WORST part of MATLAB. Arrays, vectors, matrices, are 1 indexed. That is to say, if you want to access the first entry in a vector, you would do ~vector(1)~
