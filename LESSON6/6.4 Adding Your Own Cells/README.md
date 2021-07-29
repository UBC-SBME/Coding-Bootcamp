# Adding Your Own Cells

As mentioned, you can add your own cells to this simulation if you want. Here is the list of requirements to get that working.

1. MUST EXTEND `Cell`, just like the other cells in this simulation
2. Must have an implementation of `interactNeighbors`. `Cell` does have a default implementation that does nothing, so I guess if you want another cell that does nothing go for it.
3. Must have an `id` between 0 and 9 inclusive, prefferably unique compared to other cell types. This id can change if you want a cell to flash between several colors, though epileptics be ware. Cell id determines color on the screen. See `Pixel.java` for a list of colors. If you set an id less than 0 or greater than 9 you will get an array index out of bounds exception.

And that is it! Go to town and make your cool cells.
