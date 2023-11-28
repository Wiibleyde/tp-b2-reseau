class EncodingNat:
    def encodeInteger(self, toSend):
        return toSend.to_bytes((toSend.bit_length() + 7) // 8, 'big')
    
    def decodeInteger(self, data):
        return int.from_bytes(data, 'big')

if __name__ == '__main__':
    encoded = EncodingNat().encodeInteger(123456789)
    print(encoded)
    decoded = EncodingNat().decodeInteger(encoded)
    print(decoded)