# What You Implement

You need to implement the following files: `Cell.java`, `CancerCell.java`, `DeadCell.java`, `ImmuneCell.java`, and `TissueCell.java`. To start, you can copy and paste the contents of these files you already made for assignments 3 and 5.

The next step is to finally implement `interactNeighbors`. Lets discuss.

## `interactNeighbors`

This is a method each class has, and it governs how it interacts with the simulation. This method returns nothing, but is given an ArrayList of Cells called neighbors. Despite the name, this ArrayList actually contains every single cell in the simulation. Additionally, this is the List used by the simulation, so any modification to it will be rendered in the next frame. Despite this containing every cell in the simulation, our method will only ever interact with the cells immediately adjacent to it. This does give you freedom to implement wacky cell interactions that account for the entire board, if you want!

Every implementation of `interactNeighbors` will first poll the neighbourhood for the number of cells of each type, and their location. How would you do this? Can you use the methods from `Calculator` to help? For an exact definition of neighbourhood, see the page Overarching Project in the Introduction module.

Lets talk about the exact specification of `interactNeighbors` for each specialized cell type. All of these have say "it will choose one of it's neighbors of cell type X". How you implement each's cell strategy to choose is up to you. We recomend randomly to start.

### `DeadCell`

This cell is dead. It does nothing.

### `TissueCell`

This cell checks its neighbourhood for any `DeadCell`s. If any exist, there is a 70% chance it will pick one and "grow" into it, and a 30% chance nothing happens. "Growing" just means replacing it with a new `TissueCell` at the same coordinates.

If there are no `DeadCell`s as neighbors, then nothing happens.


### `ImmuneCell`

This cell checks its neighbourhood for any `CancerCell`s. If any exist, it will choose one and "kill" it, by replacing it with a new `DeadCell` at the same location.

OPTIONAL ADDITION: If you want to make your cell more powerful, try to program the ability for it to "kill" multiple `CancerCell`s in one time step. Do this by having there be a 50% chance after every attack the cell could attack again, killing another cancer cell.

If there are no `CancerCell`s as neighbors, nothing happens.

### `CancerCell`

The most complex cell is essentially a `TissueCell` and `ImmuneCell` at the same time. First, a `CancerCell` checks its neighbors. It counts the number of `DeadCell`s, `ImmuneCell`s and `TissueCell`s around itself, and then takes on of the 3 following actions.

If there are ANY `DeadCell`s, the `CancerCell` will grow into one of them. Just like `TissueCell` it does this by replacing the `DeadCell` with a new `CancerCell`. Importantly, it does not have the randomness of tissue cells. If it can grow, it will.

Otherwise, if there are more `TissueCell`s than `ImmuneCell`s AND atleast 1 `TissueCell` in the `CancerCell`'s neighborhood, it will choose one of the neighboring `TissueCell`s and kill it by replacing it with a new `DeadCell`.

Otherwise, if there are any number of `ImmuneCell`s, it will pick on and fight it. `CancerCell` combat works slightly different here. Remember how each cell has a `strength` integer? Well, this now comes into play. When a `CancerCell` attacks an `ImmuneCell`, it will lower the `ImmuneCell`'s strength by 1. If the `ImmuneCell`'s strength is lowered to 0, it dies and is replaced by a new `DeadCell`, otherwise it keeps fighting.

## Implementation Tips
1. Each cell has to catalogue it's neighbors and choose one. It might be a good idea to store the neighbors location in a list for use later. What can the size of that list tell you about the number of a specific neighbor cell type?
2. Since `CancerCell` is essentially a combo of `ImmuneCell` and `TissueCell`, implementation order can lessen the workload on other cell types. If you implement `ImmuneCell` and `TissueCell` First, then `CancerCell`'s implementation will mostly be copy paste.
3. Test after each cell is implemented! Do this by running `main()` and modifying the cell distribution in `initialize()`. For example, if you have only implemented `TissueCell` try modifying `initialize` such that the board is 95% `DeadCell`s and 5% `TissueCells` You would expect to see the `TissueCells` grow rapidly and cover the board!


Goodluck!
