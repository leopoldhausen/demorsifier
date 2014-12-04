# Written in Python 3.4.2

# Specifically made to decode the morse code used in the Homestuck webcomic,
# which often mixes punctuation with actual morse code.

# This script can take any string. If the string has morse code in it, it will
# decode it. It will leave intact anything that is not code.

# Uses '/' to denote a space.

morse_dict = {
        # Letters and space
        '.-' : 'a', 
        '-...' : 'b',
        '-.-.' : 'c',
        '-..' : 'd',
        '.' : 'e',
        '..-..' : 'é',
        '..-.' : 'f',
        '--.' : 'g',
        '....' : 'h',
        '..' : 'i',
        '.---' : 'j',
        '-.-' : 'k',
        '.-..' : 'l',
        '--' : 'm',
        '-.' : 'n',
        '---' : 'o',
        '.--.' : 'p',
        '--.-' : 'q',
        '.-.' : 'r',
        '...' : 's',
        '-' : 't',
        '..-' : 'u',
        '...-' : 'v',
        '.--' : 'w',
        '-..-' : 'x',
        '-.--' : 'y',
        '--..' : 'z',
        '/' : ' ',
        # Numbers
        '-----' : '0',
        '.----' : '1',
        '..---' : '2',
        '...--' : '3',
        '....-' : '4',
        '.....' : '5',
        '-....' : '6',
        '--...' : '7',
        '---..' : '8',
        '----.' : '9',
        # Punctuation
        '.-.-.-' : '.',
        '--..--' : ',',
        '..--..' : '?',
        '.----.' : "'",
        '-.-.--' : '!',
        '-..-.' : '/',
        '-.--.' : '(',
        '-.--.-' : ')',
        '---...' : ':',
        '-.-.-.' : ';',
        '-...-' : '=',
        '.-.-.' : '+',
        '-....-' : '-',
        '.-..-.' : '"',
        '.--.-.' : '@',
        # Prosigns
        '...-.-' : 'End of work',
        '........' : 'Error',
        '-.-.-' : 'Start of transmission',
        '...-.' : 'Understood',
        '.-...' : 'Wait'
        }
        # Sources: http://en.wikipedia.org/wiki/Morse_code
        #          http://en.wikipedia.org/wiki/Prosigns_for_Morse_code
        #          http://www.itu.int/rec/R-REC-M.1677-1-200910-I/

def demorse(code):
    
    # adding a space before any punctuation so that str.split() works as expected
    if len(code) > 1:
        result = code
        # using negative indices to slice from the right
        # so that the added spaces don't screw with the index position
        for i in range(1-len(code), 0):
            if code[i - 1] in '.-/' and code[i] not in '.-/ ':
                result = result[:i] + ' ' + result[i:]
        code = result
    # the actual decoding
    message = ''
    morse_letters = code.split(' ')
    for letter in morse_letters:
        try:
            message += morse_dict[letter]
        except KeyError: # if letter is not in the morse_dict
            message += letter + ' '
    print(message)

demorse('''TG: (is she here?) 
TG: (is the batterwitch here in my house?????) 
UU: .-. . -- . -- -... . .-. --..-- / -.-- --- ..- .----. .-. . / --- -. .-.. -.-- / -.. .-. . .- -- .. -. --. 
UU: .- .-.. .-.. / - .... .- - / -.-- --- ..- / ... . . / .. ... / -.-. --- -- .. -. --. / ..-. .-. --- -- / -.-- --- ..- .-. / -- . -- --- .-. .. . ... / .- -. -.. / ... ..- -... -.-. --- -. ... -.-. .. --- ..- ... 
TG: (ok) 
TG: (i will keep tellin myself that) 
TG: (it is only a dream) 
TG: (it is only a dream) 
TG: (ugh) 
TG: (my dream nerves are a wreck) 
TG: (hm i wonder if my dream house has any dream booze...) 
TG: (NO!) 
TG: (bad dream roxy) 
TG: (must not) 
TG: (fall off) 
TG: (THE DREAM WAGON!) 
UU: ... .... .... .... .... .... !''')
