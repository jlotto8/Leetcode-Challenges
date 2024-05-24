"""
748. Shortest Completing Word

Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

 
Example 1:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.

Example 2:
Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
 
Constraints:
1 <= licensePlate.length <= 7
licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
1 <= words.length <= 1000
1 <= words[i].length <= 15
words[i] consists of lower case English letters.

Idea 1

input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]

{s: 2, P:1, t:1} 
Create a dictionary to hold letters of the lic plate, and their counts/how many times they occur in lic plate 
loop through lic plate
    add each letter to dict use isalpha to ignore spaces and integers, count the letters

loop through dict
    check if key letter is in the first word in the list (make a copy of the list), use .count to check if the letter is there value amount of times
    if it is, remove the letter(s) from the word
    if it is not, stop looping and go on to the next word in the list
return the first shortest word remaining in the list of words

problems 
- looping through the dict keys will work, but I'm not clear if checking the counts will work
- removing letters when found is tricky- the counts will have to be carefully tracked

idea 2

Create a dictionary to hold letters of the lic plate, and their counts/how many times they occur in lic plate 
loop through lic plate
    add each letter to dict use isalpha to ignore spaces and integers; convert letters to lowercase with .lower(), count the letters

loop through list of words
    create a dictionary for each word
    loop through each letter in each word
        add each letter, and its count to a dictionary

        create a flag to check if the word is a completing word
        loop thru lic plate dict
            check if the key is not in the word counts dict or if the lic plate letter count < value in plate dict
                the flag is False because it is not a valid completing word
                break out of the loop to save time
        
        create a result variable to hold the shortest completing word
        create a shortest length variable to hold the len of each completing word

        if the flag is True, and the length of the word is less than the current shortest word
            reset the variable to the word

        return the word

problems

- the nested for loop has poor efficiency; need to think about this further
- there are a lot of steps- is there an easier way?

- compare dictionaries
- lic a subset of word; issubset; 
- break down into 2 functions
- consider sorting the words*
- try again with built-in method
"""
def completing_word(license_plate, words):

    license_plate_counts = {}
    for plate_char in license_plate.lower():  
        if plate_char.isalpha():  
            license_plate_counts[plate_char] = license_plate_counts.get(plate_char, 0) + 1
    
    print(f'lic plate {license_plate_counts}')


    shortest_completing_word = None  # why do these have to be initialized here, instead of right befoore they aare used in the last code block?
    shortest_length = float('inf') 

    for word in words:
        word_counts = {}

        for word_char in word:
            word_counts[word_char] = word_counts.get(word_char, 0) + 1
            
        print(f'word dict {word_counts}')

        is_completing_word = True
        for plate_char, plate_count in license_plate_counts.items():
            if plate_char not in word_counts or word_counts[plate_char] < plate_count:
                is_completing_word = False
                break
                
        if is_completing_word and len(word) < shortest_length:
            shortest_completing_word = word
            shortest_length = len(word)

    return shortest_completing_word

print(completing_word('1s3 PSt',["step","steps","stripe","stepple"] ))
