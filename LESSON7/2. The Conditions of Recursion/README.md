# Conditions of Recursion
When you are writing recursive code, it is important to think about *what exactly you are doing* and *when to stop*. All recursive algorithms typically follow this idea. We already got introduced to this idea in the last lesson, when we we're writing `factorial(n)` and saw that if we didn't specify that `factorial(1) = 1` then the program would run forever. Moving forward, we want to reconcile being able to break complex problems into simple ones and also think about *what exactly we are doing as well as when to stop*.

This idea can seem difficult when you're being introduced to recursion, so we'll go through an example of how the computer really handles it, so that this makes a bit more sense.

<p align="center">
<img src="https://imgs.xkcd.com/comics/fixing_problems.png" />
</p>
<p align="center">Funny meme</p>


To make it easier, we will define 2 conditions that your recursive code **must** follow.

## There Are 2 Conditions:

1. Base Case (Exit Conditions)

  * The condition in which the function will stop "calling itself"
  * Eg) `F(1) = 1`


2. Recursive Step

  * The line of code that actually calls itself
  * Eg) `F(n) = n  * F(n-1)`



#### Background
Just a quick primer on how to the computer views your code. Whenever you run your program, your computer makes a list of the different functions that are being called. This list is called the **stack**.

Consider the factorial code from last lesson:
```py
def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)
```

Below is a table that visualizes this stack process, time will progress from left to right (increasing t). The top row tells us the function **currently being called**. The middle row will tell us **which function is waiting for an output**.

Suppose we call `factorial(4)`.

| Function call  | `factorial(4)`  | `factorial(3)`  |  `factorial(2)` |  ... |
|---|---|---|---|---|
| Waiting for output... |   | `factorial(4)`  | `factorial(3)`<br> `factorial(4)`  | ...  |
| t = 0 |  1 |  2 |  3 | ... |



### Base Case
The base case will be determined by the parameters that are passed into the function. For example, in the `factorial(n)` example we had `factorial(1) = 1` as our base case. This was specified as every time we call the function, it explicitly check for that condition. It does this in these lines of code:
```py
  if n == 1:
    return 1
```

In order to emphasize the conditions of recursion, we will take a look at our first attempt at the factorial code:

```py
def factorial(x):
  return n * factorial(n-1)
```

We will view this code in the context of the computers **function stack**. Let's call `factorial(3)` using this code:

| Function call  | `factorial(3)`  | `factorial(2)`  |  `factorial(1)` |`factorial(0)` | `factorial(-1)` |`...` |
|---|---|---|---|---|---|---|
| Waiting for output... |   | `factorial(3)`  | `factorial(2)`<br> `factorial(3)`  |`factorial(1)` <br> `factorial(2)`<br> `factorial(3)` | `factorial(0)` <br> `factorial(1)` <br> `factorial(2)`<br> `factorial(3)`| ...|
| t = 0 |  1 |  2 |  3 | 4 | 5 | ... |

This is called a (*drumroll please*) **stack overflow**. There is a certain limit of function calls a computer can do, this is dictated by the amount of memory or RAM the computer has. Thus, without a base case, the computer will infinitely recurse until it can't anymore. I know this might be obvious, but in more complex problems you will have to think hard about the base case.

To fix the issue we had in this  example, we defined a base case of `factorial(1) = 1`. This will then let the stack will collapse and the recursive code will now work.

| Function call/Output  | `factorial(3)`  | `factorial(2)`  |  `factorial(1) = 1` |`factorial (2) = 2` | `factorial(3) = 6` |
|---|---|---|---|---|---|
| Waiting for output... |   | `factorial(3)`  | `factorial(2)`<br> `factorial(3)`  | `factorial(3)` | | ...|
| t = 0 |  1 |  2 |  3 | 4 | 5 |

### Recursive Step
Thinking of a recursive step is a very important step in building recursive code. The approach we recommend that you take is by asking yourself "How would the answer to a **smaller** case of the problem help me get to an answer to the larger case?". Basically, break the complex operation down into a more simple operation; once you have that simple operation, you can write the code for it and finish your program.

Lets, elaborate on this process:

When your designing a recursive function, we recommend that you go through this thought process:

1. **Break the problem you are trying to solve, into a simpler one**, even if its only one step simpler

2. **Believe that your function will solve the simple problem**. Trust that you can solve this simple problem, like really believe it

3. Now that you can solve the simple problem, **think about how you can solve the more complex one** (if at all, sometimes solving the simple step will solve the complex one via recursion)

Like all things, this makes more sense with an example. Lets go ahead and use the Fibonacci example

**If you haven't done the assignment, please do before reading the example section**

<br>
<details><summary>Fibonacci Example</summary>

Let's preform step one, breaking the complex problem down into the simpler one. Thus, in order to compute the Fibonacci term of one term we need to compute the sum of the two previous Fibonacci term.

Okay so we can write:

```py
def fibb(n):
  return fibb(n-1) + fibb(n-2)
```
Okay, now moving onto step 2. Do we believe in this function?
No, there's no base case. Let's write one.

We know that the first two terms of the Fibonacci sequence are 1. Thus:

```py
def fibb(n):
  if n <= 2:
    return 1
  else:
    return fibb(n-1) + fibb(n-2)
```

Now do we believe that our code solves the simple problem? Yes, with every fiber in my body.

Now, onto step 3, is there anything we can do to solve the complex problem. No, there isn't. So we're done! Recall that we tried to solve the simple problem first, *then* solve the complex one. This is an important approach to writing recursive code. Don't try to solve the entire problem all at once, that's hard and inefficient. Break down the problem, think about how to solve the broken down problem, and execute your ideas.
</details>

#### Note: Progression Towards Base Case


* Each step should bring the function closer to the base case
* This will typically be done in the recursive step
