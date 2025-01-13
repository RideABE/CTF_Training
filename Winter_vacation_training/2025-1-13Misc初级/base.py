def shift_letters(s, shift):
    result = []
    for char in s:
        if 'a' <= char <= 'z':  # 小写字母
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':  # 大写字母
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:  # 非字母字符
            result.append(char)
    return ''.join(result)

# 输入字符串
input_string = "IfqZQC{IbQ_Rp_E4S3_cR0!!!!!}"

# 推动 3 个字母
shifted_string = shift_letters(input_string, 3)
print("结果:", shifted_string)
