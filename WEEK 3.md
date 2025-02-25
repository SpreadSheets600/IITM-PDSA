## 📒 Notes

## Quick Sort

### Shortcomings of Merge Sort

- Merge needs to create a new list to hold the merged elements
    - No obvious way to efficiently merge two lists in place
    - Extra storage can be costly
- Inherently recursive
    - Recursive calls and returns are expensive
- Merging happens because elements in the left half need to move to the right half and vice versa
    - Consider an input of the form `[0, 2, 4, 6, 1, 3, 5, 9]`
- So, can we divide the list so that everything on the left is smaller than everything on the right?
    - No need to merge

### Divide and Conquer without Merging

- Suppose the median value of L is m
- Move all the values $\leq m$ to the left half of L
    - Right half has values $\gt m$
- Recursively, sort the left and the right halves
    - $L$ is now sorted, no merge needed
- Recurrence: $T(n) = 2T(n/2) + n$
    - Rearrange in a single pass, time $O(n)$
- So $T(n)$ is $O(n \ log \ n)$
- So, how do we find the median?
    - Sort and pick up the median
    - But wait a minute (ちょっと待って), our aim is to sort the list!
- Instead, pick some element in L -- call it a `pivot`
    - Split $L$ with respect to the pivot element

### Quick Sort - [[C.A.R. Hoare]](https://en.wikipedia.org/wiki/Tony_Hoare)

- Choose a pivot element
    - Typically, the first element in the array
- Partition $L$ into lower and upper parts with respect to the pivot
- Move the pivot between the lower and upper partition
- Recursively sort the two partitions

<b>High level view of Quick Sort</b>

- Input list `[43, 32, 22, 78, 63, 57, 91, 13]`
    - Identify pivot
    - Mark the lower elements and upper elements
- Re-arrange the elements as lower-pivot-upper
    - `[32, 22, 13, 43, 48, 63, 57, 91]`
- Recursively sort the lowest and upper partitions

### Partitioning

- Scan the list from left to right
- Four segments: Pivot, Lower, Upper, Unclassified
- Examine the first unclassified element
    - If it is larger than the pivot, extend Upper to include this element
    - If it is less than or equal to the pivot, exchange it with the first element in the Upper. This extends Lower and shift Upper by one position
- Pivot is always the first element
- Maintain the two indices (as pointers/markers) to mark the end of the Lower and Upper segments
- After partitioning, exchange the pivot with the last element of the Lower segment

```python
def quick_sort(L, l, r):  # Sort L[l:r]
  if r - l <= 1:
    return L

  pivot = L[l]
  lower = l + 1
  upper = l + 1

  for i in range(l + 1, r):
    if L[i] > pivot:  # Extend the upper segment, if the unclassified element is bigger then the pivot
      upper += 1
    else:             # Exchange the L[i] with start of the upper segment, this extends the lower segment without shifting every single element of the upper segment
      L[i], L[lower] = L[lower], L[i]
      # Now, shift both the segments
      lower += 1
      upper += 1

  # Move the pivot between lower and upper
  L[l], L[lower - 1] = L[lower - 1], L[l]
  lower -= 1

  # Recursive calls
  quick_sort(L, l, lower)
  quick_sort(L, lower + 1, upper)
  return L
```

### Summary

- Quick sort uses divide and conquer, like merge sort
- By partitioning the list carefully, we avoid a merge step
    - This allows us to sort in-place
- We can also provide an iterative implementation to avoid the cost of recursive calls
- The partitioning strategy we described is not the only one used in the literature
    - We can build the lower and upper segments from opposite ends and meet in the middle
- We need to analyze the complexity of Quick sort

## Quick Sort

- Choose a pivot element
- Partition $L$ into lower and upper segments with respect to the pivot
- Move the pivot between the lower and upper segments
- Recursively sort the two partitions

### Analysis

- Partitioning with respect to the pivot takes time $O(n)$
- If the pivot is the median
    - $T(n) = 2T(n/2) + n$
    - $T(n)$ is $O(nlogn)$
