import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding= "utf-8")
main(languages, encoding, error)

# unicode - universal encoding of all human languages
# the solution to wasted space in characters- use a convention to encode the
# most common characters in using 8 bits and then "escape" into larger
# numbers when we need to encode more characters.   that means we have more
# than one convention that is nothing more than a compression encoding,
# making it possible for most common characters to use 8 bits and then
# escape out into 16 or 32 bits as needed

# the convention for encoding text in python is called UTF-8 which means
# Unicode Transformation Format 8 bits.  it is a convention for encoding Unicode
# characters into sequences of bytes which are sequences of bits which turn
# sequences of switches on and off.  UTF-8 is the current standard

# the script is taking bytes written inside the b'' (byte string) and converting
# them to the UTF-8

# on the left is the numbers for each byte of the UTF-8 (show in hexadecimal)
# on the right has the character output as actual UTF-8

# we have an understanding of string and byte sequences.  in python, a string
# is a UTF-8 encoded sequence of characters for displaying or working with text
# the bytes are then the "raw" sequence of bytes that python uses to store
# this UTF-8 string and start with b' to tell python you are working with raw
# bytes

# all you need to remember is that if you have raw bytes then you must use
# .decode() to get the string

# raw bytes have no convention to them.  they are just sequences of bytes with
# no meaning other than numbers, so you must tell python to decode this into
# a UTF string

# if you have a string and want to send it, store it, share it, or do some other
# operation  then usually it will work, but sometimes python will throw up an error
# saying it does not know what convention is needed  in that case you must
# .encode() to get the bytes you need

# DBES = Decode Bytes, Encode Strings
# when you have bytes and need strings, decode Bytes
# when you have strings and need bytes, encode strings
