# ASSIGNMENT 5

This assignment will require you to create 4 new classes that all inherit from the `cell` class you have made previously.

### `ImmuneCell`

This cell represents an immune cell. Its job is to fight `CancerCell`s. Here is what you need to implement:

* This class MUST extend Cell
* A constructor that takes in `int x` and `int y`, which acts as the x and y coordinates of the cell, and then calls the constructor of the superclass, with the input variables of `id = 4`, `strength = 3`, and the x and y integer values that were passed to the `ImmuneCell` constructor as arguements. HINT: This is done in 1 line.
* An override of the `interactNeighbors` method that, for now, is empty. You will implement this in the next lesson

### `TissueCell`

This cell represents a tissue cell. It grows by replacing neighbouring `DeadCell`s with `TissueCell`s. Here is what you need to implement:

* This class MUST extend Cell
* A constructor that takes in `int x` and `int y`, which acts as the x and y coordinates of the cell, and then calls the constructor of the superclass, with the input variables of `id = 1`, `strength = 0`, and the x and y integer values that were passed to the `TissueCell` constructor as arguements. HINT: This is done in 1 line.
* An override of the `interactNeighbors` method that, for now, is empty. You will implement this in the next lesson

### `DeadCell`

This simple cell does nothing, and is only there to be interacted with by other cell types. Here is what you need to implement:

* This class MUST extend Cell
* A constructor that takes in `int x` and `int y`, which acts as the x and y coordinates of the cell, and then calls the constructor of the superclass, with the input variables of `id = 0`, `strength = 0`, and the x and y integer values that were passed to the `DeadCell` constructor as arguements. HINT: This is done in 1 line.

Seeing as your `Cell` class should have an implementation of `interactNeighbors()` that does nothing, you do not need to override this method as `DeadCell` will also do nothing. You can override it if you want, but it is not neccissary.

### `CancerCell`

A complex cell that kills its neighbors and tries to grow. Here is what you need to implement:

* This class MUST extend Cell
* A constructor that takes in `int x` and `int y`, which acts as the x and y coordinates of the cell, and then calls the constructor of the superclass, with the input variables of `id = 3`, `strength = 1`, and the x and y integer values that were passed to the `CancerCell` constructor as arguements. HINT: This is done in 1 line.
* An override of the `interactNeighbors` method that, for now, is empty. You will implement this in the next lesson

Goodluck!
