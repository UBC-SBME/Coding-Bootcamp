# HashSet

## Mathematical Sets and Programming Sets
Some of you might be familiar with Sets in a mathematical context; sets in math are defined as a collection of unique and distinct terms. Terms can be anything, numbers, variables, words, and so on. This idea of Sets has been used in programming as well, a set in programming is a *list* of **unique** element. They are a fundamental skill in both math and programming, many problems that you will encounter can easily be solved using the idea of sets.

Another feature of Sets are subsets, which is a sub-collection of a unique element from a parent set. For example, suppose you have a set `A` which is defined as `{1,2,3,4}`; A subset of `A` could be `{2,4}` or `{1,3}`.

## Enter HashSet
`HashSet` is an implementation of a Set; the word "Hash" comes from the idea of a hash code which is a unique code for an object.

We would use a `HashSet` whenever we want a list of elements with **no duplicates**. This becomes very important in some problems where you want to iterate through a collection and want to know some sort of categorical information about the collection, refer to Motivating Example to get a better example.

The biggest advantages of `HashSet` are:
* A `HashSet` can store `null` as a value (just because it can does not mean it should)

* A `HashSet` is very quick in adding, getting, and removing elemnets (faster than `ArrayList`)

* **No duplicates** in a `HashSet`


The `HashSet` class is another data class from the `java.utils` package, just like `ArrayList`. However, there are two big differences between `HashSet` and `ArrayList`:
* **No duplicates allowd in HashSet**


* **HashSet has no order**
  * This means that you can not index a `HashSet`
  * Ex) Suppose you have a set: `HashSet<String> strSet = new HashSet<String>()`
  * You can **not** do `strSet[0]`. **This is an illegal operation** (in programming).

### Motivating Examples
`TODO: List of courses that BMEG students have to take`

## Assignment
Go to any one of the following resources and begin learning how to use `HashSet`.

1. [Codeacademy: Sets Article](https://www.codecademy.com/courses/java-for-programmers/articles/sets-java-for-programmers)
  * Read full article (Ignore section on `TreeSet` and `LinkedHashSet`)
  * Write and test all code examples (**Don't copy and paste**)
  * No account needed


2. [Geeks for Geeks: Sets in Java](https://www.geeksforgeeks.org/set-in-java/)
  * Read full article
  * Write and test all code (**Don't copy and paste**)

3. [Alex Lee: Java HashSet Tutorial](https://www.youtube.com/watch?v=PeFyhRr42ac)
  * Watch full video
  * Follow along and test code in IntelliJ IDEA
