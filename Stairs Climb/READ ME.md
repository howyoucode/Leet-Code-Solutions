# Number Climb Problem

This repository explores the **Number Climb** problem, a common exercise in algorithmic thinking.

---

## Problem Statement

You are climbing a staircase that requires `n` steps to reach the top. Each time you climb, you can either:

- Take **1 step**, or
- Take **2 steps**.

The task is to determine the **total number of distinct ways** to climb to the top.

---

## Examples

### Example 1:
- **Input:** `n = 2`
- **Output:** `2`
- **Explanation:** 
  1. Climb 1 step + 1 step.
  2. Climb 2 steps.

### Example 2:
- **Input:** `n = 3`
- **Output:** `3`
- **Explanation:**
  1. Climb 1 step + 1 step + 1 step.
  2. Climb 1 step + 2 steps.
  3. Climb 2 steps + 1 step.

---

## Approach

The problem can be solved using:
1. **Recursion:** A straightforward but inefficient approach due to overlapping subproblems.
2. **Dynamic Programming:** An efficient way to calculate the number of ways by storing results of smaller subproblems.

---

## Applications

This problem is a variation of the **Fibonacci sequence** and finds applications in:
- Path counting problems.
- Game theory and decision-making.
- Dynamic programming exercises.

---

## Contribution

Contributions to enhance the solution and add optimized approaches are welcome. Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the [MIT License](LICENSE).
