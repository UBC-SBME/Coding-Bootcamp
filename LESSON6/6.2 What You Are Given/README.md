# What You Are Given In the Final Project

We wanted to leave a good poriton of the code up to you, but there is some part that is just tedious to code and doesn't offer much to learn. 

## `Util`

The `Util` package contains some utilities you may find useful. The previously mentioned `Calculator` class is there, but there is also a class called `Pair`. This is a basic class that just stores two integers that act as an x and y position on a plain. This was sadly needed as you can not return 2 pieces of data in Java. You can check `Pair.java` and `Calculator.java` for method specifications that tell you how to use them.


## `Rendering`

This is a set of files that handles displaying the simulation in a window. `Pixel.java` is a useful class as it shows you what colours your cell will be. Basically, the cell ID determines the colour. You'll notice we have more colours than cell ids. This is intentional. If you want to implement your own cells with their own rules you have some extra colours you can use to destinguish them with. There is a soft limit of 10 different cells.

Additionally, in `Program.java` there are varibles that can be changed to set the size of the simulation. You mess with this if you want a larger or smaller sim. Additioannly, you can set the frame rate here by messing with the `FRAME_TIME` instance variable at the top of the file.

## `Simulation`

This is the package where you will implement your cells. There is one extra file in here called `Logic.java`. This class initializes the cell distribution on the 2D grid, will call the `interactNeighbors` method for each cell, and will let the program know what colour each cell should be (return each cell's cell id). If you want to mess with the amount of each cell type generated at the start of your simulation, or generate new cell types you add on your own, you can edit the method `initialize()`
