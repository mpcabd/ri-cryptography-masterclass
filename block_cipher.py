import sys

from sympy import divisors
from sympy.ntheory import isprime

def _rows_columns(l):
    ds = divisors(l)
    if len(ds) % 2 == 1:
        rows = columns = ds[len(ds) // 2]
    else:
        rows, columns = ds[len(ds) // 2 - 1 : len(ds) // 2 + 1]
    return rows, columns


def block_cipher(message, print_table=False):
    message = message.title().replace(' ', '')
    l = len(message)
    if l < 4:
        raise ValueError('Message too short')
    if isprime(l):
        message += ' '
        l += 1
    rows, columns = _rows_columns(l)

    if print_table:
        for r in range(rows):
            for c in range(columns):
                if c:
                    print('\t', end='', file=sys.stderr)
                print(message[r * columns + c], end='', file=sys.stderr)
            print('\n', end='', file=sys.stderr)

    ciphered_message = []
    for i in range(l):
        ciphered_message.append(message[(i // rows) + (i % rows) * columns])            

    return ''.join(ciphered_message)


def block_decipher(message):
    l = len(message)
    if l < 4 or isprime(l):
        raise ValueError('Invalid ciphered text')
    rows, columns = _rows_columns(l)
    deciphered_message = []
    for i in range(l):
        deciphered_message.append(message[(i // columns) + (i % columns) * rows])
    return ''.join(deciphered_message)

__all__ = ['block_cipher', 'block_decipher']
