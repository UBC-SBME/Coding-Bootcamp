# Pseudocode, Why?

## What is it?
If you don't remember pseudocode from APSC 160, it is a plain language description of your program. Pseudocode describes what your program does, without explicitly writing how it does it (in a specific programming language). Pseudocode describes the functionality of a program without necessary writing any of the code:

Here are a few things to keep in mind when writing pseudocode
* Break the problem down into **smaller parts**
* **Don't write an essay**, use logical notation and simple statements to illustrate your solution
  * Math heavy programs will even use math symbols and notation
* **Don't write code**, the point of pseudocode is that it describes the algorithm
  * That being said, don't be afraid to use syntax from different languages (Python is a good example because it reads like pseudocode)
* **Indent**. Being able to read pseudocode is just as important as the content in it, so make sure everything is well organized

Examples in different styles (borrowed from [here](https://www.unf.edu/~broggio/cop3530/3530pseu.htm)):

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
Pseudocode is used everywhere, including in algorithmic research, software design prototyping, and even in a lot of math problems. Computers are excellent in executing instructions, so being able to adequately articulate the list of instructions you want the computer to preform is essential in creating programs - especially if you are collaborating with other humans!

<code><mark> We should move this somewhere else </mark></code>
## How to write pseudocode
We strongly suggest that when you are attempting to write pseudocode, that you break the algorithm into simple units. Here, we will go though an example together. 

*Write an algorithm that checks to see if any of the items in a vending machine need restocking (<2 units) and notifies the owner if any are.*
We will solve this using the problem solving approach used earlier in the lesson.
1. **Read the question carefully.** How many of the items are we checking? Who are we notifying? What is the threshold at which the notification should be issued?
2. **Make an example.** What would happen if the stock values are (2,4,6,7)? What about (5,7,3,1,8)?
3. **Write algorithm steps in comments**

```java
//
```

At a high level this is what our algorithm looks like:
```
INPUT: stocks;

if ( any( stocks < 2) ):
  notification("Low stock", owner)
 ```
 This is a great starting point, but this problem can be broken down further as we are assuming the existence of an `any` function and that `stocks` can be compared to an integer (`2`). This is often not possible. Here's another attempt to break it down further:
 ```
INPUT: stocks;

for item in stocks:
  if ( item.count < 2 ):
    notification("Low stock", owner)
 ```
 Now we use a for loop to iterate over the individual items in the vending machine, and test each item individually to see if its stock is low (here, we're treating `item` as an object with `count` as a field - more on this later). Obviously item could be something else, and this will depend on the problem prompt more than anything. For example, you could have two arrays, `stock` and `id` where element `i` (with `i` being an index) in `stock` is the amount of that item left, and element `i` in `id` is the name of that item. If you would like, try to complete steps 4-6 of the problem solving technique on this prompt using the 2 array method in Java.


For example, the `countEvenNum` function that we provide in **Assignment 1** can be broken down into three units: (1) make an array, (2) make `countEvenNum` function, and (3) return number of even elements; the `countEvenNum` function can be . Thus, when you begin to write your program, having these units in mind will allow you to work on each part individually. This will also make finding a specific problem a lot easier too since each part is sectioned off into units.

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
