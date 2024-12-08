# Part 1

## Approach

After thinking about this a little bit, I'm leaning towards a "dual lookups" approach. The general idea:

- Parse the list of rules into a dictionary reference.
  - Each key is a page number
  - Its value is a set of page numbers that _must not come before it_.
- For each update, iterate through the numbers found.
  - Keep a set that tracks page numbers already encountered, adding to the set on each iteration.
  - Look the current page number up in the dictionary.
  - If there is any overlap between the set found there and the "seen" set, the update is incorrectly ordered! Return false (or move on to the next update in whatever other way you're supposed to).
- If we iterate to the end of an update without finding any correct orderings, then it's good to go:
  - find its middle page number
  - add that to a running total

# Part 2

## Approach

To correct an update, sort it based on the following comparison:

If the element at index `i` is in the rules list for the element at index `j`, then the element at index `i` should be weighted as "greater than" the element at index `j`.