- Worst case? Pivot is maximum or minimum
    - Partitions are of size $0, n - 1$
    - $T(n) = T(n - 1) + n$
    - $T(n) = n + (n - 1) + ... + 1$
    - $T(n)$ is $O(n^2)$
- Another worst case is when the array is already sorted!
- However, the average case is $O(nlogn)$
- Sorting is a rare situation where we can compute this
    - Values do not matter, only relative positioning (order) is important
    - Analyze behavior over permutations of ${1, 2, ..., n}$
    - Each input permutation is equally likely
- Expected running time is $O(nlogn)$

### Randomization

- Any fixed choice of pivot allows us to construct worst case input
- Instead, choose pivot position randomly at each step
- Expected running time is again $O(nlogn)$

### Iterative Quick sort

- Recursive calls work on disjoint segments
    - No re-combination of results is required
- Can explicitly keep track of left and right endpoints of each segment to be sorted

### Quick Sort in practice

- In practice, quick sort is very fast
- Very often, it is the default algorithm used for in-built sort functions
    - Sorting a column in a spreadsheet
    - Library sort function in a programming language

### Summary

- The worst case complexity of quick sort is $O(n^2)$
- However, the average case is $O(nlogn)$
- Randomly choosing the pivot is a good strategy to beat the worst case inputs
- Quick sort works in-place and can be implemented iteratively
- Very fast in practice, and is often used for built-in sorting functions
    - Good example of a situation when the worst case upper bound is pessimistic

## Quick Sort Implementation

```python
import time

class TimeError(Exception):
  """A custom exception used to report error in the use of Timer class"""

class Timer:
  def __init__(self):
    self._start = 0
    self._elapsed = 0
  
  def start(self):
    if self._start is not None:
      raise TimeError('Timer is running. Use .stop()')
    
    self._start = time.perf_counter()
  
  def stop(self):
    if self._start is None:
      raise TimeError('Timer is not running. Use .start()')
    
    self._elapsed = time.perf_counter() - self._start
    self._start = None
  
  def elapsed(self):
    if self._elapsed is None:
      raise TimeError('Timer has not been run yet. Use .start()')
    
    return self._elapsed
  
  def __str__(self):
    return str(self._elapsed)
```

```python
import sys
sys.setrecursionlimit(2 ** 31 - 1)
```

```python
def quick_sort(L, l, r):
  if r - l <= 1:
    return L
  
  pivot, lower, upper = L[l], l + 1, l + 1
  
  for i in range(l + 1, r):
    if L[i] > pivot:
      upper += 1
    else:
      L[i], L[lower] = L[lower], L[i]
      lower, upper = lower + 1, upper + 1
  
  L[l], L[lower - 1] = L[lower - 1], L[l]
  lower -= 1

  quick_sort(L, l, lower)
  quick_sort(L, lower + 1, upper)

  return L
```

```python
import random
random.seed(2021)
input_lists = {}

input_lists['random'] = [random.randrange(100000000) for i in range(1000000)]
input_lists['ascending'] = [i for i in range(10000)]
input_lists['descending'] = [i for i in range(9999, -1, -1)]

t = Timer()
t.stop()
for k in input_lists.keys():
  temp_list = input_lists[k][:]
  t.start()
  quick_sort(temp_list, 0, len(temp_list))
  t.stop()
  print(k, t)
```

```python
def merge(A, B):
  m, n = len(A), len(B)
  C, i, j, k = [], 0, 0, 0

  while k < m + n:
    if i == m:
      C.extend(B[j:])
      k += n - j
    elif j == n:
      C.extend(A[i:])
      k += n - i
    elif A[i] < B[j]:
      C.append(A[i])
      i, k = i + 1, k + 1
    else:
      C.append(B[j])
      j, k = j + 1, k + 1
  
  return C
```

