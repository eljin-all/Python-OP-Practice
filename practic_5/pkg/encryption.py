def encryption(text, shift):
    """Это функция, создающая шифр Цезаря."""
    path_to_alphabet = 'C:\\Pycharm\\Projects\\OP\\practic_5\\files\\alphabet.txt'
    with open(path_to_alphabet, mode='r', encoding='utf-8') as f:
        alphabet = f.read()
    result = ''
    for h in text:
        if h.upper() not in alphabet:
            result += h
        else:
            if h.upper() == h:
                new_index = (alphabet.index(h) + shift) % len(alphabet)
                result += alphabet[new_index]
            else:
                h = h.upper()
                new_index = (alphabet.index(h) + shift) % len(alphabet)
                result += alphabet[new_index].lower()
    return result