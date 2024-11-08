import hashlib


def ask_card_sute(number_of_card):
    suite = 0
    suite = int(input(f'What is the card suit of {number_of_card}\'s card?\n\n1 - Diamonds (Бубны)\n2 - Hearts (Червы)\n3 - Spades (Пики)\n4 - Clubs (Трефы)'))
    while not (1<=suite<=4):
        suite = int(input(f'\nInvalid input, try again\nWhat is the card suit of {number_of_card}\'s card?\n\n1 - Diamonds (Бубны)\n2 - Hearts (Червы)\n3 - Spades (Пики)\n4 - Clubs (Трефы)'))

    return bin(suite)[2::].zfill(2)# fill 2 bit if they are empty

def ask_card_rank(number_of_card):
    rank = 0 
    rank = int(input(f'What is the card rank of the {number_of_card}\'s card?\n\n1 - Six (Шестерка)\n2 - Seven (Семерка)\n3 - Eight (Восьмерка)\n4 - Nine (Девятка)\n5 - Ten (Десятка)\n6 - Jack (Валет)\n7 - Queen (Дама)\n8 - King (Король)\n9 - Ace (Туз)'))
    while not (1<=rank<=9):
        rank = int(input(f'\nInvalid input, try again\nWhat is the card rank of the {number_of_card}\'s card?\n\n1 - Six (Шестерка)\n2 - Seven (Семерка)\n3 - Eight (Восьмерка)\n4 - Nine (Девятка)\n5 - Ten (Десятка)\n6 - Jack (Валет)\n7 - Queen (Дама)\n8 - King (Король)\n9 - Ace (Туз)'))
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
    if len(bits) != 128:
        print("Some error acured...")
        exit(-1)
    int_value = int(bits, 2)
    byte_value = int_value.to_bytes(16, byteorder='big')
    hash_value = hashlib.sha256(byte_value).digest() 
    binary_hash = ''.join(format(byte, '08b') for byte in hash_value)

    return binary_hash[:4] 

if __name__ == '__main__':
    print("Deck of 36 card to 12 words bip39 seed")
    value128bit = ""
    

    for i in range(0,22): #main cycle to read combination of 22 cardz
        carddata = ""
        carddata +=ask_card_sute(i+1)
        carddata +=ask_card_rank(i+1)
        print(f'your num is {carddata}')
        value128bit+=carddata

    #value128bit = value128bit[:-10] # cut last 4 bit from 22's card to make 128bit value
    while (len(value128bit) != 128):
        value128bit = value128bit[:-1]
    
    print(f'{value128bit} - {len(value128bit)} bits')
    value128bit += checksum(value128bit)
    seed = bits2seed(value128bit)
    print (f'YOUR GENERATED SEED IS: \n{seed}')


        

