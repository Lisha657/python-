string = "radar"
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

if string == reversed_string:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
