## 1) Choosing a Basis

Our first lesson may be the most important: how to learn other programming languages. All of you should have some knowledge of C, the language used in APSC 160. You should also be familiar with a bit of MATLAB from MATH 152. Sadly, the world does not use only C / MATLAB for everything. Throughout your degree, you will likely use a multitude of other languages, including:
- Python 
- Java 
- C++ 
- R THREE

Throughout your career, you might use other languages too, like Rust or JavaScript. This may seem daunting at first, but much like spoken languages it becomes easier to learn new languages after learning one. Now, this is our first path split. Some people prefer to learn a new coding language on its own by just programming a small program based on some idea they have. Others like to start with a language they know, and translate ideas to a new one. As an exercise, we will translate a program from C (where you have experience) to Java (which you will soon be using). If you prefer to skip the translation and learn Java from scratch, just skip ahead and try to translate the pseudocode provided at the bottom of this document directly into Java.

## 2) Choosing a New Language

So you have chosen C as the basis for translating into your new language. The next question is, what language do you want to learn? For this course we will be focusing on Java, but in the future (or now, if you would prefer learning C# for CPEN 223), this is an important question you will need to answer. The best way to narrow things down is to think about what you are going to use the language for. Conveniently, this question is usually answered for us undergraduates. We need to learn the language for a course! In the future, when things are a bit more open ended, this question will become a bit more difficult to solve. Usually, looking at the features of the language is a good bet. Sometimes, looking at the libraries available in the language is more useful. As a reminder, libraries are a collection of pre-written code by other users of the language, typically designed for a specific purpose. For more specifics, look to the "Why So Many Languages?" section.

## 3) Familiarizing Yourself With Some Basic Syntax Differences

After you select your language, it is time to familiarize yourself with some of the basic differences between your new language and the basis. This does not have to be too in depth! Focus on the syntax differences specifically! A google search of “{Basis Language} and {Language to Learn} differences” is a great first step. Another possible search term is just “{Language} beginners guide” or “How to write “Hello World” in {Language}”. All of these will show you some basic formatting in your language, and you can usually spot the differences between languages like this. The easiest example between Java and C is the odd amount of boiler plate needed for a basic Java program compared to a C program. In C, to get started with a simple main function, you would write something like:
```java
int main() {
   //Your amazing program here!
}
```

Java however has a lot more boilerplate, specifically you would start with:
```java
class Main {
 public static void main(String[] args) {
   //Your amazing program here!
 }
}
```
You can immediately notice the differences between the two. Specifically, your main function has to be inside something called `Main` which is a class, has to have these weird `public static` keywords in it, and has an input variable called `String[] args`. As you might remember from APSC 160, `void` means a function returns nothing, so at least you can recognize that. Without getting into the details of everything, the `String[] args` is an array of Strings (this might be new to you!) that represents the input arguments the user gives, and the rest of the extra stuff is a consequence of Java being built as an object oriented language. All of this can be safely ignored for now, though importantly the word after `class` must be the exact same as the file it is in (so expect the bit of code to be in Main.java). Just treat this code as a necessary boilerplate. We will cover all of this in future lessons.

Some people find programming books useful. We recommend “Head First Java” as a way to learn a bit of Java in preparation for CPEN 221. 

## 4) Writing Your First Simple Program, and Some Companions

Our next step on the journey of learning is to create a simple program to get some idea of how your language works. For now, using an online coding platform is sufficient, though in the future installing an IDE is a good idea (this will be done in lesson 2, don’t worry!). We would recommend using replit to run the code for now. It is an easy to use website that lets you program in many different languages, which is useful for this exercise!

Here is the classic “Hello World” program. It is simple, and usually it can give you some key insight into the particulars of a language. For example, our C version would look like:
```cpp
#include <stdio.h>
 
int main() {
  printf("Hello World!")
}
```

This should look familiar, most of you have written this (or something similar) in APSC 160. How would we go about translating this to Java? Well, you could just google “how to write Hello World in Java,” but a better method is to google a more generic question, such as “how to print a string in Java”. [Let's google this together!](https://www.google.com/search?q=How+to+print+a+string+in+java)

And this is likely where you will meet the first party member on your quest: Stack Overflow. Stack Overflow is a fantastic website where users post programming questions and others answer them. Many of us have used this website hundreds (perhaps thousands) of times throughout our programming career. Posting a question on stack overflow is almost always unnecessary since your question has usually already been asked and answered, and asking duplicate questions is poor practice. Only ask a question if you can not find a similar question, and be sure to format it all correctly (stack overflow has a guide for asking questions correctly).

Another option is to google [“how to print a string in Java, Java Doc”](https://www.google.com/search?q=How+to+print+a+string+in+java+Java+Doc). This will lead to your next companion, the Java Documentation. Java Documentation is incredibly useful for learning how to use the built in types in Java. For this basic program, you won’t need to dive in too deeply, but when you start to use fancy data types such as ArrayList, googling “Java Doc ArrayList” will give you a page with every single function that list can use. Extremely helpful!

Of course, don’t limit yourself to just the Java Documentation or Stack Overflow. There are many other websites that have useful programming knowledge / tutorials that you will discover on your quest.

With any luck you found out how to print a string. We suggest you try this yourself before looking at the answer. 

It should look something like:

```java
class Main {
 public static void main(String[] args) {
   System.out.println("Hello World");
 }
}
```
Despite the simplicity of this program, it has given you a future key insight about Java. Specifically, what is this business about `System.out.println`? Sure, the `println` vaguely looks like C's `printf`, but what about that odd `System.out.` before it? Keep this in the back of your head for now, we will cover this heavily in future lessons! For now, just treat the entire `System.out.println` as an oddly long function name.

## 5) Transfering Deeper Knowledge

Now onto the fun stuff: translating a more difficult program. Now, you can either just think of some program off the top of your head and attempt to write it in Java (essentially turning pseudocode into a program), or you can first write a program in your basis language, C, and then translate that. The second option might not always be best. For example, say you want to learn how to multiply two matrices in MATLAB. Writing a program that does this in C is considerably harder than writing it in MATLAB, so method 1 is advisable. For the purposes of this lesson, we will go with option 2, as C and Java are pretty similar and we want to give you more practice in translating code. Option 1 is generally preffered. If you are confident, try directly writing the program in Java!

What should you aim to translate into your new language? Typically, it should just be whatever you need to work with at the time. For example, if you don't need to use some niche language feature, don't learn it. It would be useless to learn about intrinsics in C++ (a very complex but useful way to do calculations quickly) if you only want to print "Hello World." In our case, it is best to try to translate the bulk of our C knowledge from APSC 160 to Java. Specifically, a program that involves an array, an if-statement, a for-loop (or any kind of loop really), a print-statement, and a function should cover most of APSC 160.

If you would like an exercise in reading pseudocode, try to translate this pseudocode into C (or directly into Java if you would like a challenge!)

If you aren't familiar with pseudocode or want a refresher, check out the "Pseudocode, Why" folder in this lesson!

Translate this pseudocode to C, and then to Java (or directly to Java):
```
Main:
 Array foo = {0, 1, 2, 3, 4}
 Array bar
 For i from 0 to 99:
  bar[i] = i
 print("The The number of even numbers in foo is:")
 print(countEvenNum(foo, 5))
 print("The number of even numbers in bar is:")
 print(countEvenNum(bar, 100))
 
 
countEvenNum(Array arr, size):
 count = 0
 for each element in arr:
   if element is even:
     increment count
   else:
     do nothing
 return count
```

To check if your code works, you would expect to print a 3 out for the number of even values in foo, and a 50 for bar.
