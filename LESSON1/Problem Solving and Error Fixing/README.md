## What if Something Goes Wrong?

You might be tempted to panic if after your first attempt to compile something you get some archaic error from the compiler. Don’t panic! It is very rare for code to work perfectly the first try! Luckily, Java has some very descriptive errors, so you can usually get away by copying the error into google and looking for help in the first post it gives you (typically your friend Stack Overflow!). Algorithmic bugs are harder to spot, but for now print statements are a good tool for debugging. In Lesson 2, more specific debugging tips specific to the programming tool used in CPEN 221 will be given.

## A More General Problem Solving Technique

One element students often struggle with in programming is solving programming problems in an algorithmic method. This is extremely difficult to teach. When I took CPEN 221 back in my second year, this method just sort of slowly developed until it finally “clicked” in my head. Sadly, this click happened in the middle of the term, so my initial marks in the course weren’t the best. Luckily, despite the reputation, it is a forgiving course, so I was able to pull my grade up significantly by the end of the course!

Here is a quick rundown of how I solve an algorithmic problem. 
1. I read the problem carefully several times to understand what it is asking for. If the professor is good / kind they will usually include a couple examples of an input and expected output. 
2. I try to make my own example with a very simple input. For example, say the assignment is reversing an array, I would make my example the array {1, 2, 3}, which is fairly small, easy to think about. 
3. I try to lay out the code in by writing out comments of what I want to do for each part of the algorithm, usually with the easy example I made earlier in mind. For example, if reversing the array requires direct modification of the original array, I might want a section dedicated to copying the contents of the array to a new array, and another section for placing the copied contents back into the original array reversed.
4. I try my code on larger examples to see if it works for a variety of inputs. In CPEN 221, you will learn about how to properly test your code, but for now using a wide breadth of different inputs is good enough. Be creative here. For example, give it an empty array as input as to see if it still works!
5. If in the test in step 4 something fails, I start to debug. Print statements can work, but for more advanced algorithms using the debugging tools is essential. This will be covered in Lesson 2.


Of course, this is just what I do. Ultimately it is a very unique mindset most of us don’t have much experience in, so develop what works for you. What I can say is that 90% of programming problems boil down to using a for loop with some logic, or some generic data manipulation.
