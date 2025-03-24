# Problem Statement  :

# Jack is learning to type english from the beginning and he is making an error of repeating the same words in his texts over whatsapp. Write a function that will take input for his text sent to you and then keep only the unique texts.
# Note that, the uniqueness is about being word specific not position, there are nothing but alphabets in the sentences and words are separated only with white space.

# Constraints:
# Words in the line<=10^5
# Alphabets in the words<=20

# Sample Input:
# Send send the image send to to to me

# Output:
# Send the mage to me

def unique_text(text):
  res = ""
  lst = []
  for x in text:
    if x.lower() not in lst:
      lst.append(x.lower())
      res = res + x + " "
  return res

text = "Send send the image send to me"
# text = list(input().split())
print(unique_text(text))