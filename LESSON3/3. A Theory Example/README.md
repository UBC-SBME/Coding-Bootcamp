# Another Example Object
To emphasize how objects can talk to eachother, lets think of creating a graphical user interface (GUI) with object oriented programming. We will not be programming this, as GUIs are a rabbit hole all to their own, and Java Library for it (JavaFX) is a pain to get working

Let’s make a simple GUI for a grocery list. All it needs to do is display a list of groceries we want to buy, their price, how many we want to buy, and have a button that lets us add more groceries to the list.

Our first class we would create would be something like `GrocceryListGUI`. This is where we would have our `main` method, and it would act as the master of this program. One of its instance variables could be the desired resolution the user wants the GUI to be. Another, more interesting instance variable could be a `button` object. That is right, objects can be instance variables as well! You can imagine that this `button` object would be the add item button I talked about in the prompt. It could have instance variables that specify the coordinates of the button on the GUI, and a public method `isPressed()` which can tell `GrocceryListGUI` if the button is pressed. With that info, the `GrocceryListGUI` could then add the item to the list. Speaking of list, another instance variable object for our `GrocceryListGUI` could be the list itself. This list could then have an instance variable for each `GrocceryItem`, which would have instance variables for name, price, and amount to buy, each with their own getters and setters that prevent mischievous users from setting nefarious values for each variable.

You can really see how object-oriented programming really becomes its own with this hierarchy of object relations, and modularity. This grocery list program in the end would just be tens of objects all communicating with eachother! You can imagine how this promotes collaboration, as multiple programmers can work on different parts of this program at the same time. For example, if you give the specifications of the `GrocceryItem` class to a friend, they can program that while you program the list class, under the assumption that your friend implements their class to the rigorous specs you gave them.