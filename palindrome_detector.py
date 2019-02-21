# Iterative means of determining whether or not input is a palindrome.

def remove_non_alpha(input_text):
    """Remove every character that is not a letter."""
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters += all_letters.upper()

    new_text = ""
    for char in input_text:
        if char in all_letters:
            new_text += char
    return new_text


def palindrome_test(input_text):
    """Returns True or False if the text is a palindrome."""
    input_text = remove_non_alpha(input_text.lower())

    for idx in range(len(input_text)):
        if input_text[idx] != input_text[-(idx + 1)]:
            return False
            
    return True

input_text = input("Please enter the text you wish to test: ")
if palindrome_test(input_text):
    print(input_text + " is a palindrome!")
else:
    print(input_text + " is not a palindrome!")

# Simple solution - original approach with the exception of the print functions, which were orginally in the palindrome_test function and did not work
# def remove_non_alpha(input_text):
#     """Remove every character that is not a letter."""
#     all_letters = "abcdefghijklmnopqrstuvwxyz"
#     all_letters += all_letters.upper()

#     new_text = ""
#     for char in input_text:
#         if char in all_letters:
#             new_text += char
#     return new_text

# def palindrome_test(input_text):
#     """Return True or False if the text is a palindrome."""
#     # Remove non-alpha characters and make lowercase - I originally split the string, which is not needed because the characters will be delivered as a string/\.
#     input_text = remove_non_alpha(input_text.lower())
#     return input_text == input_text[::-1]

# input_text = input("Please enter the text you wish to test: ")
# if palindrome_test(input_text):
#     print(input_text + " is a palindrome!")
# else:
#     print(input_text + " is not a palindrome!")
