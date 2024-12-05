# Part 1

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

## Approach

Okay, so we should add to the matcher to make it pick up the do's and don't's as well.

We'll keep them all in the same array in the order they're found. Then, when we iterate through the array:
1. Set a variable to keep track of "enabled" state; initialize it to True
2. If a `mul` instruction is encountered, check whether enabled is true. If it is, perform the calculation and add to the total; if not, don't.
3. If a `do` instruction is encountered, set enabled to true.
4. If a `don't` instruction is encountered, set enabled to false.