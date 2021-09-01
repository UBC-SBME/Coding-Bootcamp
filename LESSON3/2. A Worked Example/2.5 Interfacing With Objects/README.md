## But How do get Objects to Run Methods and Tell Us the Variables?

Object oriented programing is based in the idea of “noun.verb” where the noun is the object and verb is the action. This translates to java as `Object.action`. The best way to explain this is through an example, so lets add a main to our object so we can play around with it (good time to copy paste the code below into your IDE or replit to play around!)

```java
public class MyPetDog{
    public String name;
    public String breed;
    public int age;

    public MyPetDog(String name, String breed, int age){
        this.name = name;
        this.breed = breed;
        this.age = age;
    }
    public MyPetDog(){
        this(“Fido”,”golden retriever”, 1);
    }

    public void bark(){
        System.out.println(“woof”);
    }
    public static void main(String[] args){
        MyPetDog Cas = new MyPetDog(“Cas”,”cockerspaniel”,6);
        System.out.println(Cas.age);
        Cas.bark();
    }
}
```
Running this code should print out a `6` and a `woof` into the console. In Java, to talk to an object, you use a period. To run a method you do `Object.method(input variables)`. You can see that in the code above, where we call the `bark()` method by typing `Cas.bark()`. It is important to note this we MUST call methods from OBJECTS, not classes. If we attempted to type MyPetDog.bark() we would get an error. This is just the same as attempting to do something like `System.out.println(int)`. What `int` are we printing here? No `int`, if we instead did
```java
int x = 0;
System.out.println(x);
```
We would print 0, as x is a specific instantiated integer.

For accessing instance variables, it is much the same, except we have no `()` as it is not a method, it is a piece of data. You can see that `Cas.age` in the print statement. We are running up to Cas, and screaming “TELL ME WHAT YOUR AGE IS?” and Cas responds “6”.

You secretly have been using this already every single time you print with `System.out.println()`. What is interesting about this is there are two periods! That means that from the `system` object you grab an instance variable that is an object called `out` and then you call the method `println()` that is part of the `out` object. This is an extremely cool part of Java and other object oriented languages! You can do this noun verb as much as you want. If you had some crazy hierarchy, you could reasonably do something like `Object1.Object2.Object3.Object4.Object5.method()`, though at that point it might be messy, and would probably be better to format your code such that you can do `Object1.method1()` and let `method1()` handle the whole `Object2.Object3.Object4.Object5.method()` mess.

Importantly, this form of running methods and checking variables is only possible if we have the `public` keyword in front of it! If an external class (say a class that represents the owner) attempted to call `Cas.age` if we had `private int age` in `MyPetDog` instead of `public int age` we would get a compilation error! Yes, this is finally the part when we talk about public and private.
