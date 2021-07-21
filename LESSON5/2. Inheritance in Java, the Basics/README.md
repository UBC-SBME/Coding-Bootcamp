For inheriting from a class in Java, we use the `extends` keyword. Let's try that with `MyPetChihuahua`. If you want to follow along, try creating this class in the same folder as `MyPetDog`!

Let's start with the class definition. It is essentially the same as any other class, but we need to let the compiler know we are inheriting from `MyPetDog`, so we would type the following.

```java
public class MyPetChihuahua extends MyPetDog{
}
```

And if we leave it like that we are done! `MyPetChihuahua` will function identically to `MyPetDog`. This is boring though, so let’s change stuff and talk about the nuances of inheritance.
