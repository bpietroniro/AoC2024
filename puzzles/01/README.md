# Part 1

## Problem statement (abridged)

Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

```
3   4
4   3
2   5
1   3
3   9
3   3
```

In the example list above, the pairs and distances would be as follows:

- The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
- The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
- The third-smallest number in both lists is 3, so the distance between them is 0.
- The next numbers to pair up are 3 and 4, a distance of 1.
- The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
- Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?

## Approach

From the inputs, we note that:
- All the numbers are positive.
- The two lists are the same length.
- We aren't going to de-duplicate the lists; repeated numbers are still counted in the ordering.

### Input parsing

- Initialize two list data structures
- Read each line
  - For each line, strip newline and split on whitespace
  - Append the first element to the first list, and the second element to the second list
- Return the two lists

### Algorithm

1. Sort both lists
2. Initialize total distance variable
3. Iterate through indices from 0 to the length of the list
  - for each index, find the absolute value of the difference between the numbers at that index
  - add the absolute value to the total distance
4. Return the total distance


# Part 2

## Problem statement (abridged)

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

For the same example list as above, here is the process of finding the similarity score:

- The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
- The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
- The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
- The fourth number, 1, also does not appear in the right list.
- The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
- The last number, 3, appears in the right list three times; the similarity score again increases by 9.

So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?

## Approach

1. Initialize the score at 0
2. Convert the right list into a hash where each key is a number that appears in the list, and its value is the frequency of that number
3. Iterate through the left list
  - Look up the frequency of each number in the hash
  - Multiply the number by its corresponding frequency, and add the result to the running sum
4. Return the score