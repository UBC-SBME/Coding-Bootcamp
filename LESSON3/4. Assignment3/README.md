# Project Assignment
You are a  researcher at the School of Biomedical Engineering (SBME) and are currently helping a clinical team at Vancouver General Hospital simulate cellular interactions between various cell types.

Your first step is to create a cell type in your program. This means defining, generally, what every cell in your simulation does. The idea here is to generalize as much as possible. It's okay if there isn't a lot of functionality that your cell can do, later in the project, we will differentiate a generic cell into more specific cell types.

<p align="center">
<img width="80%" src="https://bioinformant.com/wp-content/uploads/2017/08/What-are-stem-cells-definition-FEATURE-.jpg">
</br></br>
<i>Image of stem cell differentiating into other cell types <a src="https://bioinformant.com/what-are-stem-cells/">(BioInformant, 2021)</a></i>
</p>

</br>
You are *effectively* creating a virtual stem cell. Cool right?


# Task 1: Create a cell class
Create a class for the overarching project called Cellular Automata that has:

* Private instance variables: `int cellHealth`, `String name`, and `boolean replicate`
  * Where RESTRICTION, each with their getters and setters,


* A default constructor with defaults
  * `int cellHealth = 10;`
  * `String name = "Paul"; // Change this`
  * `boolean replicate = false;`


* Another constructor that lets the user set the variables as they please (you can use your setters in the constructor, by the way!).

* Additionally, add a public method that checks to see if the cell needs to replicate.


Feel free to add more detail to your cell type that you think belongs there. Alternatively, if you are especially ambitious, you can create multipotent stem cells (more specific stem cells). For example, you can create a  **hematopoietic stem cell** or perhaps **neural stem cells**.
