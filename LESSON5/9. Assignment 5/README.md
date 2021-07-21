# ASSIGNMENT 5

This assignment will require you to create 4 new classes that all inherit from the `cell` class you have made previously.

### `ImmuneCell`

This cell represents an immune cell. Its job is to fight `CancerCell`s. Here is what you need to implement

* This class MUST extend Cell
* A constructor that takes in `int x` and `int y`, which acts as the x and y coordinates of the cell, and then calls the constructor of the `Cell`, with the input variables of `id = 4`, `strength = 3`, and the x and y coords given.
* An override of the `interactNeighbors` method that, for now, is empty. You will implement this in the next lesson
