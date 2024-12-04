# Part 1

## Problem statement (abridged)

Each report is a list of numbers called levels that are separated by spaces. For example:

```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

This example data contains six reports each containing five levels.

A report only counts as "safe" if both of the following are true:

- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

- `7 6 4 2 1`: Safe because the levels are all decreasing by 1 or 2.
- `1 2 7 8 9`: Unsafe because 2 7 is an increase of 5.
- `9 7 6 2 1`: Unsafe because 6 2 is a decrease of 4.
- `1 3 2 4 5`: Unsafe because 1 3 is increasing but 3 2 is decreasing.
- `8 6 4 4 1`: Unsafe because 4 4 is neither an increase or a decrease.
- `1 3 6 7 9`: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

How many reports are safe?

## Approach

The input file tells us that:
- The reports can be of different lengths (though it looks like the longest ones are around 8 levels long)
- All levels appear to be positive integers less than 100

### Input parsing
It would be fun to do this one with concurrency, at least in Go. Maybe a separate goroutine for each line.
- Read each line
- Split each line by whitespace to get a list of levels
- Either set up a thread to process the list, or push it to a list of lists (to be iterated through)

### Algorithm
A report R is safe if:

(1) For every index $i$, $1 <= i <= len(R)$, $$0 \lt R[i] - R[i-1] \leq 3,$$
or (2) For every index $i$, $1 <= i <= len(R)$, $$0 \lt R[i-1] - R[i] \leq 3.$$

We don't have to check both for each report, though. The litmus test is the comparison between R[1] and R[0].

- If $R[1] > R[0]$, check for (1);
- Else if $R[1] < R[0]$, check for (2);
- Else the report is unsafe and we can skip any following checks.

So here's what we'll do:

1. Compare the first two elements
2. Carry out the according loop (as stated above)
3. If any of the checks is false, return false
4. Otherwise at the end, return true


# Part 2

## Problem statement (abridged)

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

- `7 6 4 2 1`: Safe without removing any level.
- `1 2 7 8 9`: Unsafe regardless of which level is removed.
- `9 7 6 2 1`: Unsafe regardless of which level is removed.
- `1 3 2 4 5`: Safe by removing the second level, 3.
- `8 6 4 4 1`: Safe by removing the third level, 4.
- `1 3 6 7 9`: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

## Approach

Okay, interesting. This is making me rethink the approach to Part 1 as well.

What if, when we parse the input, instead of storing the reports themselves, we instead store a record of the distances between each level?

So for the examples above, we'd wind up with a set of distance logs:

```
[-1, -2, -2, -1]
[1, 5, 1, 1]
[-2, -1, -4, -1]
[2, -1, 2, 1]
[-2, -2, 0, -3]
[2, 3, 1, 2]
```

Here are a few more examples to illustrate other cases that might come up:
```
10 5 3 2 1 => [-5, -2, -1, -1]
8 6 11 2 1 => [-2, 5, -9, -1]
```

If we did that, we would just have to ensure (for Part 1):
- none of the distances are 0
- either all the distances are positive or all the distances are negative
- none of the distances have an absolute value of greater than 3

Then for Part 2, how would this setup help us?

Well, first let's figure out as many categories of valid "single-error" cases as we can:
- A single repeated level (i.e. a single 0 in the distance log)
  - This is an easy fix: get rid of the repeat and check whether the report is otherwise safe.
- A single increase in an otherwise decreasing report (i.e. a single positive number in the distance log)
  - To check safety, add the value of the offending level to the value of the following level, get rid of the offending level, and check the remaining levels for safety.
- A single decrease in an otherwise increasing report (i.e. a single negative number in the distance log)
  - Follow the same procedure as above.

Single-error cases where there's no salvaging it:
- Increases of more than 3 in an all-increasing report
  - UNLESS the increase is at the beginning or end!
- Decreases of more than 3 in an all-decreasing report
  - UNLESS the decrease is at the beginning or end!

Maybe a good way to do this would be to add some metadata during the Part 1 processing. We could track the index of the first error found.

EDGE CASE: The first distance is negative but the rest or positive, or vice versa. How to handle this?