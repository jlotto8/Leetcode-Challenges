# https://leetcode.com/problems/first-unique-character-in-a-string/ 

# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
 
'''
split each email address at the @ sign so there are characters to the left of the @ sign, and characters to the right of the @ sign
remove the '.' in the characters to the left of the @ sign
when there is a '+' ignore the characters to the right (until the @ sign)
re-join the characters
add the new characters to an empty data structure set/hashmaplist
loop through the empty data structure
check for duplicates
remove duplicates
return the length of the data structure
'''

# class Solution:
def numUniqueEmails():

        emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        set_emails = set()
        for i in emails:
            final_email = ''
            email = i.split('@')
            email[0] = email[0].replace(".","")
        #email = emails.replace('.', '')
        # print(email)
            if '+' in email[0]: # syntax?
                index= email[0].index("+")
                email[0] = email[0][:index]
            final_email+=email[0]+"@"+email[1]
            set_emails.add(final_email)
        return len(set_emails)
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
numUniqueEmails()