"""
Please use dictionary to keep the count of each letter. Read a text file named “book.txt” that may have multiple lines. Then create a “summary.txt” file that has the frequency of each letter, case-insensitive, i.e., “a” and “A” are the same letter. Each line has a record of the letter and frequency. The last line should be a summary to tell if the file has all 26 letters. A sample “summary.txt” is:

A 25
C 36
…
X 2
Z 4

It doesn’t have all letters.

Another “book.txt” may generate the “summary.txt” as the following:

A 25
B 36
…
X 2
Y 1
Z 4

It has all letters.
"""
# Assign Local Variables
BOOK_FILE = 'book.txt'
READ_MODE = 'r'
ENCODING = 'utf-8'

# Create empty lists to store letters found and count 
LETTERS = {}

# Try to open book.txt if file exists
try:
    with open(BOOK_FILE, READ_MODE, encoding=ENCODING) as content:
        for character in content:
            # Ensure each letter encountered is converted to lower case letters
            for letter in character:
                letter = letter.lower()
                # If the letter is not in list, add it only if between letters 'a' - 'z' or 97 - 122
                if letter not in LETTERS and ord(letter) >= ord('a') and ord(letter) <= ord('z'):
                    LETTERS[letter] = 1
                else:
                    if letter in LETTERS and ord(letter) >= ord('a') and ord(letter) <= ord('z'):
                        LETTERS[letter] += 1
    
    SORTED_LETTERS = sorted(LETTERS.items())
    SUMMARY_FILE = 'summary.txt'
    WRITE_MODE = 'w'
    with open(SUMMARY_FILE, WRITE_MODE) as text:
        for letter, count in SORTED_LETTERS:
            text.write(f'{letter.upper()} {count}\n')
        if len(SORTED_LETTERS) == 26:
            text.write(f'It does have all letters')
        else:
            text.write(f'It does NOT have all letters')


except FileNotFoundError:
    print(f'File {file_name} not found')
except:
    print('Different Error, go figure it out scrub')