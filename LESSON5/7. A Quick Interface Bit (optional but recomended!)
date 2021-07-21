Sometimes you want to use polymorphism but you don’t want to program a base class to inherit from. That is where an interface comes in. An interface contains all the method declarations a class needs to implement. For example, a `Dog` interface may have something that looks like this.

```java
public interface Dog{
    /** Comment about what this method should do */
    public void bark();
}
```

You will notice that it contains a method declaration for bark, but no implementation. That is the user's job. They can then go about writing out their own class that implements the interface as follows

```java
public class MyPetDog implements Dog{
    public void bark(){
        System.out.println(“Woof”);
    }
}
```

And just like with the polymorphism from the previous section, you can use polymorphism with the interface.

```java
Dog x = new MyPetDog();
```

Just like before, only methods declared in the interface can be accessed. This is sometimes useful when you have a series of classes that all need to implement similar methods, but have vastly different ways to implement them.

You already know 3 interfaces. Map, List, and Set are all interfaces. `HashMap`, `ArrayList`, and `HashSet` are implementations of that interface. `LinkedList` is another implementation of the List. It holds data in a fundamentally different way compared to the `ArrayList`, so it shares little implementation with it. This also means you can make your own Map, List and Set in Java and plop it into your programs easily! [For more reading, look at this article](https://www.w3schools.com/java/java_interface.asp)

Interfaces are used in CPEN 221/223 in the mini projects to force you to implement some class in the way the rest of the program expects. It is useful to learn about them now.
