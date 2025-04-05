
from typing import List

# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.

def compress(chars):
    stack = []
    ans = []
    
    for i in range(len(chars)):
        if len(stack) == 0:
            stack.append(chars[i])
        elif stack[-1] == chars[i]:
            stack.append(chars[i])
        else:
            ans.append(stack[-1])
            if len(stack) > 1:
                ans.extend(list(str(len(stack))))
            stack.clear()
            stack.append(chars[i])

    # Process last character group
    if stack:
        ans.append(stack[-1])
        if len(stack) > 1:
            ans.extend(list(str(len(stack))))
    
    # Modify chars in-place
    for i in range(len(ans)):
        chars[i] = ans[i]

    return len(ans)  

# chars = list(input("Enter characters as a string: "))  # Example: "aabbccc"
# new_length = compress(chars)
# print("Compressed characters:", chars[:new_length])  
# print("New length:", new_length)