```python
def merge_sort(A):
  n = len(A)
  if n <= 1:
    return A
  
  L = merge_sort(A[: n // 2])
  R = merge_sort(A[n // 2:])

  return merge(L, R)
```

```python
import random
random.seed(2021)
input_lists = {}

input_lists['random'] = [random.randrange(100000000) for i in range(1000000)]
input_lists['ascending'] = [i for i in range(1000000)]
input_lists['descending'] = [i for i in range(999999, -1, -1)]

t = Timer()
t.stop()
for k in input_lists.keys():
  temp_list = input_lists[k][:]
  t.start()
  merge_sort(temp_list)
  t.stop()
  print(k, t)
```

## Concluding Remarks On Sorting Algorithms

### Stable sorting

- Often list values are tuples
    - Rows from a table, with multiple columns / attributes
    - A list of students, each student entry has a roll number, name, marks
- Suppose the students have already been sorted by their roll number
- If we now sort by name, will all students with the same name remain in sorted order with respect to roll number
- Stability of sorting is crucial in many applications
- Sorting on column B should not disturb sorting on column A
- The quick sort algorithm we implemented is not stable
    - Swapping values while partitioning can disturb existing sorted order
- Merge sort is stable, if we merge carefully
    - Do not allow elements from the right to overtake the elements on the left
    - While merging, prefer the left list while breaking ties

### Other criteria

- Minimizing data movement
    - Imagine each element is a heavy carton
    - Reduce the effort of moving values around

### Best sorting algorithm?

- Quick sort is often the algorithm of choice, despite $O(n^2)$ worst case
- Merge sort is typically used for "external" sorting
    - Database tables that are too large to store in memory all at once
    - Retrieve in parts from the disk and write back
- Other $O(nlogn)$ algorithms exist -- `heapsort`
- Sometimes hybrid strategies are used
    - use divide and conquer for large n
    - Switch to insertion sort when n becomes small (eg: $n \lt 16$)

## Difference between lists and arrays

### Sequences

- Two basic ways of sorting a sequence of values
    - Lists
    - Arrays
- What is the difference?

---

- Lists
    - Flexible length
    - Easy to modify the structure
    - Values are scattered in the memory (non-contiguous)
- Arrays
    - Fixed size
    - Allocate a contiguous block of memory
    - Supports random access

### Lists

- Typically a sequence of nodes
- Each node contains a value and points to the next node in the sequence
    - "Linked" list
    
    !https://firebasestorage.googleapis.com/v0/b/kashif-resume.appspot.com/o/linked-list.png?alt=media&token=08bb2d49-7c22-4852-b4f5-0865d7cc8084
    
- Easy to modify
    - Insertion and deletion are easy as local "plumbing"
    - Flexible size
- Need to follow links to access $A[i]$
    - Takes time $O(i)$

### Arrays

- Fixed size, declared in advance
- Allocate a contiguous block of memory
    - $n$ times the storage for a single value
- "Random" access
    - Compute offset of $A[i]$ from $A[0]$
    - Accessing $A[i]$ takes constant time, independent of $i$
- Inserting and deleting elements is expensive
    - Expanding and contracting requires moving $O(n)$ elements in the worst case

| Index | Value |
| --- | --- |
| $A[0]$ | $v_0$ |
| $A[1]$ | $v_1$ |
| . | . |
| . | . |
| . | . |
| $A[i]$ | $v_i$ |
| . | . |
| . | . |
| . | . |
| $A[n - 1]$ | $v_{n-1}$ |

### Operations

- Exchange $A[i]$ and $A[j]$
    - Constant time for arrays
    - $O(n)$ for lists
- Delete $A[i]$, insert $v$ after $A[i]$
    - Constant time for lists if we already at $A[i]$
    - $O(n)$ for arrays
- Need to keep implementation in mind when analyzing data structures
    - For instance, can we use binary search to insert in a sorted sequence?
    - Either search is slow, or insertion is slow, still $O(n)$

### Summary

