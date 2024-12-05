# Part 1

## Observations

From the inputs, we note that:
- All the numbers are positive.
- The two lists are the same length.
- We aren't going to de-duplicate the lists; repeated numbers are still counted in the ordering.

## Input parsing

- Initialize two list data structures
- Read each line
  - For each line, strip newline and split on whitespace
  - Append the first element to the first list, and the second element to the second list
- Return the two lists

## Algorithm

1. Sort both lists
2. Initialize total distance variable
3. Iterate through indices from 0 to the length of the list
  - for each index, find the absolute value of the difference between the numbers at that index
  - add the absolute value to the total distance
4. Return the total distance


# Part 2

## Algorithm

1. Initialize the score at 0
2. Convert the right list into a hash where each key is a number that appears in the list, and its value is the frequency of that number
3. Iterate through the left list
  - Look up the frequency of each number in the hash
  - Multiply the number by its corresponding frequency, and add the result to the running sum
4. Return the score