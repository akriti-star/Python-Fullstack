"""Count Vowels and Consonants:
Write a program that takes a string as input. Use a for loop to iterate through the string, and use an if-else condition inside the loop to count the number of vowels and consonants. Print the counts at the end.

"""
# Take input from the user
text = input("Enter a string: ")

# Initialize counters
vowel_count = 0
consonant_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Loop through each character in the string
for char in text:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print the results
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
