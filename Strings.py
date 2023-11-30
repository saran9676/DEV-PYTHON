# Sample string
my_string = "Hello, World!"

# Common string functions
print("Original String:", my_string)
print("Length:", len(my_string))
print("Upper Case:", my_string.upper())
print("Lower Case:", my_string.lower())
print("Capitalized:", my_string.capitalize())
print("Title Case:", my_string.title())
print("Is Alpha (letters only):", my_string.isalpha())
print("Is Numeric:", my_string.isnumeric())
print("Is Alphanumeric:", my_string.isalnum())
print("Count 'l':", my_string.count('l'))
print("Replace 'Hello' with 'Hi':", my_string.replace("Hello", "Hi"))
print("Starts with 'Hello':", my_string.startswith("Hello"))
print("Ends with 'World!':", my_string.endswith("World!"))
print("Split by comma:", my_string.split(","))
print("Joined with space:", " ".join(my_string.split(",")))
print("Index of 'o':", my_string.index('o'))
print("Substring from index 7 to 12:", my_string[7:12])
print("Strip leading and trailing whitespaces:", my_string.strip())
print("Find 'o':", my_string.find('o'))
print("Check if all characters are in uppercase:", my_string.isupper())
print("Check if all characters are in lowercase:", my_string.islower())
print("Check if the string is titlecased:", my_string.istitle())
print("Swap case:", my_string.swapcase())
print("Check if string ends with 'ld!':", my_string.endswith("ld!"))
print("Partition the string at the first comma:", my_string.partition(","))
print("Encode as bytes using UTF-8:", my_string.encode('utf-8'))
print("Decode bytes using UTF-8:", my_string.encode('utf-8').decode('utf-8'))
print("Centered within a string of length 20:", my_string.center(20, '*'))
print("Z-filled to a width of 15:", my_string.zfill(15))
print("Original String:", my_string)
print("Check if all characters are decimal:", my_string.isdecimal())
print("Check if all characters are printable:", my_string.isprintable())
print("Check if all characters are whitespace:", my_string.isspace())
print("Check if the string is composed of titlecased words:", my_string.istitle())
print("Join with '-' using join method:", '-'.join(my_string))
print("Replace 'o' with 'x' (max 2 occurrences):", my_string.replace('o', 'x', 2))
print("Expand tabs (assuming tab size is 4 spaces):", "Hello\tWorld!".expandtabs(4))
print("Find 'o' starting from index 5 to 10:", my_string.find('o', 5, 10))
print("Partition at the first occurrence of 'o':", my_string.partition('o'))
print("Splitlines on line breaks:", "Hello\nWorld".splitlines())


'''Original String: Hello, World!
Length: 13
Upper Case: HELLO, WORLD!
Lower Case: hello, world!
Capitalized: Hello, world!
Title Case: Hello, World!
Is Alpha (letters only): False
Is Numeric: False
Is Alphanumeric: False
Count 'l': 3
Replace 'Hello' with 'Hi': Hi, World!
Starts with 'Hello': True
Ends with 'World!': True
Split by comma: ['Hello', ' World!']
Joined with space: Hello  World!
Index of 'o': 4
Substring from index 7 to 12: World
Strip leading and trailing whitespaces: Hello, World!
Find 'o': 4
Check if all characters are in uppercase: False
Check if all characters are in lowercase: False
Check if the string is titlecased: True
Swap case: hELLO, wORLD!
Check if string ends with 'ld!': True
Partition the string at the first comma: ('Hello', ',', ' World!')
Encode as bytes using UTF-8: b'Hello, World!'
Decode bytes using UTF-8: Hello, World!
Centered within a string of length 20: ***Hello, World!****
Z-filled to a width of 15: 00Hello, World!
Original String: Hello, World!
Check if all characters are decimal: False
Check if all characters are printable: True
Check if all characters are whitespace: False
Check if the string is composed of titlecased words: True
Join with '-' using join method: H-e-l-l-o-,- -W-o-r-l-d-!
Replace 'o' with 'x' (max 2 occurrences): Hellx, Wxrld!
Expand tabs (assuming tab size is 4 spaces): Hello   World!
Find 'o' starting from index 5 to 10: 8
Partition at the first occurrence of 'o': ('Hell', 'o', ', World!')
Splitlines on line breaks: ['Hello', 'World']'''