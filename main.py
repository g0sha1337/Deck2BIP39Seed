import hashlib


def ask_card_sute(number_of_card):
    # !TODO create validation of input
    suite = int(input(f'What is the card suit of {number_of_card}\'s card?\n\n1 - Diamonds (Бубны)\n2 - Hearts (Червы)\n3 - Spades (Пики)\n4 - Clubs (Трефы)'))
    return bin(suite)[2::].zfill(2)# fill 2 bit if they are empty

def ask_card_rank(number_of_card):
    # !TODO create validation of input
    rank = int(input(f'What is the card rank of the {number_of_card}\'s card?\n\n1 - Six (Шестерка)\n2 - Seven (Семерка)\n3 - Eight (Восьмерка)\n4 - Nine (Девятка)\n5 - Ten (Десятка)\n6 - Jack (Валет)\n7 - Queen (Дама)\n8 - King (Король)\n9 - Ace (Туз)'))
    return bin(rank)[2::].zfill(4) # fill 4 bit if they are empty

def bits2seed(bits):
    seed = ''
    wordlistfile = open('bip39wordlist.txt', 'r')
    wordlist = wordlistfile.readlines()
    if len(bits) == 132:
        i = 0 
        j = 11
        for j in range (11, 133, 11): #taking a 11 bit to get index of bip39 wordlist
            binary_index = ''
            for k in range(i, j):
                binary_index+=bits[k]
            seed += f'{wordlist[int(binary_index, 2)].strip()} '
            i+=11
    else:
        print("Some error with getting bip39 words...")
        exit(-1)
    return seed

def checksum (bits):
    int_value = int(bits, 2)

    # Преобразуем целое число в байты (16 байт для 128 бит)
    byte_value = int_value.to_bytes(16, byteorder='big')

    # Получаем SHA-256 хэш
    hash_value = hashlib.sha256(byte_value).digest()  # Используем .digest() для получения байтов

    # Преобразуем байты хэша в двоичный формат
    binary_hash = ''.join(format(byte, '08b') for byte in hash_value)

    return binary_hash[:4]  # Возвращаем первые 4 бита

if __name__ == '__main__':
    print("Deck of 36 card to 12 words bip39 seed")
    value128bit = ""
    value128bit += '10100000000010000001010000001001000000001001110001000000010010000000001000000100010000000001000100100100101000010000000011100100'

    # for i in range(0,23): #main cycle to read combination of 22 cardz
    #     carddata = ""
    #     carddata +=ask_card_sute(i+1)
    #     carddata +=ask_card_rank(i+1)
    #     print(f'your num is {carddata}')
    #     value128bit+=carddata

    # value128bit = value128bit[:-4] # cut last 4 bit from 22's card to make 128bit value
    
    value128bit += checksum(value128bit)
    print(f'{value128bit} - {len(value128bit)} bits')
    seed = bits2seed(value128bit)
    print (f'COOL, YOUR SEED IS {seed}')


        