- Sequences can be stored as lists or array
- Lists are flexible but accessing an element is $O(n)$
- Arrays support random access but are difficult to expand, contract
- Algorithm analysis needs to take into account the underlying implementation
- How does it work in Python?
    - Is the built-in type in Python really a "linked" list?
    - NumPy library provides arrays - are these faster than lists?

## Designing A Flexible List

```python
class Node:
  def __init__(self, v = None):
    self.value = v
    self.next = None

    return
  
  def is_empty(self):
    return self.value == None
  
  def append(self, v):
    # Recursive
    if self.is_empty():
      self.value = v
    elif self.next == None:
      self.next = Node(v)
    else:
      self.next.append(v)
    
    return
  
  def append_iter(self, v):
    # Iterative
    if self.is_empty():
      self.value = v
      return
    
    temp = self
    while temp.next != None:
      temp = temp.next
    
    temp.next = Node(v)
    return
  
  def insert(self, v):
    if self.is_empty():
      self.value = v
      return
    
    new_node = Node(v)

    self.value, new_node.value = new_node.value, self.value
    self.next, new_node.next = new_node, self.next

    return
  
  def delete(self, v):
    # Recursive
    if self.is_empty():
      return
    
    if self.value == v:
      self.value = None

      if self.next != None:
        self.value = self.next.value
        self.next = self.next.next
      
      return
    else:
      if self.next != None:
        self.next.delete(v)

        if self.next.value == None:
          self.next = None
    
    return
```

### Implementing lists in Python

- Python class `Node`
- A list of sequence of nodes
    - `self.value` is the stored value
    - `self.next` points to next node
- Empty list?
    - `self.value` is `None`
- Creating lists
    - `l1 = Node()` -- empty list
    - `l2 = Node(5)` -- singleton list
    - `l1.is_empty()` results `True`
    - `l2.is_empty()` results `False`

### Appending to a list

- Add `v` to the end of the list `l`
- If `l` is empty, update `l.value` from `None` to `v`
- If at last value, `l.next` is `None`
    - Point `next` at new node with value `v`
- Otherwise, recursively append to rest of the list
- Iterative implementation
    - If empty, replace `l.value` by `v`
    - Loop through `l.next` to end of the list
    - Add `v` at the end of the list

### Insert at the start of the list

- We want to insert `v` at the head
- Create a new node with the value `v`
- But we cannot change where the head points
- Swap the values of $v_0, v$
- Make the new node point to `head.next`
- Make `head.next` point to new node

### Delete a value `v`

- Remove the first occurrence of `v`
- Scan the list for the first `v` -- look ahead at next node
- If next node value is `v`, bypass it
- Cannot bypass the first node in the list
    - Instead, copy the second node value to head
    - Bypass second node
- Recursive implementation

## Implementation of Lists in Python

- Sequences can be stored as lists or array
- Lists are flexible but accessing an element is $O(n)$
- Arrays support random access but are difficult to expand, contract
- Algorithm analysis needs to take into account the underlying implementation
- How does it work in Python?
    - is the built-in list type in Python really a "linked" list?
    - NumPy library provides array -- are these faster than lists?

### Lists in Python

- Python lists are not implemented as flexible linked lists
- Underlying implementation maps the list to an array
    - Assign a fixed block when you create a list
    - Double the size if the list overflows the array
- Keep track of the last position of the list in the array
    - `l.append()` and `l.pop()` are constant time, amortised -- $O(1)$
    - Insertion / Deletion require time $O(n)$
- Effectively, Lists in Python behave more like an array rather than a list

### Arrays vs Lists in Python

- Arrays are useful for representing matrices
- In list notation, these are nested lists

$\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}$

`[[0, 1], [1, 0]]`
- Need to be careful when initializing a multi-dimensional list
`zero_list = [0, 0, 0]
zero_matrix = [zero_list, zero_list, zero_list]`
    
    `zero_matrix[1][1] = 1
    print(zero_matrix)`
    
- Mutability aliases different values
    - Here, we are referencing the same list zero_list 3 times, that is why changing one list changes all of them because all 3 rows refer to the same list
