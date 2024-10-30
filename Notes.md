## Python Programming Basics - Study Notes
### 1. Number Classification
#### Checking if a number is positive, negative, or neutral

```python
num = int(input("Enter a number"))
if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is neutral")
else:
    print("Number is negative")
```

### Explanation: This program helps us understand how numbers can be classified. When a user enters a number:
##### - If it's greater than 0 (like 1, 2, 3...), it's positive
##### - If it's exactly 0, it's neutral
##### - If it's less than 0 (like -1, -2, -3...), it's negative