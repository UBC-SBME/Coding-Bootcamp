# Project Assignment
You are a  researcher at the School of Biomedical Engineering (SBME) and are currently helping a clinical team at Vancouver General Hospital simulate cellular interactions between various cell types.

Now that you have made a cell type, you need to be able to define some its characteristics. This means defining some of the internal processes that makes a cell type function. This is where we being to translate our cell biology knowledge into the project. We want you to do this using the Java objects that you just learned about.

<p align="center">
  <img width="75%" height="auto" src="https://i.imgur.com/kMPIhE3.jpg">
  </br></br>
  <i>Image of basic eukaryotic cell (left) and prokaryotic cell (right) <a src="https://www.nature.com/scitable/topicpage/what-is-a-cell-14023083/">(Nature Education, 2014)</a></i>
</p>

## Task 2: Characteristics of Your Cell Type
You can define characteristics is any way that you think is appropriate to your cell type. This means you can declare properties that are pertinent to the cell type using java.util objects or have a method that uses java.util objects. Again, the main goal is to use and implement one of the main java objects.


Here are some suggestions that you can do:
* Within your cell type, declare an instance variable that holds various information of the cell type.
  * Use a `HashMap` to track the concentration of various chemicals, like lactate, ATP, or glucose.

    * This way, later in the project you can define a rule that says if a cell has a certain level of ATP or glucose it replicates; or likewise if a cell has too much lactate it dies!

  * Use a `HashSet` to keep track of signal molecules (this can be a simple ) your cell type interacts with.

    * That way, if your cell recognizes a certain signal, it can preform a specific action (induce a pathway, replicate itself, etc.)


* Within your cell type, you can create a private method that provides functionality
  * You can use an `ArrayList` to check all adjacent cells and determine cell behavior
    * For example, if there are too many adjacent cells (we can arbitrarily say 6), the cell itself could try to move away or even die.


Some of these examples are a gross oversimplification of the actual interactions that go on in your body, however the idea is to create a simple set of rules. **Your implementation does not need to be detailed.** Simplicity is key here.
