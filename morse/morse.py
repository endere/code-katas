MORSE_CODE = {'..-.': 'F', '-..-': 'X', '...---...': "SOS",
                 '.--.': 'P', '-': 'T', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                 '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                 '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                 '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                 '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                 '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}




def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    to_return = ""
    for i in range(len(morseCode)):
        if morseCode[i] != " ":
            morseCode = morseCode[i:]
            break
    morseCode = morseCode.split('   ')
    if len(morseCode) > 1:
        for i in morseCode:
            to_return += decodeMorse(i) + ' '
    else:
        morseCode = morseCode[0].split()
        for i in morseCode:
            to_return += MORSE_CODE[i]
    try:
        if to_return[-1] == ' ':
            to_return = to_return[:-1]
    except IndexError:
        pass
    return to_return





if __name__ == '__main__':
    print(decodeMorse('.... . -.--   .--- ..- -.. .'))
    print(decodeMorse('...---...'))