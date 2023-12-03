from collections import Counter

if __name__ == '__main__':
    cryptogram = '''
    53‡‡†305))6*;4826)4‡.)4‡);80
    6*;48†8¶60))85;1‡(;:‡*8†83(88)
    5*†;46(;88*96*?;8)*‡(;485);5*†
    2:*‡(;4956*2(5*-4)8¶8*;40692
    85);)6†8)4‡‡;1(‡9;48081;8:8‡1
    ;48†85;4)485†528806*81(‡9;48
    ;(88;4(‡?34;48)4‡;161;:188;‡?;
    '''

    """
    Decrypt message above, which is most likely a text message encrypted with a simple substitution cipher.
    """
    cryptogram = cryptogram.replace(' ', '').replace('\n', '')
    print(cryptogram)

    counts = Counter(cryptogram)
    print(counts)

    count_keys = list(counts.keys())

    # e a o i d h n r s t u y c f g l m w b k p q x z
    # english_common = ["e", "a", "o", "i", "d", "h", "n", "r", "s", "t", "u", "y", "c", "f", "g", "l", "m", "w", "b", "k", "p", "q", "x", "z"]
    # print(''.join(dict(zip(counts.keys(), english_common))[c] for c in cryptogram))

    mapping = {'8': 'e'}

    # the == ';48'
    mapping[';'] = 't'
    mapping['4'] = 'h'

    print(''.join(mapping.get(c, c) for c in cryptogram))

    # tree
    mapping['('] = 'r'

    print(''.join(mapping.get(c, c) for c in cryptogram))

    # through
    mapping['‡'] = 'o'
    mapping['?'] = 'u'
    mapping['3'] = 'g'

    print(''.join(mapping.get(c, c) for c in cryptogram))

    # degree
    mapping['†'] = 'd'

    print(''.join(mapping.get(c, c) for c in cryptogram))

    # thirteen
    mapping['6'] = 'i'
    mapping['*'] = 'n'

    print(''.join(mapping.get(c, c) for c in cryptogram))

    # minutes
    mapping['9'] = 'm'
    mapping[')'] = 's'
    print(''.join(mapping.get(c, c) for c in cryptogram))

    # Agood, and
    mapping['5'] = 'a'
    print(''.join(mapping.get(c, c) for c in cryptogram))

    # glass
    mapping['0'] = 'l'
    print(''.join(mapping.get(c, c) for c in cryptogram))

    # devil
    mapping['¶'] = 'v'

    # from
    mapping['1'] = 'f'
    print(''.join(mapping.get(c, c) for c in cryptogram))

    # eye
    mapping[':'] = 'y'
    print(''.join(mapping.get(c, c) for c in cryptogram))

    # bishop, bee
    mapping['2'] = 'b'
    mapping['.'] = 'p'
    print(''.join(mapping.get(c, c) for c in cryptogram))

    # branch
    mapping['-'] = 'b'
    print(''.join(mapping.get(c, c) for c in cryptogram))






