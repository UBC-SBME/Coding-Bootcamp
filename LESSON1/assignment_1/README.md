# Assignment 1

## Setup
By now, you likely don't have the Java environment installed on your PC. **This is fine**, in later lessons we will show you how to install the Java runtime environment and a very good IDE (Integrated Development Environment), the IntelliJ IDEA.

For now, either create an account on [repl.it](https://replit.com/~) or simply google "online java ide" and use whichever one you would prefer. This website is an online IDE for a lot of languages.

[Watch this video](https://www.youtube.com/watch?v=iv-fJPRVBDU) to learn how to create a Java Repl.


We highly recommend that you make a GitHub account and connect to [repl.it](https://replit.com/~) using this. Your GitHub account will become very important in your software development career. Moreover, once you make a GitHub account, you can redeem your free [GitHub student pack](https://education.github.com/pack). This has lots of goodies.

## Translating C Code to Java
First, let's do a guided walkthrough with Java. You should try your best to translate this code without looking at the solution guide, and then take a look to see how you did.

The objective of this program is simple, you want the program to do the following tasks:

1. Create an n size array (Either "hard code" the array or create one using an array)
2. Create a separate function to see if number in array is even or odd
3. Iterate throughout the array
4. Have the output of the function return total count of even numbers


Here is the starter C code that you are to translate into Java.

### C code

```cpp
#include <stdio.h>
int countEvenNum(int arr[], int size);

int main()
{
   int n = 5;
   int foo[5] = { 0, 1, 2, 3, 4};

   // You can make a new size var to something a lot bigger
   int m = 100;
   int bar[100];

   for(int i = 0; i < m; i++){
       bar[i] = i;
   }


   printf("The total number of even numbers in foo are: %i\n", countEvenNum(foo, n));

   printf("The total number of even numbers in bar are: %i\n", countEvenNum(bar, m));

   return 0;
}

int countEvenNum(int arr[], int size){

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
```
