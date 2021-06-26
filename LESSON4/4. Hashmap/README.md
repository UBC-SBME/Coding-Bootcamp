# HashMap

## Mapping
You can think of a `Map` like a dictionary, every "word" has a corresponding definition. The definition of the word *depends* on the word itself rather than its location in the dictionary. `Map` has a set of keys that correspond to a set of values. Each key has a value, and you can not have two values for the same key.

Another good analogy for this type of data structure is the definition of a mathematical function. Every input has **exactly** one output. Logically, this also makes sense as if you trying to find a value using a key, then having several values per key will create chaos as you can't be sure which value is the one you want. You are used to a numbered key set (starting at zero) that correspond to objects; this is what most arrays are.

| Key | Value|
| --- | --- |
| 0 | "Dog" |
| 1 | "Cat" |
| 2 | "Bird" |

The documentation for `Map` specifically states:
> An object that maps keys to values. A map cannot contain duplicate keys; each key can map to at most one value.

Another example of key-value paired `Map` could be:

| Key | Value|
| --- | --- |
| oncoGene0 | VEGF |
| oncoGene1 | BRCA1 |
| oncoGene2 | AKT2 |
| oncoGene3 | RAS |


## Enter HashMap
`HashMap` will quickly become your best friend in CPEN221 and your software development career. `HashMap` is an implementation of `Map` in Java, it uses key-value pairs to create a dictionary-like data structure. It becomes especially useful whenever we want to sort a list of values according to some metric (alphabetical, based on a score, etc).   

The biggest advantages of `HashMap` are:
* Custom key-value pair list of objects

* Can add key-value pair dynamically

* Allows sorting of a list using a custom sort type (alphabetical, grade, etc)

Here are some examples of you can initialize a `HashMap` variable:
* `HashMap<String, String> dict = new HashMap<String, String>()`

* `HashMap<MyPetDog, DNA> dogToDNA = new HashMap<MyPetDog, DNA>()`


### Motivating Example
`TODO: Key-value pair of BMEG student to grades`

## Assignment
Go to any one of the following resources and begin learning how to use `HashMap`.

1. [Codeacademy: HashMaps in Java](https://www.codecademy.com/courses/java-for-programmers/articles/hashmaps-java-for-programmers)
  * Read the full article
  * Implement the code examples in IntelliJ IDEA (**Do not copy and paste**)
  * No account needed


2. [W3 Schools: Java HashMap](https://www.w3schools.com/java/java_hashmap.asp)
  * Write and test all the code in IntelliJ IDEA
  * Click the "Try it Yourself" and play with the code
  * No account needed


3. [Alex Lee: HashMap Java Tutorial](https://www.youtube.com/watch?v=70qy6_gw1Hc)
  * Watch the full video
  * Follow along with tutorial in IntelliJ IDEA
