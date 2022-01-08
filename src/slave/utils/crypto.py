def xor(left_data, right_data):
    return bytearray(l^r for l, r in zip(*map(bytearray, [left_data, right_data])))

def encrypt(in_data, key):
    return xor(in_data.encode("utf-8"), key)

def decrypt(in_data, key):
    return xor(in_data, key).decode()
