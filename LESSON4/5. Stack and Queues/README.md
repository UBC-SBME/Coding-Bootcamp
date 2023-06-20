# Stacks and Queues

These two are slightly more niche than the previous 3 data structures. If this is too confusing, feel free to skip this section. Nonetheless, they are useful and would be "good to know"

Another potentially useful data structure is the Stack and the Queue. Much like the ArrayList, stacks and queues are a list that can store an arbitrary number of items and duplicates. What makes them different is how you interface with these items. Essentially, you can only look at and remove the item at the "front" of a stack or queue.

## What are LIFO and FIFO

Last In First Out (LIFO) and First In First Out (FIFO) are the operating procedure for the stack and queue respectively. For a stack, the most recent item (or LAST added item) you add to it is the only item that can be interacted with or removed. For a queue, the first item added to it is the only item that can interact with or be removed.

Think of a stack as a literal stack of plates on a table. You can only reasonably look at the top plate, and have to remove it from the stack to look at the next one (assume you are very weak and can not lift more than one plate at a time).

Think of a queue as a line of people waiting to get into a ride at an amusement park. You can only talk to the person at the front of the line (the first person to get there), and once they are on the ride (removed from the queue) you can talk to the next

Why would you use this over a list? Sometimes the constrained interface method helps remove some algorithmic burden from the programmer. Basically, if your application requires you to know the order an item was placed in a list, instead of manually tracking that a queue or stack can do that for you.
