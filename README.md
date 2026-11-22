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
| 23 | Hashing | [Intersection of Two Arrays II](hashing/intersect_two_arrays.py) | Count the shorter array, spend counts | O(n + m) | O(min(n, m)) |
| 24 | Hashing | [Contiguous Array](hashing/contiguous_array.py) | Running balance, first index per balance | O(n) | O(n) |
| 25 | Two pointers | [Squares of a Sorted Array](two_pointers/sorted_squares.py) | Fill from the back, larger absolute end first | O(n) | O(n) |
| 26 | Two pointers | [3Sum](two_pointers/three_sum.py) | Sort, fix one, sweep two pointers, skip duplicates | O(n²) | O(1) |
| 27 | Two pointers | [Two Sum II (sorted input)](two_pointers/two_sum_sorted.py) | Pointers from both ends, move the side that fixes the sum | O(n) | O(1) |
| 28 | Two pointers | [3Sum Closest](two_pointers/three_sum_closest.py) | Sort, fix one, sweep two pointers, track the best sum | O(n²) | O(1) |
| 29 | Two pointers | [Remove Duplicates from Sorted Array](two_pointers/remove_duplicates_sorted.py) | Slow write pointer, fast read pointer, copy on change | O(n) | O(1) |
| 30 | Two pointers | [Trapping Rain Water](two_pointers/trapping_rain_water.py) | Move the lower wall inward; its water level is already decided | O(n) | O(1) |
| 31 | Two pointers | [Container With Most Water](two_pointers/container_with_most_water.py) | Start widest, move the shorter wall inward | O(n) | O(1) |
| 32 | Two pointers | [Sort Colors](two_pointers/sort_colors.py) | Three regions with low, mid and high pointers (Dutch flag) | O(n) | O(1) |
| 33 | Sliding window | [Maximum Average Subarray I](sliding_window/max_average_subarray.py) | Fixed window: add the entering element, drop the leaving one | O(n) | O(1) |
| 34 | Sliding window | [Minimum Size Subarray Sum](sliding_window/min_size_subarray_sum.py) | Grow right until the sum reaches target, shrink left while it still does | O(n) | O(1) |
| 35 | Sliding window | [Best Time to Buy and Sell Stock](sliding_window/best_time_to_buy_sell_stock.py) | One pass tracking the lowest price so far; best sale is today minus that low | O(n) | O(1) |
| 36 | Sliding window | [Longest Substring Without Repeating Characters](sliding_window/longest_substring_no_repeat.py) | Variable window; on a repeat inside it, jump left past the earlier index | O(n) | O(k) |
| 37 | Sliding window | [Max Consecutive Ones III](sliding_window/max_consecutive_ones.py) | Window holding at most k zeros; shrink from the left when it holds more | O(n) | O(1) |
| 38 | Sliding window | [Minimum Window Substring](sliding_window/minimum_window_substring.py) | Grow until all needed characters are covered, then shrink while still covered | O(n) | O(k) |
| 39 | Sliding window | [Contains Duplicate II](sliding_window/contains_duplicate_ii.py) | Fixed window of the last k values in a set; drop the oldest as it slides | O(n) | O(k) |
| 40 | Sliding window | [Longest Repeating Character Replacement](sliding_window/longest_repeating_replacement.py) | Window valid while length minus its most frequent letter count is at most k | O(n) | O(1) |
| 41 | Stack / queue | [Valid Parentheses](stack_queue/valid_parentheses.py) | Stack of openers; each closer must match the top | O(n) | O(n) |
| 42 | Stack / queue | [Daily Temperatures](stack_queue/daily_temperatures.py) | Monotonic stack of days still waiting for a warmer one | O(n) | O(n) |
| 43 | Stack / queue | [Queue using Stacks](stack_queue/queue_using_stacks.py) | Inbox and outbox stacks; refill the outbox only when it is empty | O(1) amortised | O(n) |
| 44 | Stack / queue | [Evaluate Reverse Polish Notation](stack_queue/eval_rpn.py) | Operand stack; an operator pops right then left and pushes the result | O(n) | O(n) |
| 45 | Stack / queue | [Min Stack](stack_queue/min_stack.py) | Parallel stack of running minima, one entry per push | O(1) | O(n) |
| 46 | Stack / queue | [Largest Rectangle in Histogram](stack_queue/largest_rectangle_histogram.py) | Increasing-height stack; popping a bar fixes the widest rectangle it can anchor | O(n) | O(n) |
| 47 | Stack / queue | [Stack using Queues](stack_queue/stack_using_queues.py) | One queue; after each push rotate older items behind the new one | O(n) push, O(1) pop | O(n) |
| 48 | Stack / queue | [Next Greater Element II](stack_queue/next_greater_element_ii.py) | Monotonic stack over the array scanned twice to handle the wrap-around | O(n) | O(n) |
| 49 | Linked list | [Reverse Linked List](linked_list/reverse_list.py) | Re-point each node at its predecessor while saving the next node first | O(n) | O(1) |
| 50 | Linked list | [Remove Nth Node From End](linked_list/remove_nth_from_end.py) | Two pointers n apart with a dummy head; the gap locates the node before the target | O(n) | O(1) |
| 51 | Linked list | [Merge Two Sorted Lists](linked_list/merge_two_sorted_lists.py) | Dummy head and tail pointer; attach the smaller front node, then the leftover list | O(m + n) | O(1) |
| 52 | Linked list | [Linked List Cycle II](linked_list/linked_list_cycle_ii.py) | Floyd's tortoise and hare, then restart one pointer from the head to reach the entrance | O(n) | O(1) |
| 53 | Linked list | [Palindrome Linked List](linked_list/palindrome_linked_list.py) | Slow/fast pointers to the middle, reverse the second half, compare, then restore | O(n) | O(1) |
| 54 | Linked list | [Add Two Numbers](linked_list/add_two_numbers.py) | Digit-by-digit addition with a carry; loop while either list or the carry remains | O(max(m, n)) | O(1) |
| 55 | Linked list | [Middle of the Linked List](linked_list/middle_of_linked_list.py) | Slow and fast pointers; slow is at the middle when fast reaches the end | O(n) | O(1) |
| 56 | Linked list | [Reorder List](linked_list/reorder_list.py) | Find the middle, reverse the second half, then interleave the halves in place | O(n) | O(1) |
| 57 | Binary search | [Search Insert Position](binary_search/search_insert_position.py) | Leftmost index with value >= target using a half-open range | O(log n) | O(1) |
| 58 | Binary search | [Search in Rotated Sorted Array](binary_search/search_rotated_sorted_array.py) | At each step one half is sorted; keep the half that can contain the target | O(log n) | O(1) |
| 59 | Binary search | [Sqrt(x)](binary_search/integer_square_root.py) | Binary search for the largest r with r*r <= x over [1, x // 2]; exact integers, no floats | O(log x) | O(1) |
| 60 | Binary search | [First and Last Position](binary_search/first_last_position.py) | Two binary searches (first index >= target, first index > target); the target occupies the range between | O(log n) | O(1) |
| 61 | Binary search | [Find Minimum in Rotated Sorted Array](binary_search/find_min_rotated.py) | Compare mid with hi to discard the sorted half and converge on the inflection point | O(log n) | O(1) |
| 62 | Binary search | [Find Peak Element](binary_search/find_peak_element.py) | Follow the upward slope (nums[mid] < nums[mid+1]) to guarantee encountering a local maximum | O(log n) | O(1) |
| 63 | Binary search | [Single Element in a Sorted Array](binary_search/single_non_duplicate.py) | Binary search on even indices; a broken pair means the single element is at or before mid | O(log n) | O(1) |
| 64 | Binary search | [Median of Two Sorted Arrays](binary_search/median_two_sorted_arrays.py) | Binary search the partition of the shorter array so each side holds half the combined length | O(log(min(m, n))) | O(1) |
| 65 | Binary search | [Square Root with k Decimal Places](binary_search/sqrt_precision.py) | Binary search over scaled integers so truncation never involves a float comparison | O(log(x * 10^k)) | O(1) |
| 66 | Binary search | [Split Array Largest Sum](binary_search/split_array_largest_sum.py) | Binary search the answer itself; a greedy O(n) scan checks whether a candidate cap needs at most k pieces | O(n log(sum(nums))) | O(1) |
| 67 | Trees | [Validate Binary Search Tree](trees/validate_bst.py) | Recurse with inherited (low, high) bounds, not just a local parent/child check | O(n) | O(h) |
| 68 | Trees | [Lowest Common Ancestor of a Binary Tree](trees/lowest_common_ancestor.py) | Post-order recursion; a node is the LCA once p and q are found in different subtrees of it | O(n) | O(h) |
| 69 | Trees | [Zigzag Level Order Traversal](trees/level_order.py) | Plain BFS by level; reverse every other level's list in place | O(n) | O(n) |
| 70 | Trees | [Serialize and Deserialize Binary Tree](trees/serialize_deserialize.py) | Pre-order traversal with a '#' marker for missing children, rebuilt by consuming the same sequence recursively | O(n) | O(n) |
