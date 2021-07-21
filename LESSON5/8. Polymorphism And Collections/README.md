This is where we bring in your knowledge from lessons 3, 4 and 5 all together to get a cool result. Polymorphism can be used to store many different subclasses in one collection, like an `ArrayList`

Say you have a whole bunch of classes that all inherit from `MyPetDog` (or implement the `Dog` interface), and you want to store them all in a list and make them all bark. All of these classes are different dog species, from Chihuahuas to Cocker Spaniels to Great Danes to Golden Retrievers, and each has a unique bark. This sounds hard, but with polymorphism it is possible! Here is some example code on how this would look like.

```java
ArrayList<MyPetDog> dogList = new ArrayList<MyPetDog>();
dogList.add(new MyPetChihuahua());
dogList.add(new MyPetCockerSpaniel());
dogList.add(new MyPetGreatDane());
dogList.add(new MyPetGoldRetriever());

for(MyPetDog dog : dogList){
    dog.bark();
}
```

And the output would look something like

```
Yip!
Bark!
BWOOOF!
Woof!
```

We will be sure to make use of this in the project!
