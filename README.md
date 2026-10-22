# dsa-practice

Daily data structures and algorithms practice in Python: one problem a day, with the approach,
complexity and tests for every solution.

![CI](https://github.com/usmanali-hub/dsa-practice/actions/workflows/ci.yml/badge.svg)

## Run tests

```bash
pip install pytest
pytest
```

## Progress

| # | Topic | Problem | Approach | Time | Space |
|---|---|---|---|---|---|
| 1 | Arrays | [Two Sum](arrays/two_sum.py) | Hash map of seen values | O(n) | O(n) |
| 2 | Arrays | [Contains Duplicate](arrays/contains_duplicate.py) | Set with early exit | O(n) | O(n) |
| 3 | Arrays | [Best Time to Buy and Sell Stock](arrays/best_time_to_buy_sell_stock.py) | One pass, track lowest price | O(n) | O(1) |
| 4 | Arrays | [Maximum Subarray (Kadane)](arrays/maximum_subarray.py) | Extend or restart running sum | O(n) | O(1) |
| 5 | Arrays | [Move Zeroes](arrays/move_zeroes.py) | Two pointers, swap non-zeros forward | O(n) | O(1) |
| 6 | Arrays | [Product of Array Except Self](arrays/product_except_self.py) | Prefix and suffix products | O(n) | O(1) extra |
| 7 | Arrays | [Container With Most Water](arrays/container_with_most_water.py) | Two pointers, move the shorter side | O(n) | O(1) |
| 8 | Arrays | [Sort Colors](arrays/sort_colors.py) | Dutch national flag, three pointers | O(n) | O(1) |
| 9 | Strings | [Valid Palindrome](strings/valid_palindrome.py) | Two pointers, skip non-alphanumerics | O(n) | O(1) |
| 10 | Strings | [Longest Substring Without Repeating Characters](strings/longest_substring_no_repeat.py) | Sliding window with last-seen index | O(n) | O(k) |
