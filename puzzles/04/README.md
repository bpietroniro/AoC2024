# Part 1

## Approach

Since we need to find all occurrences of `XMAS`, this brings backtracking to mind.

A naive (non-pruned) approach that finds all possible strings that can be made from 4 adjacent letters in the grid, then counts how many of those spell `XMAS`.
If I had more time, I might do that first, before optimizing by pruning it down. However, life is short.

### Input parsing

First off, we need to get the input in a usable form (a 2D array).
1. Initialize an empty array of string arrays
2. Read input line by line
3. Split each line by whitespace, and add the result to the array
4. Return the array

### Method
#### Stuff that each next move depends on:
- length of the current candidate string (stop when it reaches 4)
- which direction we're going in, in terms of both dx and dy
  - north: dx = 0, dy = 1
  - northeast: dx = 1, dy = 1
  - east: dx = 1, dy = 0
  - southeast: dx = 1, dy = -1
  - south: dx = 0, dy = -1
  - southwest: dx = -1, dy = -1
  - west: dx = -1, dy = 0
  - northwest: dx = -1, dy = 1
- whether we're out of bounds of the grid (i.e. the grid itself is a dependency)

#### Possible helper functions:
- check whether a given position is out of bounds
- check whether the next letter is what we want, depending on what the letter is and what index we're at (0-3)

#### Outline
Starting conditions:
  - i = 0
  - j = 0
  - result = []
  - current_string = ''

Beginning at (0,0), iterate through each row. Whenever an `X` is encountered, begin a new search process in each direction starting from that `X`.

Cut the search process short if we're out of bounds or if the newly encountered letter is not the one we're looking for (depending on the current `index`).

Increment the total count if we've reached index 3 and found an `S` (this means we've found `XMAS`), and return (no need to continue the search in that direction).

If we made it this far in the function call, it's time to continue the search recursively in the same direction.

# Part 2

Ha, okay, this seems easier. Basically we're looking for all the `A`s in the puzzle that meet a certain condition: they need to have

(`M` to the northwest and `S` to the southeast) \
OR \
(`S` to the northwest and `M` to the southeast) 

AND

(`M` to the northeast and `S` to the southwest) \
OR \
(`S` to the northeast and `M` to the southwest).

I think this part should be as simple as going through and checking every `A` in the grid for this condition?