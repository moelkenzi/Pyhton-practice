# Python Programming Basics - Study Notes

---

## 1. Number Classification
### Explanation:
This program classifies a number as positive, neutral, or negative based on user input.

- If the number is greater than 0 (like 1, 2, 3...), it's positive.
- If the number is exactly 0, it's neutral.
- If the number is less than 0 (like -1, -2, -3...), it's negative.

### Code:
```python
num = int(input("Enter a number: "))
if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is neutral")
else:
    print("Number is negative")
```

---

## 2. Grade Calculation System
### Explanation:
This grading system converts numerical marks into letter grades.

- 90 or above → A
- 80-89 → B
- 70-79 → C
- 60-69 → D
- Below 60 → Fail

### Code:
```python
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Your grade is A")
elif marks >= 80:
    print("Your grade is B")
elif marks >= 70:
    print("Your grade is C")
elif marks >= 60:
    print("Your grade is D")
else:
    print("Failed")
```

---

## 3. Basic Loops
### Explanation:
Loops are used to repeat actions. Here, the program counts from 1 to 10.

- `count = 1`: Sets the initial value.
- `count <= 10`: Repeats as long as count is less than or equal to 10.
- `count += 1`: Adds 1 to `count` with each loop.

### Code:
```python
count = 1
while count <= 10:
    print(count)
    count += 1
```

---

## 4. Even/Odd Number Checker
### Explanation:
This program checks if a number is even or odd using the modulus operator `%`.

- `%` is the modulus operator, which gives the remainder of a division.
- If a number divided by 2 has no remainder (`% 2 == 0`), it's even.
- If there's a remainder, it's odd.

### Code:
```python
num = int(input("Enter a random number: "))
if num % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
```

---

## 5. Age Category Classification
### Explanation:
This program categorizes individuals based on age ranges:

- 13 or younger → too young
- 14-25 → boy
- 26-50 → man
- Over 50 → adult

### Code:
```python
age = int(input("Please enter your age: "))
if age <= 13:
    print("You are too young")
elif age <= 25:
    print("You are a boy")
elif age <= 50:
    print("You are a man")
else:
    print("You are an adult")
```

---

## 6. Number Sequence Generators
### Explanation:
These two programs generate number sequences, either increasing or decreasing:

- **Increasing Sequence**: Counts up from start number to end number.
- **Decreasing Sequence**: Counts down from start number to end number.
- `+=` adds to the count, and `-=` subtracts from it.

### Code:
**Increasing Sequence:**
```python
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
while start < end:
    start += 1
    print(start)
```

**Decreasing Sequence:**
```python
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
while start >= end:
    start -= 1
    print(start)
```

---

## 7. Simple Security Check
### Explanation:
A basic security check that verifies if a user enters the correct secret code.

- Preset code is "B5B."
- If entered code matches → Access granted.
- If not → Access denied.

### Code:
```python
secret_code = "B5B"
user = input("Please enter the secret code: ")
if user == "B5B":
    print("Successfully permitted")
else:
    print("Permission Denied")
```

---

## Key Programming Concepts Learned:
1. **Input/Output**: Using `input()` to get user data and `print()` to display results.
2. **Variables**: Storing and using data.
3. **Conditional Statements**: Using `if`, `elif`, and `else` for decision making.
4. **Loops**: Using `while` for repeated actions.
5. **Operators**:
   - **Comparison**: `>`, `<`, `>=`, `<=`, `==`
   - **Mathematical**: `+`, `-`, `%`
6. **Data Types**: Working with integers, strings, and floating-point numbers.
