# Cell Simulation and Automata

You are a  researcher at the School of Biomedical Engineering (SBME) and are currently helping a clinical team at Vancouver General Hospital simulate cellular interactions between various cell types. You want to be able to help clinicians better understand the complex nature of cell interactions and ultimately aid them in making more informed medical decisions.

The goal of this project is to:
* Help illustrate the need for object-oriented programming in a biomedical context

* Implement various object-oriented programming paradigms

* Create a software project and contribute to building your CV/ software portfolio

* Understand the relevancy and methodology of translating clinical requirements into your project


## Background

### What is Cellular Automata?
In this project, you are going to create a cellular automaton. A cellular automaton is a model of a system of objects; basically, an automaton simulates the interactions between objects based on a set of rules. Most automata have the following features:
* The objects are embedded in an array (typically a 2D grid)
* The object itself has a certain state (typically 0/off or 1/on)
* Each object in the array has an adjacent neighbour object

Let (x,y) denote the coordinates of the central position. The entire table is an example of a neighbourhood for (x,y).


|(x-1,y-1) | (x,y-1)| (x+1, y-1) |
|:---: |:---: |:---: |
| (x-1,y)| (x,y)| (x+1,y)|
| (x-1,y+1)| (x,y+1)| (x+1,y+1)|

A popular example of cellular automata can be the [Game of Life by John Conway](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). In Conway's Game of Life, he defines a set of **simple** rules for simulating the natural world. Conway was able to show that incredible complexity can be born out of general guidelines. Much like Conway's Game of Life, we can also simulate a biological system using our knowledge of cell systems and their known behaviour.

An example of Conway's Game of Life in action:

![](https://cdn-images-1.medium.com/fit/t/1600/480/1*2c5Mfwq7mu0xajlLCmsCDQ.gif)

### Why is this relevant to us?
Being able to understand the cellular level interactions of different cell types can play an important role in guiding therapeutics or even giving insight into diagnostic solutions. There are several active areas of research on this front.

For example, the image below is from a research paper that aims to simulate the dynamics of HIV-1 between HIV cells and white blood cells (lymphocytes). The paper can be found [here.](https://www.researchgate.net/profile/Monamorn-Precharattana/publication/283799493_Stochastic_modeling_for_dynamics_of_HIV-1_infection_using_cellular_automata_A_review/links/5a98cc1a45851535bce0dade/Stochastic-modeling-for-dynamics-of-HIV-1-infection-using-cellular-automata-A-review.pdf)

<p align="center"><img width="80%" height="auto" src="https://op.mahidol.ac.th/ra/wp-content/uploads/2019/08/IL_2562-02-02.jpg"> <br><i>Stochastic Cellular Automata Model for HIV -1 Infection Dyanimics <a src="https://op.mahidol.ac.th/ra/en/2019/10/24/il_2562-02-2/">(Precharattana, 2019)</a></i></p></p>

There are several very interesting areas of research that rely on some sort of simulation, such areas include:
* Whole-Cell Modeling and Simulation
  * [A Brief Survey](https://link.springer.com/article/10.1007/s00354-019-00066-y#Abs1)

* Tumour Growth Simulation
  * [A Novel Method for Simulating Cancer Growth](https://link.springer.com/chapter/10.1007/978-3-642-15979-4_15)

* Tissue Growth Simulation
  * [Tissue growth for 3D printed Scaffolds](https://link.springer.com/article/10.1007/s10237-018-1040-9)

## Your Project

Your project will be to use cellular automata to create a simulation of cancer cells vs. human cells. Specifically, your simulation will have 4 types of cells

### `ImmuneCell`

This cell fights cancer. Specifically, it will check arround its neighbourhood for `CancerCells`, pick one, and kill it, replacing it with a `DeadCell`

### `TissueCell`

The `TissueCell` exists to grow. All it does is check its neighbourhood for `DeadCell`. If one exists, it will "grow" a new `tissueCell` by replacing the `DeadCell` with a `TissueCell`

### `DeadCell`

This simple cell does nothing, and is only there to be interacted with by other cell types.

### `CancerCell`

The most complex cell, as it does does what both immune and tissue cells do! Specifically, a `CancerCell` will look at its neighbourhood and count the number of dead, tissue and immune cells around it, while also storing their location (it will have a seperate list for dead cell, tissue cell, and immune cell locations). It will then chose one of 4 actions depending on its local enviroment. If there are any number of dead cells, the cancer will choose one a "grow" into it, replacing it with a new `CancerCell`. If the number of tissue cells is greater than the number of immune cells, it will choose one and kill it, replacing it with a `DeadCell`. If the number of immune cells is greater than the number of tissue cells, it will attack an immune cell, potentially killing it. If the cancer cell is entirely surrounded by cancer cells then it will do nothing.

This may sound complex, but we will build up to this through the weeks by completing the following tasks:

## Tasks
Each task can be found in more details in the respective lesson project assignment.


### Task 1: Make a Cell Class
Make a cell type class. Specifics of what methods and instance variables this class needs are in Assignment 3

### Task 2: Characteristics of Your Cell Type
Implement a Java object in your cell type object type, this way you can introduce some characteristics of your cell type

You can define characteristics in any way that you think is appropriate to your cell type. This means you can declare properties that are pertinent to the cell type using java.util objects or have a method that uses java.util objects. Again, the main goal is to use and implement one of the main java objects.


### Task 3: Inheritance Using Your Cell Type
Create a sub-class of your cell type class (the one you made in Task 2). Specifically, after lesson 5 where you learn about inheritance, you can now make sub-classes of your cell class that are more specific. For example, you can make a `TissueCell` class! See Assignment 4 for more details.

### Task 4: Finishing Touches
Using polymorphism, finish your overarching project by implementing the logic of the simulation.
