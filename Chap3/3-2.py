# 数値の区切り
print(1,000,000)  # (1, 0, 0)
print(1_000_000)  # 1000000

# 除算
print(5 / 2)         # 2.5
print(5 // 2)        # 2
print(5 % 2)         # 1
print(divmod(5, 2))  # (2, 1)

# 基数
value = 29
print(bin(value))    # 0b11101（Binary）
print(oct(value))    # 0o35（Octal）
print(hex(value))    # 0x1d（Hexadecimal）

# 文字コードへの変換とその逆
print(chr(65))   # A（文字コードを解釈）
print(ord('A'))  # 65（文字コードへ変換）

# 型の変換
print(int(True))     # 1
print(int(5.9))      # 5（文字列の5.9は処理できない）
print(int("10", 16)) # 16（16進数の10を10進数に変換）