# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.
word=input("Pick a word:")
for i in (word):
    print(i)
    
vowel="aeiouAEIOU"
count=0
for i in word:
    if i in vowel:
        count+=1

print(f"Your word has {i} vowels.")
# Challenge:
# Count how many vowels are in the word.
