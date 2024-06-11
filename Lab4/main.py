# This is a sample Python script.
from Cryptosystem import CryptoSystem

if __name__ == '__main__':
    rabin = CryptoSystem(3, 4, 179, 499)
    ciphertext, redundancies = rabin.encrypt("GAMED")
    print()
    plaintext = rabin.decrypt(ciphertext, redundancies)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
