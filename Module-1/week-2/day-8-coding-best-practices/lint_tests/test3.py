import string
SHIFT = 3
CHOICE = input("would you like to encode or decode?")
WORD = input("Please enter text")
LETTERS = string.ascii_LETTERS + string.punctuation + string.digits
ENDCODED = ''
if CHOICE == "encode":
    for letter in WORD:
        if letter == ' ':
            ENDCODED = ENDCODED + ' '
        else:
            x = (LETTERS.index(letter) +
                 SHIFT)
            ENDCODED = ENDCODED + LETTERS[x]
if CHOICE == "decode":
    for letter in word:
        if letter == ' ':
            ENDCODED = ENDCODED + ' '
        else:
            x = LETTERS.index(letter) - SHIFT
            ENDCODED = ENDCODED + LETTERS[x]
print(ENDCODED)
