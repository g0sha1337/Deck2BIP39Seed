import hashlib


def ask_card_sute(number_of_card):
    # !TODO create validation of input
    suite = int(input(f'What is the card suit of {number_of_card}\'s card?\n\n1 - Diamonds (Бубны)\n2 - Hearts (Червы)\n3 - Spades (Пики)\n4 - Clubs (Трефы)'))
    return bin(suite)[2::].zfill(2)# fill 2 bit if they are empty

def ask_card_rank(number_of_card):
    # !TODO create validation of input
    rank = int(input(f'What is the card rank of the {number_of_card}\'s card?\n\n1 - Six (Шестерка)\n2 - Seven (Семерка)\n3 - Eight (Восьмерка)\n4 - Nine (Девятка)\n5 - Ten (Десятка)\n6 - Jack (Валет)\n7 - Queen (Дама)\n8 - King (Король)\n9 - Ace (Туз)'))
    return bin(rank)[2::].zfill(4) # fill 4 bit if they are empty

if __name__ == '__main__':
    print("Deck of 36 card to 12 words bip39 seed")
    value128bit = ""
    # while (int(input("R U ready to show you combination?\n 0 to no\n1 for yes"))):
    #     continue
    for i in range(0,23): #main cycle to read combination of 22 cardz
        carddata = ""
        carddata +=ask_card_sute(i+1)
        carddata +=ask_card_rank(i+11)
        print(f'your num is {carddata}')
        value128bit+=carddata

    value128bit = value128bit[:-4] # cut last 4 bit from 22's card to make 128bit value
    # value128bit+=   hashlib.sha256(value128bit.encode()).digest() !TODO add 4 first bits of hash 


    # TODO add converte 132 bits (with hashed 4 bits) into 12 words of bip39 wordlist
        

