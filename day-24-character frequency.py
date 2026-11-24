
# Day 24: Character Frequency in a String

s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Character Frequency:", freq)
