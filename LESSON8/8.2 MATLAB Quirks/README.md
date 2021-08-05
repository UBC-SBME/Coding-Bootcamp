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

## Accessing Arrays and Matrices

MATLAB does this with brackets and indices. For example, say we want to acces the 3rd element in a vector, we will type something like `vector(3)`, where `vector` is whatever you named the variable. Pretty simple! For matrices, or something that is has rows and columns, then you access them by giving MATLAB for each row and column. Say you want to access the element in a 2D matrix that is in the 4th row and 2nd column, you would type `matrix(4,2)`, again where `matrix` is whatever you named the matrix. This continues for any N dimensional matrix, just plop in all the coordintes. The general form is `matrix(x1,x2,...,xN)`.

What about if you want to access a portion of a vector, say elements 3 through 5? Well in matlab, we have the `:` operator. What this does is generate a sequence. For example, if we type `3:5` it will generate the sequence `3,4,5`. This can be used to interface with vectors and matrices! Just replace the single coordinate with that fun `x:y` statement. For example, to acces the 3rd through 5th element of a vector, you would type `vector(3:5)`. Similiarly, to access the 3rd through 5th row and 2nd thru 3rd column of a matrix, type `matrix(3:5,2:3)`.

What if you want an entire column? Well instead of typing `1:numberOfRows` you can just do `:`. So for example, if you want the entire first column of a matrix, type `matrix(:,1)`

Finally, you can also generate more specific sequences with this. You would type something like `x:y:z`. You read this like "Make me a sequence starting at `x` and ending at most `z` where each value is `y` greater than the last. For example, `1:2:5` generates `1,3,5`. Note the at most. If you type `1:3:6` you still get the sequence `1,3,5`. Like all of this other stuff, you can use that sequence to get the 1st, 3rd, and 5th element of a matrix.

Essentially, when accessing data from a matrix (or vector or array), you can pass it a vector who's elements represent indices of that matrix, and you will get those values at those indices.

## The `;`

In MATLAB, you do not have to end a line with `;`, but it is recomended. Unlike C, C++, and Java, where `;` tells the complier that single code statement is complete, it tells MATLAB not to print anything to the console. You will notice that if you neglect to add `;` to the end of the line usually your console is filled with a bunch of text. This is especially annoying if you are modifying a bunch of enteries in a matrix, as each time an entry is modified it will print the entire matrix to the console. This also slows down your program significantly.

So how does MATLAB know when a line ends? Like Python, MATLAB loves white space. Statements are seperated onto their own lines. This also means that for for loops or if statements, code in the body of the for loop or if statement is indented. Here is an example
```MATLAB
if x > 1
  x = x + 1;
end
```
Notice the indent. Additionally, you need to tell matlab if a for loop or if statement ends by typing `end`. How fun.

## Functions

Functions are weird in MATLAB. Luckily, you likely will never have to write one for any of the classes you take. There are two types. One is a function like you have seen before in programming and the other is a function in the math sense. Lets cover both quickly.

The normal function is very similiar in declaration to Java. Lets cover the most general version.

```MATLAB
function [y1,y2,...,yn] = myFun(x1,x2,...,xm)
  % a bunch of code that does stuff
end
```

Every function needs to be declared by the keyword `function`. `[y1,y2,...,yn]` is all the data returned by the function. `x1,x2,...,xm` are all the inputs. Nothing too crazy, and you will likely never have to write this sort of function.

The other type is very simple. Here is an example

```MATLAB
F = @(x) 2*x^2 + 1
```

To translate this to the common math form, this is f(x) = 2x^2 + 1. This is a great way to write out math functions nicely in one line, and is espeically useful if said function is used often in a MATLAB file, or if it cleans up a particularly nasty part of code. This is heavily used in BMEG 371.



And thats basically it for some of the weird MATLAB quirks. The rest is usually self explanitory, minor, or cleared up by someone on Stack Overflow.
