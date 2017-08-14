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
    for i in range(len(bits)):
        if bits[i] != "0":
            bits = bits[i:]
            break
    rate = 0
    for i in range(len(bits)):
        if bits[i] == "0":
            rate += 1
        if bits[i] == "1" and rate > 0:
            break
    if rate == 0:
        return '.'
    bits = bits.split("0" * rate)
    for i in range(len(bits)):
        if bits[i] == "1" * rate:
            bits[i] = '.'
        elif bits[i] == '1' * rate * 3:
            bits[i] = '-'
        elif len(bits[i]) < rate and bits[i][0] == "1":
            bits[i] = '.'
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
    print(bits)
    bits = "".join(bits)
    print(bits)
    return bits


if __name__ == '__main__':
    print(decodeMorse(decodeBits("10001")))
    print(decodeMorse(decodeBits("1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011")))
