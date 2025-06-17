# スライスによる文字列の取り出し
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0:3])  # abc（0~2）
print(alphabet[10:])  # klmnopqrstuvwxyz（11~）
print(alphabet[:5])   # abcde（~4）

# ステップ
print(alphabet[::2])  # acegikmoqsuwy（奇数番目の文字）
print(alphabet[::-1]) # zyxwvutsrqponmlkjihgfedcba（逆順）

# 範囲外に対して寛容
print(alphabet[100:200])  # 空文字列（範囲外は無視されるて空文字になる）