- Instead, use list comprehension
`zero_matrix = [[ 0 for i in range(3) ] for j in range(3) ]`

### NumPy Arrays

- The NumPy library provides arrays as a basic type
`import numpy as np
zero_matrix = np.zeros(shape=(3, 3))`
- Can create an array from any sequence type
`new_array = np.array([[0, 1], [1, 0]])`
- `arange` is the equivalent of `range` for lists
row2 = np.arange(5)
- Can operate on a matrix as a whole
    - `C = 3*A + B`
    - `C = np.matmul(A, B)`
    - Very useful for data science

### Summary

- Python lists are not implemented as flexible linked structures
- Instead, allocate an array, and double the space as needed
- Append is cheap, insert is expensive
- Arrays can be represented as multidimensional lists, but need to be careful about mutability, aliasing
- NumPy arrays are easier to use

## Implementation Of Dictionary In Python

### Dictionary

- An array / list allows access through positional indices
- A dictionary allows access through arbitrary keys
    - A collection of key-value pairs
    - Random access -- access time is the same for all they keys
- How is a dictionary implemented?

### Implementing a Dictionary

- The underlying storage is an array
    - Given an offset `i`, find `A[i]` in constant time
- Keys have to be mapped to ${0, 1, ..., n - 1}$
    - Given a key `k`, convert it to offset `i`
