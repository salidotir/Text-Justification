# Text-Justification -> Split text into "good" lines
Algorithm implemented using dynamic programming

In order to have a more readable text, we should use some way of alignment. It will make out text more readable and more beautiful.

### Description:
we should define a factor of neatness in our texts.
If a given line contains words i, i+1, ..., j each with length li and we leave exactly one space between words, the number of extra spaces at the end of the line is: 
* M - (j - i +  #no._of_spaces)
* we wish to minimize the squae of the above sum in whole lines.

***Factor of badness in this algorithm is the above sum to power of 2.***

### reference:
- https://www.youtube.com/watch?v=ENyox7kNKeY&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=21&t=1978s
- https://www.youtube.com/watch?v=RORuwHiblPc
- https://www.geeksforgeeks.org/word-wrap-problem-dp-19/
