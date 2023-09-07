from Crypto.Cipher import AES
import base64


def aes_encrypt(key, plaintext):
    # 将密钥和明文转换为字节串
    key_bytes = key.encode("utf-8")
    plaintext_bytes = plaintext.encode("utf-8")

    # 使用 PKCS7 填充方式将明文补齐为 16 的倍数
    pad_len = 16 - len(plaintext_bytes) % 16
    padded_plaintext = plaintext_bytes + bytes([pad_len] * pad_len)

    # 创建 AES 加密器对象
    cipher = AES.new(key_bytes, AES.MODE_ECB)

    # 加密明文
    ciphertext = cipher.encrypt(padded_plaintext)

    # 将密文转换为 Base64 编码的字符串并返回
    return base64.b64encode(ciphertext).decode("utf-8")


def aes_decrypt(key, ciphertext):
    # 将密钥和密文转换为字节串
    key_bytes = key.encode("utf-8")
    ciphertext_bytes = base64.b64decode(ciphertext.encode("utf-8"))

    # 创建 AES 解密器对象
    cipher = AES.new(key_bytes, AES.MODE_ECB)

    # 解密密文
    padded_plaintext = cipher.decrypt(ciphertext_bytes)

    # 去除 PKCS7 填充并返回明文字符串
    pad_len = padded_plaintext[-1]
    plaintext = padded_plaintext[:-pad_len]
    return plaintext.decode("utf-8")


k = "1234567890123456"
c = aes_encrypt(k, "Hello, world!")
print(c)
m = aes_decrypt(k, c)
print(m)
