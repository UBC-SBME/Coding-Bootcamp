Say `MyPetDog` has a method called `bark()` that prints the word “woof” to the console. This is not desirable for `MyPetChihuahua`, as Chihuahuas don’t bark, they yip. Java lets us fix this by overriding the method. Essentially, this will replace the original inherited method with a new one. The syntax looks like this.

```java
public class MyPetChihuahua extends MyPetDog{
    @Override
    public void bark(){
        System.out.println(“yip”);
    }
}
```
Now, the `@Override` is just a bit of highlighting that lets you keep track of what method is being overridden, but you don’t have to have it there! You can remove it and your code will work. We recommend you add it so you can keep track of things.

Another way to modify a method that requires less rewriting is using the `super` keyword. `super` is very similar to the `this` keyword from earlier, but it instead refers to the superclass. For example, say you want your Chihuahua to yip and then let our a bark, you could write something like this

```java
public class MyPetChihuahua extends MyPetDog{
    @Override
    public void bark(){
        System.out.println(“yip”);
        super.bark();
    }
}
```
What `super.bark()` does is call the `bark()` method from the superclass. This can be used just like the normal `object.action` syntax we use in java, calling any method or instance variable from the superclass. Importantly, it still has the same restrictions with `public` and `private`, meaning…
