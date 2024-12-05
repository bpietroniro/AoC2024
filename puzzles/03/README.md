# Part 1

## Problem statement (abridged)

In the following string containing multiplication instructions interspersed with nonsense,

`xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`,

the only the valid `mul` instructions are:
- mul(2,4)
- mul(5,5)
- mul(11,8)
- mul(8,5)

Adding up the result of each instruction produces 161 $(2*4 + 5*5 + 11*8 + 8*5).$

Scan the input for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

## Approach

This is looking pretty regex-y to me.

The matcher will be something like:
```re
/mul\(\d{1,3}\,\d{1,3}/
```

So, we find all the instances of that.

Then for each instance:
1. Strip off anything that's not a digit from both ends
2. Split what remains by the comma
3. Convert the two resulting elements to ints and multiply them
4. Add the product to a running total

Then return the total.


# Part 2

## Problem statement (abridged)

There are two new instructions you'll need to handle:

The `do()` instruction enables future mul instructions.
The `don't()` instruction disables future mul instructions.
Only the most recent `do()` or `don't()` instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

`xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`

This is similar to the example from before, but this time the `mul(5,5)` and `mul(11,8)` instructions are disabled because there is a `don't()` instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a `do()` instruction.

This time, the sum of the results is $48$ $(2*4 + 8*5)$.

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?

## Approach

Okay, so we should add to the matcher to make it pick up the do's and don't's as well.

We'll keep them all in the same array in the order they're found. Then, when we iterate through the array:
1. Set a variable to keep track of "enabled" state; initialize it to True
2. If a `mul` instruction is encountered, check whether enabled is true. If it is, perform the calculation and add to the total; if not, don't.
3. If a `do` instruction is encountered, set enabled to true.
4. If a `don't` instruction is encountered, set enabled to false.