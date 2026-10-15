text = input('输入文字')
secret = ''
for t in text:
    secret += chr(ord(t) + 1)
print(f'解密文字为{secret}')