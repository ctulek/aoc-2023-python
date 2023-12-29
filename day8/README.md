# Notes
I couldn't figure out the second part on my own. I had a good excuse, though.
I had a hunch that it should be related to finding the periods for each start node.
However, I had the following questions that discouraged me from going that way:
* You may have many periods for different Z nodes. How do you decide which period to choose?
* The periods may end up with the instructions in different positions, then with five starting nodes;
how do you align the instructions and periods?

The answers to those questions were in the structure of the puzzle input. However, I didn't find that myself.
I have relied on [a YouTube video](https://youtu.be/_nnxLcrwO_U).
* The first Z node you find also becomes the period of which you choose from A to Z because:
  * When you calculate the next period, you end up with the first Z node. So, the pattern is A -> Z1 -> Z1 -> ...
  * The second period is equal to the first period. So, A -> Z1 is equal to Z1 -> Z1.
* The periods are all multiples of the length of the instructions. So you don't need to worry about the alignments.

Hence, the step count is the Least Common Multiple of all the periods.

I think part 2 of day 8 was hard to find without playing with data, and even then, you may need to be lucky to see
that pattern.
