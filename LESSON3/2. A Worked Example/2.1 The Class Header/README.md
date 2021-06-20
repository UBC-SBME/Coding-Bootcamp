## The Class Header

This is the section we have been alluding too since lesson 1, and where all that boiler plate mess and “don’t worry about this we will talk about it later” will start to make sense. Let’s make “MyPetDog” in Java. First, we must make a file called `MyPetDog.java` somewhere in our IDE. InteliJ should automatically populate this for us, and it will look something like this

```java
public class MyPetDog{
}
```

Immediately you will recognize the `public class` from the first assignment. Because Java is an object oriented language, it demands that every single file is a class, and this bit of code lets the complier know we are making a class. This is sometimes annoying, and is why we had that boiler plate in both “Hello World” and assignment 1, we had to make a class that contained a `main` method. Importantly, any class can have a `main`. If you are crazy, multiple classes in the same program can have a `main`! `main` just acts as the entry or start point for a program, so place it where it makes sense. Sometimes an obvious master class is made. Usually there is only one that ever gets instantiated in the lifetime of your program. That is a good place for main.
