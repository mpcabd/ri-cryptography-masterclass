import sys
import string
import random

from sympy import divisors
from sympy.ntheory import isprime


class Cipher(object):
    def cipher(self, message, *args, **kwargs):
        raise NotImplemented('I am an abstract class')

    def decipher(self, message, *args, **kwargs):
        raise NotImplemented('I am an abstract class')


class BlockCipher(Cipher):
    def __init__(self, print_table=False):
        super().__init__()
        self.print_table = print_table

    def _rows_columns(self, l):
        ds = divisors(l)
        if len(ds) % 2 == 1:
            rows = columns = ds[len(ds) // 2]
        else:
            rows, columns = ds[len(ds) // 2 - 1: len(ds) // 2 + 1]
        return rows, columns

    def cipher(self, message):
        message = message.title().replace(' ', '')
        l = len(message)
        if l < 4:
            raise ValueError('Message too short')
        if isprime(l):
            message += ' '
            l += 1
        rows, columns = self._rows_columns(l)

        if self.print_table:
            for r in range(rows):
                for c in range(columns):
                    if c:
                        print('\t', end='', file=sys.stderr)
                    print(message[r * columns + c], end='', file=sys.stderr)
                print('\n', end='', file=sys.stderr)

        ciphered_message = []
        for i in range(l):
            ciphered_message.append(
                message[(i // rows) + (i % rows) * columns])

        return ''.join(ciphered_message)

    def decipher(self, message):
        l = len(message)
        if l < 4 or isprime(l):
            raise ValueError('Invalid ciphered text')
        rows, columns = self._rows_columns(l)
        deciphered_message = []
        for i in range(l):
            deciphered_message.append(
                message[(i // columns) + (i % columns) * rows])
        return ''.join(deciphered_message)


class MappingCipher(Cipher):
    def __init__(self, print_mapping=False):
        super().__init__()
        self.print_mapping = print_mapping

    def map_character(self, character, *args, **kwargs):
        raise NotImplemented('I am an abstract class')

    def unmap_character(self, character, *args, **kwargs):
        raise NotImplemented('I am an abstract class')

    def cipher(self, message, *args, **kwargs):
        if self.print_mapping:
            self._print_mapping()
        return ''.join(map(self.map_character, message))

    def decipher(self, message, *args, **kwargs):
        return ''.join(map(self.unmap_character, message))
    
    def _print_mapping(self):
        for c in string.ascii_lowercase:
            print(f'{c}, {c.upper()} ➡️ {self.map_character(c)}, {self.map_character(c.upper())}', file=sys.stderr)


class MapBasedCipher(MappingCipher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.forward_map = {}
        self.backward_map = {}
        
    def map_character(self, character, *args, **kwargs):
        return self.forward_map.get(character, character)

    def unmap_character(self, character, *args, **kwargs):
        return self.backward_map.get(character, character)


class SlidingScaleCipher(MapBasedCipher):
    def __init__(self, rot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rot = rot % 26

        lscale = string.ascii_lowercase * 2  # repeat letters twice
        uscale = string.ascii_uppercase * 2  # repeat letters twice

        for i in range(26):
            # lower case
            self.forward_map[lscale[i]] = lscale[i + self.rot]
            self.backward_map[lscale[i + self.rot]] = lscale[i]

            # upper case
            self.forward_map[uscale[i]] = uscale[i + self.rot]
            self.backward_map[uscale[i + self.rot]] = uscale[i]


class HalfReversedAlphabetCipher(SlidingScaleCipher):
    def __init__(self, *args, **kwargs):
        super().__init__(13, *args, **kwargs)


class RandomMappingCipher(MapBasedCipher):
    def __init__(self, lcase_alphabet=string.ascii_lowercase, ucase_alphabet=string.ascii_uppercase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lcase_alphabet = lcase_alphabet
        self.ucase_alphabet = ucase_alphabet
        
        shuffled_indexes = list(range(26))
        random.shuffle(shuffled_indexes)
        
        for i in range(26):
            index = shuffled_indexes[i]
            # print(f'{string.ascii_lowercase[i]} => {index}')
            self.forward_map[string.ascii_lowercase[i]] = self.lcase_alphabet[index]
            self.forward_map[string.ascii_uppercase[i]] = self.ucase_alphabet[index]
            
            self.backward_map[self.lcase_alphabet[index]] = string.ascii_lowercase[i]
            self.backward_map[self.ucase_alphabet[index]] = string.ascii_uppercase[i]


class RandomMappingEmojiCipher(RandomMappingCipher):
    LCASE_ALPHABET = '🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🌮🍒🍓🫐🥝🍅🫒🥥🥑🥪🥔🥕🌽🌷🌳'
    UCASE_ALPHABET = '🥒🥬🥦🧄🧅🍄🥜🫘🌰🍞🥐🥖🫓🥨🥯🥞🧇🧀🍖🍗🥩🥓🍔🍟🍕🌭'

    def __init__(self, *args, **kwargs):
        super().__init__(self.LCASE_ALPHABET, self.UCASE_ALPHABET, *args, **kwargs)