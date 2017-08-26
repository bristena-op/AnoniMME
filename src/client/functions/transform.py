from constants import ENCODING_MAX_LENGTH


def string_to_number(msg):
    return int.from_bytes(str.encode(msg), byteorder='little')


def number_to_string(number):
    number_to_bytes = number.to_bytes(ENCODING_MAX_LENGTH, byteorder='little')
    byte_string = number_to_bytes.replace(b'\x00', b'')

    return byte_string.decode()