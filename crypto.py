
# caesar cypher
def cipher(message):
    message2cipher = {'a':'01', 'b':'02', 'c':'03', 'd':'04', 'e':'05', 'f':'06', 'g':'07', 'h':'08', 'i':'09', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25','z':'26' }
    ciphertext = ''
    for letter in message:
        ciphertext = ciphertext + message2cipher[letter]
    return ciphertext


def decipher(ciphertext):
    cipher2message = {'01':'a', '02':'b', '03':'c', '04':'d', '05':'e', '06':'f', '07':'g', '08':'h', '09':'i', '10':'j', '11':'k', '12':'l', '13':'m', '14':'n', '15':'o', '16':'p', '17':'q', '18':'r', '19':'s', '20':'t', '21':'u', '22':'v', '23':'w', '24':'x', '25':'y', '26':'z'}
    msg = ''
    for i in range(0, len(ciphertext), 2):
        token = ciphertext[i] + ciphertext[i+1]
        msg = msg + cipher2message[token]

    return msg

if __name__ == '__main__':

    message = 'hello everybody i am ananya'
    print(cipher(message))
    print(decipher(cipher(message)))
