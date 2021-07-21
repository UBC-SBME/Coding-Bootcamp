# ArrayList

## The Problem with Array Sizes
In APSC 160 we learned that one can create arrays by declaring the size and then filling each element in the array. However, some of you might have already noticed that this quickly becomes annoying. You might have even thought "What if we don't know the size of the array?". Excellent question! Many clever computer scientists have also found this problem irritating, thus they have developed data structures that help solve this.

 The basic idea is that every element in the array points to another element in the same array. So if we want to extend the array, we have the last element of the array point to the new element.

|  0 |  1 | 2 | 3 |
|---|---|---|---|
| Points to 1  | Points to 2  | Points to 3  | Points to nothing  |

If you want to add a new element, then:

|  0 |  1 | 2 | 3 | -> | 4|
|---|---|---|---| --- | --- |
| Points to 1  | Points to 2  | Points to 3  | Points to 4  | -> | Points to nothing|


## Enter ArrayList
Traditionally, whenever we have worked with arrays in Java, they have always been a fixed size that we can't change. But to create **dynamic** and **mutable** arrays, we can use Java's `ArrayList`.

The biggest advantages of using an `ArrayList` are:
* Elements are ordered and having indices

* Add objects to the `ArrayList`

* Remove objects to the `ArrayList`

* Have **Duplicates** of objects in the `ArrayList`

The biggest difference between `ArrayList` and other data objects in Java is that `ArrayList` **allow duplicates**. This is very important and should become something that you exploit in your code.

### Motivating Example

One potential use of an arraylist is storing data that can have duplicates. For example, say you want to store the first name of every BMEG student. This will surely have duplicates (there is probably more than one John or Peter in BMEG), so it would make sense to store this in an array list. The duplicates are helpful here, as you can determine the most common name in BMEG

### Note
Whenever you are introduced to a new data class, you should always investigate its Java documentation to get a better understanding of how you can use it. Know how to use your tools before actually using them. Thus, take a look at the [ArrayList doc](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html).

Something that you will notice is this new bit of syntax, the <b>`<E>`</b>. The `<E>` is the **type parameter**. This just the data **type** of the `ArrayList`. For example, this could be `Integer`, `String`, or even `MyPetDog` (from Lesson 3). The `<E>` just tells Java what type the objects in the ArrayList are (ArrayList of Integers, ArrayList of Strings, etc).

#### Examples
* `ArrayList<String> arrLst = new ArrayList<String>();`

*  `ArrayList<MyPetDog> arrLst = new ArrayList<MyPetDog>();`

* `ArrayList<DNA> arrLst = new ArrayList<DNA>();`


## Assignment
Go to any one of the following resources and begin learning how to use `ArrayList`.

1. [Codeacademy: Intro to ArrayList](https://www.codecademy.com/courses/learn-java/lessons/learn-java-arraylists/exercises/introduction)
  * Do all 9 sub-lessons
  * Need Codeacademy account (or sign in with GitHub, Google, etc)
  * Built-in compiler


2. [W3 Schools: Java ArrayList](https://www.w3schools.com/java/java_arraylist.asp)
  * Write and test all the code in IntelliJ IDEA (**Do not copy and paste**)
  * Click the "Try it Yourself" and play with the code
  * No account needed

3. [edureka! : Java ArrayList Tutorial](https://youtu.be/gmm7062i-tI?t=117)
  * Follow along with video and implement examples in IntelliJ IDEA
  * No account
