# Day 24 – Character Frequency in a String

## Description
This Python program counts the frequency of each character in a given string using a dictionary.

## Concepts Used
- Python Strings
- Dictionaries
- For Loop
- `get()` Method
- User Input
- Dictionary Updating

## Program
```python
s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Character Frequency:", freq)
```

## Sample Output
```text
Enter string: hello
Character Frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

## What I Learned
- How to use dictionaries in Python.
- How to count character occurrences.
- How to use the dictionary `get()` method.
- How to work with strings and loops.

## Day 24 Completed Successfully! 🚀

#Python #PythonProgramming #100DaysOfCode #Day24 #Coding #LearningPython