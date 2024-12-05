# Part 1

## Observations

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

Edge cases include pretty much any time the offending interval is between the first and second level in the report.

...after a bunch of this kind of thinking and plenty of fussy little workarounds, decided to resign myself to brute force, essentially:

### Algorithm

1. If it's just plain safe, return True.
2. If it's safe when you chop off the first or last level, return True.
3. If it's safe if you splice out any other single level, return True.

I still want a more efficient solution, but don't have time for it right now.