def int32_to_ip(int32):
    bin_str = bin(int32)[2:].zfill(32)
    result = ''
    for i in range(0, 32, 8):
        result = f'{result}.{int(bin_str[i:i+8], 2)}'
    return result[1::]


def main():
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"


if __name__ == '__main__':
    main()
