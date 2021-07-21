# Why So Many Languages?

This is a question many of you might have right now. Why are there so many programming lanuguages? Why not just 1 super language that does everything? 
The most simple answer is another question: Why are there so many types of hand tools? Why have a wrench, a hammer, a screwdriver, and a CNC machine when you could have one super tool? The answer is each is designed to do a specific task well. Sure you can get some ultra tool that does many things poorly (though they have their place in), but sometimes having a specific tool for the job is prefered.

The exact same idea can be applied to programming languages. They are just tools, and each has its own specific use case. Typically, this use case is what fundamentally dictated the design philosophies of that language, hence why each is different. Let's run through some quick examples of the languages you will likely see through your career.

## C

Ah good old C (not to be confused with C++). C (designed as the successor to B) is really useful for [embedded systems](https://en.wikipedia.org/wiki/Embedded_system) where you need to program at a very low level, but don't want to use an [assembly language](https://en.wikipedia.org/wiki/Assembly_language). This is why you used C for programming the DAC in APSC 160; this is where good old C shines. C is quite old too, which in our case, is a good thing since it has a lot of support. What is bad about C is that it lacks a lot of modern programming features that we could find useful. The most grievous example is how a string in C is a char array. Another thing that C (and its successor C++) allow the programmer to do is to directly mess with pointers. Don't worry about pointers for now (though if you want to read up on them, they are really interesting), but just know they allow you to program some very interesting algorithms. Also, C is really, really fast.

## C++

C++ is C with more modern additions that make it less of a pain to work with. Notably, it has support for objects (which C lacks) which makes it much more useful for modern larger programs. In addition to letting the programmer mess with pointers, C++ is incredibly fast as any C++ (or C) code is compiled directly to machine language, meaning your computer hardware runs it directly. The issue with this is that it places a lot of trust on the programmer, and does not hold your hand. For example, if you are not careful, you can get memory leaks (the program fills up your ram, will eventually crash the program or your computer) very easily with C and C++. This headache does not happen in languages like Java that implement garbage collections (a method that looks at memory and frees it for use if the data in that memory won't be used again).

C++'s speed - as well as the large support of libraries - is what makes it so popular today. Additionally, the speed can be useful for more advanced signal processing. If you take CPSC 221 you will learn a bit of C++.

## Rust

Rust is a relatively new language that is meant to be a successor to C++. It is notable for also being compiled to machine language, but also being designed for asynchronous programming. Although we won't cover this in our course, just know that an asyncronous program can do more than one thing at a time. You know how your computer advertises that it has 4 or more cores? Well, async programming lets you use each core at the same time. For example, if you wanted to do a repetitive mathematical calculation on an array of 10,000 items, instead of doing that calc one item at a time, you could make your program asynchronous, letting each core of your CPU do that calculation on a different entry in the array. If you have 4 cores, that is 4 times the work completed in the same time!

## Java

Java was one of the first big object-oriented languages, and because of this it is still popular today. Java's biggest claim to fame is the Java Virtual Machine (JVM). Essentially, when you compile a Java program, it is not run directly by the CPU, but rather it is converted to Java byte code and run by the JVM. The benefit here is not only garbage collection (so no pesky memory leaks) but also how portable Java code is. Instead of having to rewrite your code for every type of computer (Windows, Linux, MacOS, Android, etc.) if it has a version of the JVM, you can just run it without major changes. Very convenient. The downside of this is that Java programs generally run slower than an equivalent program in C++ due to the overhead of the JVM (you can test this if you would like with assignment_1).

# JavaScript

JavaScript is used a lot for web development and making web pages. If you try to make a website you will likely use it. JavaScript is notable for two things. First, it uses JavaScript Object Notation (JSON) which is very popular - this means other languages need to use extra (really annoying) libraries to try and parse JSON formatting strings. Another is that it was created in 10 Days, and boy does it show.
Also despite the name, it isn't super related to Java. The name was chosen just because Java was popular at the time. This is the programming equivalent of Greenland, notable for being not green most of the year.

## MATLAB

MATLAB is the language for math stuff. It was made for math. It is not particularly fast (instead of any virtual machine like Java, each line is complied individually at run time, which is very slow), but it has so many math features and libraries that it makes it worthwhile. From linear algebra, to calculus, to some really good libraries for signal and image processing (though if speed is needed C++ is a better option). It also has great tools for visualizing data (graphs) and a really great set of tools for control systems (simulink is particularly great, though it is not a programming language per say). Additionally, it is possible to write C++ or C code that is then run in MATLAB, which can make some MATLAB projects run much faster.
One annoyance with this language is that all arrays start at index 1. This is different than the previous languages, which all start at 0. You will likely come to hate this inconsistency.

## Python

Python is a very interesting language. Like MATLAB, it is possible to write pre-compiled C or C++ code to make it faster. More interestingly, it is loosely typed, which is to say each variable does not have to be of a specific type, for example, if I were to do this in C++

```cpp
int x = 1;
x = "hello";
```

You would be called a heretic, but in Python if you do

```python
x = 1
x = "hello"
```

It just works. This can be both incredibly useful and the worst thing ever. It is the worst, as types still can have limits or quirks, which can lead to archaic bugs. For example, the default integer type in python has no limit, it can be any number, no matter how large. This is different compared to C, where the integer can only have a value from -2,147483,648 to 2147,483,647 inclusive. The issue is python has a library called numpy, a useful and fast library used for matrix operations. Its speed comes from how it is written in C (in python, you can write modules in C that are compiled before runtime, speeding up your program). This comes with a fun annoyance where secretly, numpy integers are just C integers, meaning they having this limit, unlike the normal python integer. This means if you write a program that produces a large integer value, it can overflow if it is a numpy integer. This kind of bug is really hard to spot! This would be fixed if python was strongly typed.

Another feature of python is its use of white space. You will notice in the code segment above python lacks any `;`, instead of using white space as an equivalent. This can make code look cleaner, though some programmers still like the semicolon, as it has its niche uses. One example is in Java (or C++) you can split a line in two to make it look cleaner:

```Java
int x = reallyLongFunctionName(ReallyLongVariable1,
                               ReallyLongVariable2);
```
But this is not possible in Python.

Finally, Python is notably slow by default, as each line is complied at run time. It is a great scripting language, and easy to use, but if you want speed use C++.

Python has a lot of useful libraries, making it almost the swiss army knife of languages. It has great libraries for scientific data analysis (SciPy, Numpy, Jupyter Notebook, MatPlotLib), signal processing (SciPy), basic game creation (Pygame), and machine learning (Pytorch). The best part is each of these libraries is mostly written in C, so they are actually fast as runtime. The bad part is each tries to include the syllable "Py" in its name, which just kinda looks tacky.

## R

R is a language mostly used for statistics. It has some weird syntax with assigning variables, but otherwise is basically a statistics version of MATLAB. It also has some great tools for bioinformatics, which you will get to use in BMEG 310. The editor R Studio is also pretty nice.

## Assembly

Assembly is as close to directly writing what the CPU does as you can get, without writing machine code. It is not often used today, is specific to the hardware, and is using instructions, with an instruction being something the CPU does. For example, loading data from a memory address to a cache is an instruction. You probably won't use this one, though if you want to program a game for the NES or an ancient computer, this is the way to go. It is the fastest programming language, but you have to sell your soul if you want to program anything in it.

## Others

There are probably a bunch that aren't listed here. You might run into them. Just remember to think about what they are designed to do, and if they are useful for your current application.
