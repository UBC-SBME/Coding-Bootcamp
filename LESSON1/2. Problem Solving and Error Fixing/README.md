## What if Something Goes Wrong?

You might be tempted to panic if after your first attempt to compile something you get some cryptic error from the compiler. Don’t panic! It is very rare for code to work perfectly the first try! Luckily, Java has some very descriptive errors, so if you can't make sense of the error you can usually get away by copying the error into google and looking for help in the first match it gives you (typically your friend Stack Overflow!). Algorithmic bugs are harder to spot, but for now print statements are a good tool for debugging. In Lesson 2, more specific debugging tips specific to the programming tool used in CPEN 221 will be given.

## A More General Problem Solving Technique

One element students often struggle with in programming is solving programming problems in an algorithmic way. This is extremely difficult to teach. Sometimes this approach slowly develops until eventually it “clicks”. 

Here is a quick rundown of how to solve an algorithmic problem. 
1. Read the problem carefully several times to understand what it is asking for. Sometimes examples of inputs and expected outputs are provided. If not, sometimes you can create these examples manually (if the task is not too complex). 
2. Try to make an example with a very simple input. For example, say the assignment is reversing an array, you could make the array {1, 2, 3}, which is fairly small, and easy to trace through the algorithm. 
3. Try to outline the code by writing out comments of what each part of the algorithm does (which can often be broken down into sub-parts). Keeping the easy example you made (or was provided) in mind can help in this process. For example, for reversing an array requires direct modification of the original array, you might want a section dedicated to copying the contents of the array to a new array, and another section for placing the copied contents back into the original array reversed.
4. Write your code!
5. Try your code on a variety of inputs, including larger examples to see if it works. In CPEN 221, you will learn about how to properly test your code, but for now using a wide breadth of different inputs is good enough. Be creative here. For example, give it an empty array as input as to see if it still works!
6. If in the test in step 5 something fails, start to debug. Print statements can work, but for more advanced algorithms using the debugging tools present in IDEs is essential. This will be covered in Lesson 2.


Here, we have outlined one approach to solving algorithmic problems. You may find that a modification of this approach, or another approach works best for you. 