- Hash function
    - h:S \rightarrow X maps a set of values $S$ to a small range of integers $X = {0, 1, ..., n - 1}$
    - Typically, $|X| \ll |S|$, so there will be collisions, $h(s) = h(s'), s \neq s'$
    - A good hash function will minimize collisions
    - SHA-256 is an industry standard hashing function whose range is 256 bits
        - Used to hash large files -- avoid uploading duplicates to cloud storage
        - Also used in cryptography
        - The output of this algorithm is 256 bits (it is a large number ie. $2^{256}$)
        - An application:
            - In cloud storage systems, for example Dropbox, sometimes when we upload a large file, it will upload very fast
            - Why does that happen?
            - The reason is the system computer the SHA-256 hash and if it detects that this hash is already present, it doesn't actually upload. It simply makes a pointer saying "one more copy of this file is uploaded"

### Hash Table

- An array `A` of size $n$ combined with a hash function $h$
- $h$ maps the keys to ${0, 1, ..., n - 1}$
- Ideally, when we create an entry for key `k`, `A[h(k)]` will be unused
    - What if there is already a value at that location?
- Dealing with collisions
    - Open addressing (closed hashing)
        - Probe (examine) a sequence of alternate slots in the same way
    - Open hashing (not to be confused with open addressing)
        - Each slot in the array points to a list of values
        - Insert into the list for the given slot
- Dictionary keys in Python must be immutable
    - If the value changes, the hash also changes

### Summary

- A dictionary is implemented as a hash table
    - An array plus a hash function
- Creating a good hash function is important (and difficult too)
- Need a strategy to deal with collisions
    - Open addressing / Close hashing -- probe for free space in the array
    - Open hashing -- each slot in the hash table points to a list of key-value pairs
    - Many heuristics / optimizations possible for dealing with collisions

## Difference between Lists and Arrays (implementation)

### Setup

- Set the recursion limit to `maxint`, $2^{31} - 1$
    - This is the highest value Python allows
- Setup the `Timer` class to time executions
`import sys
sys.setrecursionlimit(2 ** 31 - 1)
import time`

```python
import time

class TimeError(Exception):
  """A custom exception used to report error in the use of Timer class"""

class Timer:
  def __init__(self):
    self._start = 0
    self._elapsed = 0
  
  def start(self):
    if self._start is not None:
      raise TimeError('Timer is running. Use .stop()')
    
    self._start = time.perf_counter()
  
  def stop(self):
    if self._start is None:
      raise TimeError('Timer is not running. Use .start()')
    
    self._elapsed = time.perf_counter() - self._start
    self._start = None
  
  def elapsed(self):
    if self._elapsed is None:
      raise TimeError('Timer has not been run yet. Use .start()')
    
    return self._elapsed
  
  def __str__(self):
    return str(self._elapsed)
```

### Python List

```python
t = Timer()
t.stop()
t.start()
l = []
for i in range(10000000):
  l.append(i)
t.stop()
print(t)
```

```python
t = Timer()
t.stop()
t.start()
l = []
for i in range(100000):
  l.insert(0, i)
t.stop()
print(t)
```

### Searching

```python
def naive_search(v, L):
  for x in L:
    if v == x:
      return True
  return False
```

```python
def binary_search_list(v, L):
  if L == []:
    return False
  
  mid = len(L) // 2
  if v == L[mid]:
    return True
  
  if v < L[mid]:
    return binary_search_list(v, L[:mid])
  else:
    return binary_search_list(v, L[mid + 1:])
```

### Naive search and Binary search with arrays (NumPy)

```python
def naive_search(v, A, l, r):
  for i in range(l, r):
    if v == A[i]:
      return True
  return False
```

```python
def binary_search_array(v, A, l, r):
  if r - l <= 0:
    return False
  
  mid = (l + r) // 2
  if v == A[mid]:
    return True
  
  if v < A[mid]:
    return binary_search_array(v, A, l, mid)
  else:
    return binary_search_array(v, A, mid + 1, r)
```

### Naive Search VS Binary Search

```python
l = list(range(0, 100000, 2))
t = Timer()
t.stop()
t.start()
for i in range(3001, 13000, 2):
  v = naive_search(i, l)
t.stop()
print()
print('Naive search', t)
t.start()
for i in range(3001, 13000, 2):
  v = binary_search_list(i, l)
t.stop()
print()
print('Binary search', t)
```

### Naive search VS Binary search on arrays

```python
import numpy as np
my_array = np.arange(0, 100000, 2)
t = Timer()
t.stop()
t.start()
for i in range(3001, 5000, 2):
  v = naive_search(i, my_array, 0, np.prod(my_array.shape))
t.stop()
print()
print('Naive search', t)
t.start()
for i in range(3001, 13000, 2):
  v = binary_search_array(i, my_array, 0, np.prod(my_array.shape))
t.stop()
print()
print('Binary search', t)
```

## Sorting

```python
def selection_sort_list(L):
  n = len(L)
  if n < 1:
    return L
  
  for i in range(n):
    min_pos = i
    for j in range(i + 1, n):
      if L[j] < L[min_pos]:
        min_pos = j
    L[i], L[min_pos] = L[min_pos], L[i]
  
  return L
```

```python
def selection_sort_array(A):
  n = np.prod(A.shape)
  if n < 1:
    return A
  
  for i in range(n):
    min_pos = i
    for j in range(i + 1, n):
      if A[j] < A[min_pos]:
        j = min_pos
    A[i], A[min_pos] = A[min_pos], A[i]
  
  return A
```

```python
import random
random.seed(2021)
input_lists = {}
input_lists['random'] = [random.randrange(100000) for i in range(100000)]
input_lists['ascending'] = [i for i in range(100000)]
input_lists['descending'] = [i for i in range(9999, -1, -1)]
t = Timer()
for k in input_lists.keys():
  temp_list = input_lists[k][:]
  t.start()
  selection_sort_list(temp_list)
  t.stop()
  print(k, t)
```

```python
import numpy as np
import random
random.seed(2021)
input_lists = {}
input_lists['random'] = np.arange(100000)
for i in range(100000):
    input_lists['random'][i] = random.randrange(100000)
input_lists['ascending'] = [i for i in range(100000)]
input_lists['descending'] = [i for i in range(9999, -1, -1)]
t = Timer()
for k in input_lists.keys():
  temp_list = input_lists[k][:]
  t.start()
  selection_sort_array(temp_list)
  t.stop()
  print(k, t)
```
