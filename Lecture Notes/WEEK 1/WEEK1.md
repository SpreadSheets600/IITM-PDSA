## 📖 Quick Summary

**Key Takeaways** :

- Python is a versatile, high-level programming language with clear syntax and extensive libraries
- Key features include easy readability, dynamic typing, cross-platform compatibility, and rich ecosystem of frameworks
- Core concepts covered include basic syntax, control flow, functions, classes, and abstract data types
- Implementation of data structures like stacks demonstrates object-oriented programming principles
- Advanced topics include slicing operations, exception handling, and algorithm efficiency considerations
- Focus on code efficiency and operation counting for optimizing program performance
- Different approaches to solving problems demonstrated through GCD calculation examples

## 📒 Note

## Basics of Python

- Python is a versatile, high-level programming language that emphasizes code readability and simplicity.
- It was created by Guido van Rossum and released in 1991. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming, making it suitable for a wide range of applications.

### Key Features of Python

- **Easy to Learn**: Python's syntax is clear and resembles the English language, making it beginner-friendly.
- **Interpreted Language**: Python code is executed line by line, which simplifies debugging and enhances flexibility.
- **Dynamic Typing**: Variables in Python do not require explicit declaration; their types are determined at runtime.
- **Extensive Libraries**: Python comes with a rich set of libraries and frameworks that facilitate tasks in web development, data analysis, machine learning, automation, and more.
- **Cross-Platform Compatibility**: Python can run on various operating systems like Windows, macOS, and Linux without requiring significant changes to the code.

### Setting Up Python

To start coding in Python, you need to set up your environment:

1. **Install Python**: Download the latest version from the official Python website and follow the installation instructions for your operating system.
2. **Choose an IDE or Text Editor**: Popular choices include PyCharm, Visual Studio Code, or simple text editors like Notepad++.
3. **Run Your First Program**: Open your IDE or text editor and write your first program:
    
    ```python
    print("Hello, World!")
    
    ```
    
    Save the file with a `.py` extension and run it to see the output.
    

### Python Syntax Basics

- **Comments**: Use `#` for single-line comments. Multi-line comments can be enclosed in triple quotes (`'''` or `"""`).
- **Variables**: Variables are used to store data. They can be assigned values without declaring their type:
    
    ```python
    age = 25
    name = "Alice"
    
    ```
    
- **Data Types**: Common data types include:
    - Integers (`int`)
    - Floating-point numbers (`float`)
    - Strings (`str`)
    - Booleans (`bool`)

### Control Flow

Python provides several control flow statements that allow you to execute code conditionally or repeatedly:

- **If Statements**:
    
    ```python
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
    
    ```
    
- **Loops**:
    - **For Loop**: Iterates over a sequence (like a list or string).
        
        ```python
        for i in range(5):
            print(i)
        
        ```
        
    - **While Loop**: Repeats as long as a condition is true.
        
        ```python
        count = 0
        while count < 5:
            print(count)
            count += 1
        
        ```
        

### Functions

Functions are blocks of reusable code that perform specific tasks. They can take parameters and return values:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

```

### Classes & Objects

In Python, classes are blueprints for creating objects (instances). They encapsulate data for the object and provide methods to manipulate that data.

- **Defining a Class**:

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable

    def bark(self):
        return f"{self.name} says Woof!"

```

- **Creating an Object**:

```python
my_dog = Dog("Buddy")
print(my_dog.bark())  # Output: Buddy says Woof!

```

### ***Abstract Data Types (ADTs)

An Abstract Data Type (ADT) is a model for a data type where its behavior is defined by a set of values and operations. The implementation details are hidden from the user, allowing for abstraction.

### Example : Stack ADT

A stack is a classic example of an ADT that follows the Last-In-First-Out (LIFO) principle. It supports the following operations:

- **Push**: Add an element to the top of the stack.
- **Pop**: Remove the element from the top of the stack.
- **Peek**: Return the top element without removing it.
- **IsEmpty**: Check if the stack is empty.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())  # Output: 2
print(stack.pop())   # Output: 2
print(stack.is_empty())  # Output: False

```

### Slicing

Slicing is a powerful feature in Python that allows you to access parts of sequences like lists or strings using specified indices.

- **Syntax**:

```python
sequence[start:stop:step]

