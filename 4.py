"""
Придумать и написать шифровальщик текста
Он будет принимать строку и ключ шифрования, возвращать ее в зашифрованном виде
Затем должен быть дешифровальщик который пример зашифрованную строку и ключ и расшифрует ее
"""

"""Всем привет -> Жцйс фхнжйч -> Всем привет"""  # Придумать что-то интереснее шифра Цезаря


def encrypt_massage(massage: str, key: int) -> str:
    """
    Функция , принимающая на вход сообщение и ключ шифрования
    :param massage:
    :param key:
    :return: возвращается закодированное сообщение в виде str
    """
    encode_message = ''.join(
        [
            (chr(ord(letter) + key))
            for letter in massage
        ]
    )
    return encode_message


def decrypt_massage(encoded_massage: str, key: int) -> str:
    """
    Функция , принимающаяя на входе зашифрованное сообщение и ключ
    :param encoded_massage:
    :param key:
    :return: Возращает расшифрованное сообщение в виде str
    """
    decoded_message = ''.join(
        [
            chr(ord(letter) - key)
            for letter in encoded_massage
        ]
    )
    return decoded_message


user_input = input("Введите сообщение: ")
key = int(input("Введите ключ шифрования: "))

encode_message = encrypt_massage(user_input, key)
decode_message = decrypt_massage(encode_message, key)

print("Зашифрованное сообщение:", encode_message)

encoded_message = input("Введите зашифрованное сообщение: ")
key = int(input("Введите ключ шифрования: "))

print("Расшифрованное сообщение:", decode_message)
