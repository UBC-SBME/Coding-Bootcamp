# Pseudocode, Why?

## What is it?
If you don't remember what pseudocode is from APSC 160, it is the plain language description of your program. Pseudocode describes what your program does, without explicitly writing how it does it (in a specific programming language). Pseudocode describes the functionality of a programming without necessary writing any of the code:

Here are a few things to keep in mind when writing pseudocode
* Break the problem down into **smaller parts**
* **Don't write an essay**, use logical notation and simple statements to illustrate your solution
  * Math heavy software will even use math symbols and notation
* **Don't write the program**, the point of pseudocode is that it describes the software
  * That being said, don't be afraid to use syntax from different languages (Python is a good example)
* **Ident**. Being able to read pseudocode is just as important as the content in it, so make sure everything is organized

Examples in different styles (I borrowed the examples from [here](https://www.unf.edu/~broggio/cop3530/3530pseu.htm)):

**Example 1.** Pseudocode: Pass/fail program
```
  INPUT: grade;

  IF(grade >= 60)
      Print "passed"
      Return true
  ELSE
      Print "failed"
      Return false
  ENDIF

```

**Example 2.** Pseudocode: Compute average grade
```
Set total to zero
Set counter to zero

Input the first grade

while the user has not finished entering grades
   Add this grade into the running total
   Add one to the grade counter  
   Input the next grade (possibly the sentinel)
endwhile

if the counter is not equal to zero
   Set average to total divided by counter
   print average  
else
   print "no grades were entered"
endif
```


## Why do we need it
Pseudocode is used everywhere, including in algorithmic research, software design prototyping, and even in a lot of math problems. Computers are excellent in executing instructions, so being able to adequately articulate the list of instructions you want the computer to preform is essential in creating programs - specially if you are collaborating with other humans!

## How to write pseudocode
We strongly suggest that when you are attempting to write pseudocode, that you break the pseudocode into simple units.

For example, the problem that we provided in **Assignment 1** can be broken down into three units: (1) make an array, (2) make evenOrOdd function, and (3) return number of even elements. Thus, when you begin to write your program, having these units in mind will allow you to work on each part individually. This will also make finding a specific problem a lot easier too since each part is sectioned off into units.

Try to do these examples on your own:

1. FizzBuzz
  > Write pseudocode for a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

  * Ex. 1, 2, Fizz, 4, Buzz, ...

2. Are all brackets closed?
  > Write pseudocode for a program that reads a string (an array of characters) of brackets and ensures that every opening bracket has a closing brackets

  * Ex. "()" returns True
  * Ex. "(()" returns False

## Resources
* [What is Pseudocode by educative](https://www.educative.io/edpresso/what-is-pseudocode)
* [Bob Roggio from University of North Florida](https://www.unf.edu/~broggio/cop2221/2221pseu.htm)
* [ScienceDirect](https://www.sciencedirect.com/topics/engineering/pseudocode)
