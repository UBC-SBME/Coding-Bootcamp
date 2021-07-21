An interesting quirk of inheritance is you can declare a variable of type superclass but create a new subclass. Here is an example

```java
MyPetDog x = new MyPetChihuahua(10, 3, “Killer”);
```

See, this variable `x` is of type `MyPetDog`, but the implementation is going to be `MyPetChihuahua`. This is really confusing, but basically you can use any public methods from `MyPetDog` but at runtime it will use the `MyPetChihuahua` implementation. What does that mean? Well, remember how we made `MyPetChihuahua` a `bark()` method that printed “yip”? If we type something like `x.bark()` despite `MyPetDog` having a `bark()` method that prints “woof”, it will use `MyPetChihuahua`’s `bark()` method, so it will print “yip”. Try this on your own, it's best to play around with this.

Importantly, when you use this declaration style you can ONLY use methods from` MyPetDog` and have NO direct access to methods from `MyPetChihuahua`. Remember that `bite()` method from earlier? Well if we do `x.bite()` we will get a syntax error. You can get around this by casting `x` to `MyPetChihuahua` (much like how you can cast an `double` to be an `integer`, often done in APSC 160), but this is really messy.
