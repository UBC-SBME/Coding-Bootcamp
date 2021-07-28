# Static Methods

before we jump right into the guts of this final project, lets quickly talk about static methods and their uses.

In Java, you can place the key word `static` infront of any method (you have seen this with `main()` already). What this does is make it such that the method can be called without creating an instance of a class. This means, you can group together a collection of useful utility methods into one class file, make them all static, and let every other part of your program use it without having to create an instance of that class. You can imagine this would save a lot of memory, as instead of potentially thousands of objects each having their own instance of some utility class, they can all share one.

This is used in the project in a class called `Calculator`. It has a series of methods that help you switch from an index to a coordinate on a plain. Our project's cell simulation is on a 2D grid, but the cells are stored in an ArrayList, which is 1 dimensional. The Calculator has methods that let you convert a point on the 2D grid into an index for the ArrayList, and vice versa.

[For more information, look at this handy guide.](https://www.geeksforgeeks.org/static-methods-vs-instance-methods-java/)
