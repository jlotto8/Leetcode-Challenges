/*
1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false
 
Constraints:
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.

I: string lower-case letters
O: booleon true or false
C: lowercase english letters
E: empty string, other chars besides letters

create a dictionary  to store letters and counts of each letter
loop thru the string
    check if letter is in dict, if not add it, if yes, increase the count
check if dict has 26 keys
if  yes, return true
if no return false
*/

function isPangram(s) {

    let letter_counts = {};

    for (let char of s){
        if (/^[a-zA-Z]$/.test(char)) {
            let lowerChar = char.toLowerCase();
            if (!(lowerChar in letter_counts)) {
                letter_counts[lowerChar] = 1
            }
        }
    }
    return Object.keys(letter_counts).length >= 26;
}

console.log(isPangram("thequickbrownfoxjumpsoverthelazydo")); // Output: false
// console.log(isPangram("thequickbrownfoxjumpsoverthelazydog")); // 
// {} is llike an indent in js
// npm to share libraries
// objects are implemented using a hashtable; object doesnt need a class 
// variable declaration for let, const
// node package manager is package manager for node
