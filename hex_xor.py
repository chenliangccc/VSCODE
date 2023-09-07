def hex_xor(a, b):
    # 将十六进制字符串转换为整数
    a_int = int(a, 16)
    b_int = int(b, 16)
    # 对整数进行异或操作
    result_int = a_int ^ b_int
    # 将异或结果转换为十六进制字符串
    result_hex = hex(result_int)[2:]
    # 如果结果字符串长度不足 2 的倍数，则在前面补零if len
    if len(result_hex) % 2 != 0:
        result_hex = f"0{result_hex}"
    return result_hex


a = "6f"
b = "65"
print(hex_xor(a, b))
