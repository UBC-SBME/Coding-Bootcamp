# The MATLAB Mindset

You should enter a new mindset whenever you are faced with an assignment that asks you to complete something in MATLAB. Sure, you could approach it by creating your own algorithm with a series of for loops and conditionals that does what the assignments asks. This is a silly approach. MATLAB is a slow language. If you make huge nested for loops, your code will run slow. Your goal in MATLAB should be to commit every MATLAB programmer's favourite deadly sin: Sloth.

Be as lazy as possible in MATLAB. As mentioned, MATLAB has many libraries and packages with functions that can probably do what you want not only more elegantly than you, but faster too. How do you discover these functions? Google and the MATLAB Docs!

Lets start with an example. Say I have a matrix `A` that is `250x250` elements and I want to increment every element by one. Sure, I could do a for loop and solve it like this

```MATLAB
for i = 1:size(A,1)
    for j = 1:size(A,2)
        A(i,j) = A(i,j) + 1;
    end
end
```

And sure this will work, or I can be lazy. [Lets litterally google "matlab add 1 to every element in an array" and click on the first result](https://www.mathworks.com/matlabcentral/answers/398433-how-to-add-a-constant-to-all-the-elements-of-the-matrix)

Would you look at that, we can just do this instead:

```MATLAB
A = A + 1;
```

Not only is this really clean, but it runs lightning quick aswell.

This approach can be applied to most problems in MATLAB. Usually the process of solving this is to first google what you want to do and either click on the link to the MATLAB documentation or the mathworks answers page. Next, you find some useful function that will help. You can either just try to work with this directly after readding the documentation of the function on the MATLAB documentation, or type `help functionName` into the MATLAB console (both methods work, sometimes the console is more useful that the documentation!)

Lets do another example from a course you will likely take, BMEG 321. Say you are asked to apply a 4th order low pass butterworth filter with a cutoff of 100 Hz. This sounds absolutely crazy, and the math behind the butterworth filter is somewhat complex and has a basis in controll systems. You could implement this yourself in about 100 lines, [or you could google "matlab butterworth filter design"](https://www.mathworks.com/help/signal/ref/butter.html)

And boom, you find a page about the butterworth filter, how to use it, what inputs it requires, and how to use the output. Specifically, with a bit more googling, you will find this monumental 100 line problem become a 2 liner

```MATLAB
[a,b] = butter(4, 100, 'low');
filteredSig = filter(a,b,rawSig);
```

You should take this approach with almost every MATLAB problem you have. Be as lazy as possible.
