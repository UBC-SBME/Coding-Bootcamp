# Assignment 1 Solution Guide
## Translating C Code to Java

### Step 1: What to first write

Our first step in developing the translated program is writing the initial code for the Java compiler to even recognize it as code. If you don't know what compilers are, or need a refresher, go ahead and look it up (This will be a common theme). For each language its different, and if you don’t know this, just Google: “Java Hello world program” or replace Java with whatever language you are learning

You might be asking yourself: Why do I need to write all this? For now, let's just say *don’t worry about* it, this will all make more sense later. If you already have an existing Java file from another class, feel free to use the main function from that. But, for now all you need to know is that all java programs follow this structure.:

```java
class Main {
 public static void main(String[] args) {
   // Your awesome code here
 }
}
```

There are 3 reminders that we want to mention here:
1. The class name
  * It has to be the exact name as your java file, so if your file is called `BootCampCode.java` then you have to write `class BootCampCode`
  * It is typically Java convention to capitalize the words in the class name
    * Ex. NeuronCell, HeartCell, Cell, etc
2. The function output of main
  * You may remember from APSC 160 that we usually write `int main(){...}`, where the `int` refers to the function output type. However in Java, the output is `void` (meaning no output)

3. The function input of main
  * In C you will also note that `main()` takes nothing for an input but in Java, main takes `String[] args` as an input. **Don’t worry about this**. For now you can accept  that we have to do this
    * Side note: If you are interested about the `String[] args`, this tells java to accept an array of strings with variable name `args`. This will act as input to the entire program, which is occasionally useful. However, this variable name can be whatever. For example, it can even be: “`String[] bootCamp`” or “`String[] awesomeCode`”


### Step 2: Creating the initial arrays
Just like with the first step, if you don’t know how to do something, **just google it**. The internet is full of an abundance of resources, so take advantage of it. Our first step is creating an array in Java. So, just google “How to create an array in Java” and click on the [first link](https://www.w3schools.com/java/java_arrays.asp). Now we can start writing code!

**Note:** Using other people's code is a large part of programming, in fact, people build libraries of code for others to use. However, it is important that you credit the code that you are using. Blindly copy and pasting code without crediting the rightful author is academic misconduct.

```java
class Main {
 public static void main(String[] args) {
   int[] foo = {0, 1, 2, 3, 4};
 }
}
```

We can do the same with a for loop and create an array using that! However, you’ll notice you need an extra piece of syntax. You will need to do

```c
int[] bar = new int[100]
```

We will talk more about this in a later lesson about Classes, but for now think of this as explicitly creating a **new** array.

```java
class Main {
 public static void main(String[] args) {
   int[] foo = {0, 1, 2, 3, 4};

   int[] bar = new int[100];
   for(int i = 0; i < 100; i++){
       bar[i] = i;
   }
 }
```

### Step 3: Declaring a new function
We want to declare a new function called countEvenNum. You can guess that we're also going to google this. Thus, you can create a new function just like this:

```java
class Main {
 public static void main(String[] args) {
   int[] foo = {0, 1, 2, 3, 4};

   int[] bar = new int[100];
   for(int i = 0; i < 100; i++){
       bar[i] = i;
   }
 }

 public static int countEvenNum(int[] arr, int size){
   // Your awesomer code here
   return 0;
 }
}
```

Again, the mysterious public and static keywords appear. For now, treat them as a necessary evil we will learn more about in future lessons. You should notice that other then the mystery keywords, the function declaration is very similar to the style found in C.


### Step 4: For loop and if statement
By now, you should be able to google what you want to do and be able to use that code as reference. You should get something like this as your final product.

```java
public static int countEvenNum(int[] arr, int size){
  int count = 0;

  for(int i = 0; i < size; i++){

    if(arr[i] % 2 == 0){
      count++;
    }

    else {
        /* This else statement doesn't need to be here
           but we included it so you know how to write
           complete if-else statements */
    }
  }
  return count;
}
}
```
Again, this should look almost identical to the for loops and if statements you have made in C. Lucky for us, the original Java developers took some inspiration from C when creating the language, so there is a lot of familiar syntax!


### Step 5: Wait, how do you print in Java!?
Printing in java will look incredibly convoluted at first, you will have to type things that don’t make sense. But, again, we will come back to this. For now, just assume you have to do this.

This is how you write a print statement in Java:

```java
// For strings
System.out.println("Hello");

// For integers
System.out.println(420);

// You can also call functions directly in the print statement, effectively // printing whatever is returned
System.out.println(countEvenNum(arr, size));
```

Thus, we can finish writing the code by adding a few print statements and calling the function that we want to.

```java
class Main {
 public static void main(String[] args) {
   int[] foo = {0, 1, 2, 3, 4};

   int[] bar = new int[100];
   for(int i = 0; i < 100; i++){
       bar[i] = i;
   }
 System.out.println("The number of even numbers in foo is:");
 System.out.println(countEvenNum(foo, 5));

 System.out.println("The number of even numbers in bar is:");
 System.out.println(countEvenNum(bar, 100));

 }



  private static int countEvenNum(int[] arr, int size){
   int count = 0;

   for(int i = 0; i < size; i++){
     if(arr[i] % 2 == 0){
       count++;
     }
     else{

     }
   }

   return count;
 }
}
```

Running this program should give you almost identical results to the C code!


#### YOUR ASSIGNMENT FOR THIS LESSON:
Take what you have learned in this lesson and translate the C code to your language of choice, and upload to Canvas. It can be any language, but we personally recommend Python or MATLAB as they are well documented and have some interesting features compared to C and Java. It would be a good exercise to note some of the difference between your chosen language and C / Java! Additionally, both have browser based tools to program in them (replit has python built in, MATLAB has an online version as well). Good luck, and have fun!
