def cipher(text, shift, encrypt=True):
    """
    Encrypts or decrypts a Caeser cipher.

    Parameters
    ---
    text: string
        Input string to be either encrypted or decrypted. 
    shift: integer
        Integer value indicating the alphabet shift for the replacement. Can be positive for negative.
    encrypt: bool
        Boolean value determining whether the function encrypts or decrypts 'text'. Defaults to 'True', use false to decrypt. 

    Returns
    ---
    string
        The encrypted or decrypted 'text'.

    Examples
    ---
    Encryption:

    >>> from cipher_jer2240 import cipherpkg
    >>> cipherpkg.cipher('text', 5, encrypt = True)
    'yjCy'

    Decryption:
    >>> from cipher_jer2240 import cipherpkg
    >>> cipherpkg.cipher('yjCy', 5, encrypt = False)
    'text'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text