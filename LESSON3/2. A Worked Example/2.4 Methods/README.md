## Methods

Methods are very similar in syntax to the function you have written in C. Lets write that example method, `bark` we talked about earlier. This method just gets the dog to bark, so it will print something to the terminal, will not take in any variables, and will not return anything. Adding it to our code will give use something that looks like
```java
public class MyPetDog{
    public string name;
    public string breed;
    public int age;

    public MyPetDog(string name, string breed, int age){
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
}
```
Fairly simple here. If we want to return a value, we can switch that `void` to whatever type we want, and add a `return` statement. If we want to have some sort of input variable (say the number of times the dog barks) we can add that in the brackets. This is almost identical to the C code you say in APSC 160, except for that `public` key word, which we will talk about very soon!
