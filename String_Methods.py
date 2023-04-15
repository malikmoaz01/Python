s1 = "abc"
print(s1.capitalize()) # First Letter Capital

s2 = "ABC"
print(s2.casefold())   # Into Lower Case

s3 = "XYZ"
print(s3.center(20))   # Str into the Center 

s4 ="XXXZZZLLLX"
print(s4.count("X" ))  # Count No of Letters in A string

s5 = "My Nåme"
print(s5.encode())       # The encode() method encodes the string, using the specified encoding.If no encoding is specified, UTF-8 will be used.

s6 = "ABCDE"
print(s6.endswith("E"))   # Returns true if the string ends with the specified value

s7 = "M\ta\tl\ti\tk"
print(s7.expandtabs(4))    # Set tab size of  string

s7_ = "My {n} is Malik Moaz!"
print(s7_.format(n = "name"))  # Formats specified values  in String

# s8 = "a b c d e f g h "
# print(s8.find("e")) # Find Method used for knowing the place 

s9 = "a b c d e"
print(s9.index("c"))

s10 = "zakariya is my friend"

print(s10.isalnum()) # The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9). if space include in this , it will return false .

s11 = "USER"
print(s11.isalpha()) # Returns True if all characters in the string are in the alphabet

s12 = "Apple"
print(s12.isascii()) # Returns True if all characters in the string are ASCII

s13 = "1234"
print(s13.isdigit()) # Returns True if all characters in the string are digits

s14 = "Banana"
print(s14.isidentifier()) # Returns True if the string is an identifier. A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

s15 = "Orange"
print(s15.islower()) 
# islower()	Returns True if all characters in the string are lower case
print(s15.isnumeric())
# isnumeric()	Returns True if all characters in the string are numeric
print(s15.isprintable())
# isprintable()	Returns True if all characters in the string are printable
print(s15.isspace())
# isspace()	Returns True if all characters in the string are whitespaces
print(s15.istitle())
# istitle()	Returns True if the string follows the rules of a title
print(s15.isupper())
# isupper()	Returns True if all characters in the string are upper case

s16 = "Kiwi Orange Mango"
print(" - ".join(s16)) # The join() method takes all items in an iterable and joins them into one string. 

s17 = "banana"
x = s17.ljust(20)
print(x, "is my favorite fruit.") # The ljust() method will left align the string, using a specified character (space is default) as the fill character.

s18 = "     banana     "
x = s18.lstrip()
print("of all fruits", x, "is my favorite") # The lstrip() method removes any leading characters (space is the default leading character to remove)

# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning