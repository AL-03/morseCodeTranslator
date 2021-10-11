################
# Morse Code Translator
# Author: Alice L.
# Date: Monday, October 11, 2021
###############

# Function used to decode a Morse Code message
def decode_morse_code(message):
    if message == " ":
        print(" ")
    else:
        message = message.strip()
        decoded = message.replace(" .-/", "A").replace(" -.../", "B").replace(" -.-./", "C").replace(" -../", "D").replace(" ./", "E")\
            .replace(" ..-./", "F").replace(" --./", "G").replace(" ..../", "H").replace(" ../", "I").replace(" .---/", "J")\
            .replace(" -.-/", "K").replace(" .-../", "L").replace(" --/", "M").replace(" -./", "N").replace(" ---/", "O").replace(" .--./", "P")\
            .replace(" --.-/", "Q").replace(" .-./", "R").replace(" .../", "S").replace(" -/", "T").replace(" ..-/", "U").replace(" ...-/", "V")\
            .replace(" .--/", "W").replace(" -..-/", "X").replace(" -.--/", "Y").replace(" --../", "Z")
        print("This is the decoded message: " + decoded)

# Function used to translate a sentence into Morse Code
def translate_to_morse_code(message):
    message = message.strip().upper()
    translated = message.replace(" ", " / ").replace("A", ".- ").replace("B", "-... ").replace("C", "-.-. ").replace("D", "-.. ")\
        .replace("E", ". ").replace("F", " ..-./").replace("G", "--. ").replace("H", ".... ").replace("I", ".. ").replace("J", ".--- ")\
        .replace("K", " -.-/").replace("L", ".-.. ").replace("M", "-- ").replace("N", "-. ").replace("O", "--- ").replace("P", ".--. ")\
        .replace("Q", "--.- ").replace("R", ".-. ").replace("S", "... ").replace("T", "- ").replace("U", "..- ").replace("V", "...- ")\
        .replace("W", ".-- ").replace("X", "-..- ").replace("Y", "-.-- ").replace("Z", "--.. ")
    print(translated)

# Morse Code Decoder
print("MORSE CODE DECODER - Decodes a Morse Code message.\nNote:\n1. Use - as a dash\n2. Put a space at the start of each character, and a / at the end of each character\n3. Use 2 spaces to separate words\n4. Enter a space to go to the translator")

morse_message = input("Type your message here: ")
decode_morse_code(morse_message)

# Morse Code Translator
print("\nTRANSLATE TO MORSE CODE - Translates a message into Morse Code.\nNote:\nOnly letters can be used\n")
message_to_translate = input("Type your message here: ")
translate_to_morse_code(message_to_translate)
