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
| 11 | Strings | [Valid Anagram](strings/valid_anagram.py) | Character counts, fail fast on negative | O(n) | O(k) |
| 12 | Strings | [Group Anagrams](strings/group_anagrams.py) | Bucket by sorted-letters key | O(n·k log k) | O(n·k) |
| 13 | Strings | [Longest Common Prefix](strings/longest_common_prefix.py) | Shorten the first word until all match | O(S) | O(1) |
| 14 | Strings | [Valid Parentheses](strings/valid_parentheses.py) | Stack of open brackets | O(n) | O(n) |
| 15 | Strings | [Reverse Words in a String](strings/reverse_words.py) | Split on whitespace, reverse, join | O(n) | O(n) |
| 16 | Strings | [Is Subsequence](strings/is_subsequence.py) | Two pointers across the longer string | O(n) | O(1) |
| 17 | Hashing | [Subarray Sum Equals K](hashing/subarray_sum_equals_k.py) | Prefix sums with a count map | O(n) | O(n) |
| 18 | Hashing | [Longest Consecutive Sequence](hashing/longest_consecutive_sequence.py) | Set, count only from run starts | O(n) | O(n) |
| 19 | Hashing | [Top K Frequent Elements](hashing/top_k_frequent.py) | Count, then bucket by frequency | O(n) | O(n) |
| 20 | Hashing | [Isomorphic Strings](hashing/isomorphic_strings.py) | Two maps, one per direction | O(n) | O(k) |
| 21 | Hashing | [Contains Duplicate II](hashing/contains_duplicate_within_k.py) | Last-seen index per value | O(n) | O(n) |
| 22 | Hashing | [4Sum II](hashing/four_sum_count.py) | Meet in the middle: count pair sums | O(n²) | O(n²) |
