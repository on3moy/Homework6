"""
This site https://www.whitehouse.gov/briefings-statements/remarks-president-trump-state-union-address-3/  has the Remarks by President Trump in State of the Union Address. Please copy the text between “9:06 P.M. EST” to “10:24 P.M. EST” and create a “summary.txt” file with the following statistics:

-	Total word count
-	Total character count
-	The average word length
-	The average sentence length
-	A word distribution of all words ending in “ly”
-	A list of top 10 longest words.

The file should be similar to – the numbers are wrong, just for illustration:


Total word count: 34093 
Total character count: 2030303
The average word length: 7
The average sentence length: 10

A word distribution of all words ending in “ly”
highly: 2
totally: 1
…

A list of top 10 longest words in descending order:
Substantially, opportunities, ,,,
"""

import os

REMARKS_FILE = 'remarks.txt'
OUTPUT_FILE = 'summary.txt'
READ_MODE = 'r'
WRITE_MODE = 'w'
ENCODING = 'utf-8'

if os.path.isfile(REMARKS_FILE):
    # Read File
    FREQUENCY = {}
    TOTAL_CHARACTER = 0
    LINES = 0
    with open(REMARKS_FILE,READ_MODE, encoding=ENCODING) as file:
        # Read each line from text
        for line in file:
            LINES += 1
            content = line.rstrip('\n').split()
            
            # Get Total Amount of Characters
            for _ in line:
                TOTAL_CHARACTER += 1

            # Remove all other characters besides alphabet
            for words in content:
                word = ''
                for letter in words:
                    letter = letter.lower()
                    if letter in [chr(x) for x in range(ord('a'),ord('z')+1)]:
                        word += letter
                if word not in FREQUENCY:
                    FREQUENCY[word] = 1
                else:
                    FREQUENCY[word] += 1

            # Count total word character count excluding special characters
            TOTAL_WORD_CHAR = 0
            for word in FREQUENCY:
                TOTAL_WORD_CHAR += len(word)

            # Create a list of all words ending in ly
            LY_LIST = []
            for word, count in FREQUENCY.items():
                if 'ly' in word:
                    LY_LIST += [[word, count]]
    # Write results to summary.txt
    with open(OUTPUT_FILE, WRITE_MODE) as output:
        output.write(f'Total word count: {sum(FREQUENCY.values()):,}\n')
        output.write(f'Total character count: {TOTAL_CHARACTER:,}\n')
        output.write(f'The average word length: {TOTAL_WORD_CHAR/sum(FREQUENCY.values()):.2f}\n')
        output.write(f'The avereage sentence length: {TOTAL_CHARACTER/LINES:.2f}\n')
        
        # print ly distribution list
        output.write('\nA word distribution of all words ending in "ly":\n')
        for word in LY_LIST:
            output.write(f'{word[0]}: {word[1]}\n')

        # Top ten longest words
        output.write(f'\nA list of top 10 longest words in descending order\n')
        LETTER_COUNT = {x: len(x) for x in FREQUENCY}
        LONGEST_WORDS = sorted(LETTER_COUNT.items(), key=lambda x : x[1], reverse=True)
        TOP_10 = 0
        for word in LONGEST_WORDS:
            TOP_10 += 1
            output.write(f'{word[0]}\n')
            if TOP_10 == 10:
                break
        
else:
    print(f'\n{REMARKS_FILE} is not found in {os.getcwd()}!!!\n')