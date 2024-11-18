# Square Root Approximation

This repository contains three different approaches to compute the square root of a non-negative integer, `x`, and return the square root rounded down to the nearest integer. The three methods are implemented using different algorithms: a basic approach, a binary search approach, and the Newton-Raphson method for higher precision.

## Algorithms Used

### 1. Basic Approach
This method loops through integers starting from 1 and checks when the square of the integer exceeds the given number. Once found, it returns the integer before the one that exceeded the number.

### 2. Binary Search Approach
This approach optimizes the search for the square root by narrowing down the possible range using binary search. The range is halved with each iteration until the correct square root is found.

### 3. Newton-Raphson Method
The Newton-Raphson method approximates the square root by iterating using the formula:
\[
g_{n+1} = \frac{1}{2} \left( g_n + \frac{value}{g_n} \right)
\]
This method provides higher precision after a few iterations.


___
### <center>How You Code<center>