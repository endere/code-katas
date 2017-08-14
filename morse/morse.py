MORSE_CODE = {'..-.': 'F', '-..-': 'X',
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


def decodeBits(bits):
    while bits[-1] == '0':
        bits = bits[:-1]
    for i in range(len(bits)):
        if bits[i] != "0":
            bits = bits[i:]
            break
    rate = 0
    rate2 = 0
    for i in range(len(bits)):
        if bits[i] == "1" and rate2 == 0:
            rate += 1
            continue
        if bits[i] == "0":
            rate2 += 1
            continue
        rate = rate if rate < rate2 else rate2
        break
    if rate == 0:
        return '.'
    bits = bits.split("0" * rate)
    for i in range(len(bits)):
        if bits[i] == "1" * rate:
            bits[i] = '.'
        elif bits[i] == '1' * rate * 3:
            bits[i] = '-'
    i = 0
    while True:
        try:
            if bits[i] == "":
                if bits[i + 1] == "." or bits[i + 1] == '-':
                    count = 0
                    while bits[i - 1] == "":
                        count += 1
                        del bits[i - 1]
                        i -= 1
                        bits[i] = '   ' if count == 5 else ' '
            i += 1
        except IndexError:
            break
    bits = "".join(bits)
    return bits


if __name__ == '__main__':
    print(decodeMorse(decodeBits("00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000101110101110101110")))
    print(decodeMorse(decodeBits('0100010')))

