import sys
import string

from sympy import divisors
from sympy.ntheory import isprime


class Cipher(object):
    def cipher(self, message, *args, **kwargs):
        raise NotImplemented('I am an abstract class')

    def decipher(self, message, *args, **kwargs):
        raise NotImplemented('I am an abstract class')


class BlockCipher(Cipher):
    def _rows_columns(self, l):
        ds = divisors(l)
        if len(ds) % 2 == 1:
            rows = columns = ds[len(ds) // 2]
        else:
            rows, columns = ds[len(ds) // 2 - 1: len(ds) // 2 + 1]
        return rows, columns

    def cipher(self, message, print_table=False):
        message = message.title().replace(' ', '')
        l = len(message)
        if l < 4:
            raise ValueError('Message too short')
        if isprime(l):
            message += ' '
            l += 1
        rows, columns = self._rows_columns(l)

        if print_table:
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
    def map_character(self, character, *args, **kwargs):
        raise NotImplemented('I am an abstract class')

    def unmap_character(self, character, *args, **kwargs):
        raise NotImplemented('I am an abstract class')

    def cipher(self, message, *args, **kwargs):
        return ''.join(map(self.map_character, message))

    def decipher(self, message, *args, **kwargs):
        return ''.join(map(self.unmap_character, message))


class SlidingScaleCipher(MappingCipher):
    def __init__(self, rot):
        self.forward_map = {}
        self.backward_map = {}
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

    def map_character(self, character, *args, **kwargs):
        return self.forward_map.get(character, character)

    def unmap_character(self, character, *args, **kwargs):
        return self.backward_map.get(character, character)


class HalfReversedAlphabetCipher(SlidingScaleCipher):
    def __init__(self):
        super().__init__(13)
