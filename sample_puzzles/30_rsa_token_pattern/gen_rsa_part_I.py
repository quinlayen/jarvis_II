# RSA tokens produce a sequence of pseudorandom six-digit numbers
#     that update every 60 seconds. 
# The six-digit numbers are used to help authenticate users that
#     log into systems, typically by requiring the user to supply
#     both a PIN and the six-digit number.
# On the screen, the numbers are broken into two groups of three
#     and might look something like the following:
#     * 247 456
#     * 765 294
#     * 232 543

# Interestingly, the six-digit numbers occasionally have patterns
#     such as the following:
#     * 123 321     - a palindrome if you consider all six numbers
#     * 121 454     - two mini palindromes, one in each group of three
#                     (they do not need to be identical)
#     * 123 679     - rising numbers (each subsequent number is equal to 
#                     or larger than the previous number)
#     * 654 321     - falling numbers (each subsequent number is
#                     equal to or smaller than the previous number)

# Given the values in the file rsa_token_values.txt:
# Count how many times each pattern occurs and identify the smallest and 
# largest counts (ignore count of items that don't match any category).
# For example, given the following...

#     * 123 321     palindrome
#     * 247 456     no category
#     * 765 294     no category
#     * 123 679     rising
#     * 345 543     palindrome

# largest count is 2 (palindrome) and smallest count is 1 (rising), 
#     ignore the no category samples.

from random import randint, choice 
from math import ceil
from gen_utilities import palindrome, rising_falling, generic, stitcher

NUM_LINES = 1000

with open('rsa_token_values_I.txt', 'w') as fout:
    options = ('pal', 'mini', 'rising', 'falling', 'normal')
      
    for item in range(NUM_LINES):
        category = choice(options)
        if category == 'pal':
            token = stitcher(palindrome())
        elif category == 'mini':
            token = palindrome(3) + palindrome(3)
            token = stitcher(token)
        elif category == 'rising':
            token = stitcher(rising_falling())
        elif category == 'falling':
            token = stitcher(rising_falling(rising=False))
        else:
            token = stitcher(generic())
      
        fout.write(token)