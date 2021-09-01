## Constructors

Next, we want to have a constructor to set those variables to something. In Java, the constructor is a public method with the name of the class it constructs. Importantly, it has no return statement or type, not even a `void`! Just like any other method, it can take in variables, so let’s let it take a variable for the name, age and breed. We would get something like this.

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
}
```
Here is another new piece of Java syntax, the `this` keyword. This keyword is a pretty useful bit of syntax, as it allows you to name the inputs to a methods identically to the names of the instance variables, but still differentiate between them. Let look at the line `this.name = name;`. In this line, the `this.name` is the instance variable, while the `name` after the `=` is the variable passed to the method. Think of `this` as referring to the specific object itself. If `this` is confusing, you can alternatively name the input variables differently, like below

```java
public MyPetDog(String nameToSet, String breedToSet, int ageToSet){
    name = nameToSet;
    breed = breedToSet;
    age = ageToSet;
}
```
This will work the exact same. Personally, we suggest learning to use the keyword `this` as it can help you avoid making cumbersome variables names that include the phrase `ToSet` in them.

Another thought you might have is “what if I want a constructor that only sets the name of the dog, but gives the age and breed some default value?” or even “what if I want some constructor that just sets these instant variables to some default value?” This is possible! Our programming forefathers and foremothers had this thought too! You can create multiple constructors that take in different variables, and Java will know which to use based on the variables given to the constructor!

Lets say we want a default constructor that sets our dogs name to “Fido”, breed to “golden retriever” and age to “1”. We can program that in a few ways. The obvious way is to basically copy the constructor we have but delete the input variables and just write in our defaults. It would look something like
```java
public MyPetDog(){
    name = “Fido”;
    breed = “golden retriever”;
    age = 1;
}
```
Another way is to abuse that lovely `this` keyword again! Our code would look like
```java
public MyPetDog(){
    this(“Fido”,”golden retriever”, 1);
}
```
In this sneaky trick, the `this` keyword essentially acts as a call to another constructor (in our case, the one that takes two `strings` and an `int` as input)! This is very sneaky, but it does allow you to make many constructors easily. For example, if you only want to set the age of the dog, but leave the other fields to default, you can write.
```java
public MyPetDog(int age){
    this(“Fido”,”golden retriever”, age);
}
```
To differentiate between these constructors on object declaration/instantiation, it depends on the input variables given to it. For example, `MyPetDog x = new MyPetDog(“Cas”, “cocker spaniel”, “6”);` would use the constructor that lets us set the instance variables to what we want. `MyPetDog x = new MyPetDog();` uses the default constructor we made that sets the variables to “Fido”, “golden retriever” and “1”. This is a topic called overloading, and we will cover it in more detail later, for now just know it can be used to give a method multiple forms depending on the input variables.
