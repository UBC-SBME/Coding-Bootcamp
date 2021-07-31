# Assignment
Dr. de Boer was very impressed by the work that you did in Lesson 4, and in fact, has asked you to come back to his lab to help write some code for the same project.

This time, you are in charge of writing code to determine palindromic sequences in a genome. [Palindromic sequences](https://en.wikipedia.org/wiki/Palindromic_sequence) are sequences of DNA/RNA wherein the sequence in one direction (5' to 3') is the reverse sequence (3' to 5') in the opposite direction.

Eg)

5' - AGCT<br> 3' - TCGA




Checkout the appendix for the relevance of palindromic sequences in biomedical engineering if you are interested.

You are to write the program in a recursive manner since Dr. de Boer **hates** loops (not actually true but I am taking some creative liberties).


Here is some starter code that is supplied to you:

```java
public class Main {

  public static boolean checkPalidromicSeq(String fivePrimeToThreePrime, String threePrimeToFivePrime) {
    // Your recursive code here
  }


  public static void main(String[] args) {
   System.out.println(checkPalidromicSeq("ATGC","GCAT"));
   System.out.println(checkPalidromicSeq("GAATTC","CTTAAG"));
   System.out.println(checkPalidromicSeq("GGATCC","CCTAGG"));
 }

}

```

Here are some example input and outputs for your program:

* `checkPalidromicSeq("ATGC","TACG")`

  * `false`


* `checkPalidromicSeq("GAATTC","CTTAAG")`

  * `true`  


* `checkPalidromicSeq("GGATCC","CCTAGG")`

  * `true`  




## Hints
Please try the actual problem prior to using hints. Go to office hours or post a question on piazza before you use the hints.

<details>
  <summary>
    Hint 1
  </summary>

Think about the decomposing complexity strategy from the previous lesson. There is one self similar problem and one different problem. **You need private helper functions**.

</details>

<br>
<br>


<details>
  <summary>
    Hint 2
  </summary>

The different problem is checking to see if the two string are equal to each other.

</details>

<br>
<br>


<details>
  <summary>
    Hint 3
  </summary>

The self similar problem is reversing the string of one of the sequences.


</details>


## Deliverables

* Java file called `Main.java`

<br>
<br>
<br>
<br>
<br>

#### Appendix A: Palindromic Sequences

##### Restriction Endonucleases (Restriction Enzymes)
In genetic engineering, often times we are interested in a certain sequence of a gene. If we want to insert that part of a gene, we need to cut another part out of the plasmid. We cut that part of the plasmid using restriction enzymes. Each restriction enzyme will cut out a different sequence. Palindromic sequences will often be identified since they leave "sticky ends" which allow the desired gene sequence to be inserted nicely. Sticky ends are the ends of the cuts made by restriction enzymes, they leave an "L" like shape which will let other desired genes be inserted.

| 5' |T | || C| G| A| 3'|
| --- |---|---|---|---|---|---|---|
|3' | A| G| C| |  | T| 5'|

Stick Ends Example

##### CRISPR
Clustered Regularly Interspaced Palindromic Repeats (CRISPR) is a gene editing tool that enters a cell and cuts at specific sequence sites. CRISPR uses repeats of DNA (~20-40bp) that are palindromes. When these palindromes are translated to RNA, they form hairpin turns which provide recognition sites for enzymes.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/DNA_palindrome.svg/1200px-DNA_palindrome.svg.png)

Notice how the sequences in the middle are a palindromic sequences:

5' --- GATC <br> 3' --- CTAG

CRISPR Takes advantage of this, the cas9 protein actually has nucleases where it cuts the DNA sequence. The recognition site of where the DNA cuts will depend on the guide RNA (gRNA) that the cas9 protein holds.

Obviously, this is a bit of an oversimplification but hopefully helps you understand the relevance of palindromic repeats in biomedical engineering.