```

Where:

- `start`: The starting index (inclusive).
- `stop`: The ending index (exclusive).
- `step`: The interval between each index (optional).

### Examples of Slicing:

- **String Slicing**:

```python
s = "Hello, World!"
print(s[0:5])  # Output: Hello

```

- **List Slicing**:

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [2, 3, 4]

```

- **Using Negative Indices**:

```python
print(my_list[-3:-1])  # Output: [3, 4]

```

### Exception Handling In Python

Exception handling allows programmers to manage errors that occur during the execution of a program. This prevents crashes and improves code robustness.

- **Try and Except Block**: The most common way to handle exceptions in Python is by using the `try` and `except` blocks. Code that might raise an exception is placed inside the `try` block, while the `except` block contains code that handles the error.

```python
try:
    x = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

```

- **Else and Finally Blocks**: You can also use `else` to run code if no exceptions occur, and `finally` to run code regardless of whether an exception occurred.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

```

- **Raising Exceptions**: You can raise exceptions intentionally using the `raise` keyword.

```python
def check_positive(x):
    if x < 0:
        raise ValueError("Only positive numbers are allowed.")

check_positive(-10)  # This will raise a ValueError

```

### Data Structures and Algorithms (DSA) in Python

Python provides built-in data structures such as lists, tuples, dictionaries, and sets that are useful for implementing algorithms efficiently.

### Common Data Structures :

- **Lists**: Ordered collections that can hold mixed types.

```python
my_list = [1, "two", 3.0]

```

- **Dictionaries**: Key-value pairs for fast lookups.

```python
my_dict = {"name": "Alice", "age": 25}

```

- **Sets**: Unordered collections of unique elements.

```python
my_set = {1, 2, 3}

```

### Useful Algorithms :

Python's libraries provide many built-in algorithms for searching (like binary search), sorting (like quicksort), and more complex operations like graph traversals (BFS/DFS).

---

## **Number Of Operation Or Instruction When Program Runs**

- We need to make our code efficient, reducing the number of operations or instructions needed to complete a task.
- This helps optimize performance and resource usage, especially when dealing with large datasets.
- Understanding how many operations a program performs is crucial for analyzing its efficiency and complexity.

### 1. Computing GCD - Greatest Common Divisor

```python
def gcd(m,n):
	cf = [] # List Of Common Factors
	for i in range(1,min(m,n)+1):
		if (m%i) == 0 and (n%i) == 0:
			cf.append(i)
	return(cf[-1])
```

- **`gcd(m, n)` — greatest common divisor**
    - Largest k that divides both m and n
    - `gcd(8, 12)` = 4
    - `gcd(18, 25)` = 1
- **Also `hcf` — highest common factor**
    - `gcd(m, n)` always exists
    - 1 divides both m and n
- **Computing `gcd(m, n)`**
    - `gcd(m, n) ≤ min(m, n)`
    - Compute list of common factors from 1 to `min(m, n)`
    - Return the last such common factor

### **2. Computing `gcd` - Eliminate The List**

```python
def gcd(m,n):
	for i in range(1,min(m,n)+1):
		if (m%i) == 0 and (n%i) == 0:
			mrcf = i
	return(mrcf)
```

### 3. **Computing `gcd` - Better Way**

- Suppose d divides m and n
- let m = ad and n = bd
- then, m − n = (a − b) d
- d also divides m − n

```python
def gcd(m,n):
	(a,b) = (max(m,n), min(m,n))
	if a%b == 0:
		return(b)
	else:
		return(gcd(b,a-b))
```

### 4. **Computing `gcd` - Euclid’s algorithm**

- If n divides m then gcd(m, n) = n
- Otherwise, compute gcd(n, m mod n)

```python
def gcd(m,n):
	(a,b) = (max(m,n), min(m,n))
	if a%b == 0:
		return(b)
	else:
		return(gcd(b,a%b))
```

### **Why Efficiency ?**

- Resource Optimization: Efficient code uses fewer computational resources (CPU, memory) and runs faster.
- Scalability: As data size grows, efficient algorithms become increasingly important to maintain reasonable performance.
- Cost-Effectiveness: In cloud computing and large-scale applications, more efficient code directly translates to lower operational costs.

This makes sence when we think about : 

- Sort all Aadhaar number
- Real time Gamming Problem
- Search data from big database
