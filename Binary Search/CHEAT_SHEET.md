
#  <img src="https://github.com/user-attachments/assets/0b70acb4-2bd5-4fee-8cae-44c3b04a7052" width="25px"> Binary Search Cheat Sheet 🗺️

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)

This cheat sheet provides an overview of several binary search templates, each suited for different scenarios in algorithmic problem-solving. Binary search is a powerful technique used to efficiently locate a target value within a sorted array or to determine an appropriate insertion point for a target value. The templates discussed here cover basic binary search, handling duplicate elements, and applications in greedy problems.

## Table of Contents
- [Basic Binary Search](#basic-binary-search)
- [Binary Search with Duplicate Elements](#binary-search-with-duplicate-elements)
	- [Left-most Insertion Point](#left-most-insertion-point)
	- [Right-most Insertion Point](#right-most-insertion-point)
- [Binary Search on Sorted Data With Limited Range](#binary-search-on-sorted-data-with-limited-range)
	- [Rotated Sorted Array Search](#rotated-sorted-array-search)
- [Binary Search for Greedy Problems](#binary-search-for-greedy-problems)
	- [Finding a Minimum](#finding-a-minimum)
	- [Finding a Maximum](#finding-a-maximum)
- [Advanced Topics in Binary Search](#advanced-topics-in-binary-search)
	- [Tuning Precision in Binary Search (Floating Point Targets)](#tuning-precision-in-binary-search-floating-point-targets)
- [Applications of Binary Search](#applications-of-binary-search)
	- [Binary Search on Answers](#1-binary-search-on-answers)
	- [Peak Element Search](#2-peak-element-search)
	- [Finding Closest Element](#3-finding-closest-element)
	- [Order Agnostic Binary Search](#4-order-agnostic-binary-search)

## Basic Binary Search

### Template

```python
def fn(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            # do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # left is the insertion point
    return left
```

### Description

This is a standard binary search template used to find a target value in a sorted array. If the target is found, the function can be modified to return the index or perform a specific action. If the target is not found, the function returns the position where the target can be inserted to maintain the sorted order.

## Binary Search with Duplicate Elements

### Left-most Insertion Point

```python
def fn(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left
```

### Right-most Insertion Point

```python
def fn(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left
```

### Description

These templates are particularly useful when dealing with arrays that contain duplicate elements. The first template finds the left-most insertion point for the target, which is useful when you want to insert the target before any existing duplicates. The second template finds the right-most insertion point, ideal for inserting the target after any duplicates.

## Binary Search on Sorted Data With Limited Range

### Rotated Sorted Array Search

```python
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1  # Target not found
```

### Description

This template is ideal for finding a target within a rotated sorted array (e.g., `[4, 5, 6, 7, 0, 1, 2]`). The logic determines which half of the array is sorted and adjusts the binary search range accordingly.

## Binary Search for Greedy Problems

### Finding a Minimum

```python
def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left
```

### Finding a Maximum

```python
def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right
```

### Description

These templates are designed for problems where you need to find an optimal solution based on a greedy approach. The `check` function is problem-specific and determines whether a given condition is met. The first template is used to find the minimum value that satisfies the condition, while the second template finds the maximum value. These are particularly useful in optimization problems where you need to maximize or minimize a certain parameter.

## Advanced Topics in Binary Search

### Tuning Precision in Binary Search (Floating Point Targets)

```python
def binary_search_precision(a, b, EPS=1e-7):
    def is_valid(mid):
        # Example condition goes here
        return BOOLEAN

    left, right = a, b

    while right - left > EPS:
        mid = (left + right) / 2
        if is_valid(mid):
            right = mid
        else:
            left = mid

    return left
```

### Description

This technique is used for binary search on floating-point ranges, such as finding square roots, optimizing continuous functions, or solving equation systems. The `EPS` constant dictates the desired precision.

## Applications of Binary Search

### 1. **Binary Search on Answers**
Binary search can be applied to find optimal answers in problems where the relationship between input and output is monotonic. Examples include minimizing costs, maximizing profits, and determining boundaries.

### 2. **Peak Element Search**

```python
def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left
```

This finds a peak element in an array where the elements satisfy specific constraints (e.g., `nums[i-1] < nums[i] > nums[i+1]`).

### 3. **Finding Closest Element**

```python
def find_closest(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Compare the two closest indices
    if left >= len(nums) or (right >= 0 and abs(nums[right] - target) <= abs(nums[left] - target)):
        return right

    return left
```

### 4. **Order Agnostic Binary Search**

```python
def order_agnostic_binary_search(arr, target):
    left, right = 0, len(arr) - 1

    # Check if the array is ascending or descending
    is_ascending = arr[left] < arr[right]

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found at index mid

        if is_ascending:
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Descending order
            if arr[mid] < target:
                right = mid - 1
            else:
                left = mid + 1

    return -1  # Target not found
```

### Description

The **Order Agnostic Binary Search** is a versatile binary search algorithm that works on both ascending and descending sorted arrays. Instead of assuming the array's order, it determines it first by comparing the values at the start (`arr[0]`) and the end (`arr[-1]`) of the array.

## 📚 More Resources?

- [LeetCode Code Templates](https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723)
	- _To access this resource, you would have need to purchase [LeetCode's Data Structures and Algorithms Course](https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms)._
