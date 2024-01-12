def separate_and_convert(s):

    numbers = ''.join([char for char in s if char.isdigit()])
    letters = ''.join([char for char in s if char.isalpha()])

    converted_numbers = [str(ord(char)) for char in numbers if int(char) % 2 == 0]
    converted_letters = [str(ord(char)) for char in letters if char.isupper()]

    return numbers, letters, converted_numbers, converted_letters

s = '5464DDSDlhaks54r3hfks464844FFR46464OIOnk'
number_string, letter_string, ascii_numbers, ascii_letters = separate_and_convert(s)

print("Number String:", number_string)
print("Letter String:", letter_string)
print("ASCII Codes of Even Numbers:", ascii_numbers)
print("ASCII Codes of Upper-case Letters:", ascii_letters)

