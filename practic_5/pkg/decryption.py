def decryption(text, shift):
    """Это функция, дешифрующая криптограмму, созданную по методу Цезаря."""
    path_to_alphabet = 'C:\\Pycharm\\Projects\\OP\\practic_5\\files\\alphabet.txt'
    with open(path_to_alphabet, mode='r', encoding='utf-8') as f:
        alphabet = f.read()
    result = ''
    for h in text:
        if h.upper() not in alphabet:
            result += h
        else:
            if h.upper() == h:
                old_index = ((alphabet.index(h) - shift + len(alphabet))
                             % len(alphabet))
                result += alphabet[old_index]
            else:
                h = h.upper()
                old_index = ((alphabet.index(h) - shift + len(alphabet))
                             % len(alphabet))
                result += alphabet[old_index].lower()
    return result