# Increment Large Integer by One

## Problem Description
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zeros.

The task is to increment the large integer by one and return the resulting array of digits.

### Example:
#### Input:
```
digits = [1, 2, 3]
```
#### Output
```
[1, 2, 4]
```

# Explanation:
The integer represented by the array is 123. After incrementing it by `1`, the number becomes `124`, which is returned as the result `[1, 2, 4]`.

Edge Case:
If the number ends with several 9's, like `[9, 9, 9]`, the result should be `[1, 0, 0, 0]`, because adding 1 to 999 results in 1000.

## Constraints:
- The input integer is non-negative and does not have leading zeros.
- The array is ordered from the most significant digit to the least significant digit.
- The array can represent integers up to a very large value (i.e., numbers with many digits).

## Approach
Start from the least significant digit: Begin iterating from the rightmost digit of the array.
Handle carry-over: If the digit is less than 9, increment it and return the array. If the digit is 9, set it to 0 and carry over 1 to the next more significant digit.
Final carry: If all digits are 9 (like `[9, 9, 9]`), the result will require an additional digit at the beginning (e.g., `999` becomes `1000`).

## Time Complexity:
- Time Complexity: `O(n)`, where `n` is the number of digits. We may need to process every digit in the worst-case scenario.
- Space Complexity: `O(1)`, since the input array is modified in place.


# Code Implementation
```Pyhton
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits
```

## Contributing
Feel free to fork the repository and submit a pull request. Contributions are welcome!


### <center> - How You Code</center>
