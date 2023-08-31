"""Task

Write a program that replaces the standalone "dog" in the following sentence with "cat". 
Use f-string when printing the output.

"A dogmatic dog buys dogecoin to become rich and buy hotdogs every day." 
-->  "Output: A dogmatic cat buys dogecoin to become rich and buy hotdogs every day."
"""



text = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."

replace = text.replace(" dog ", " cat ")

print(f'"Output: {replace} "')
