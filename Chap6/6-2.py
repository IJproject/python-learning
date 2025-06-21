alphabet = "abcdefghijklmnopqrstuvwxyz"
for word in alphabet:  # for文で展開
    print(f"{word}")

# range関数を使って数値のリストを生成
for num in range(5):  # 0から4までの数値を生成（この場合はスタートを省略している）
    print(f"{num}")   # 0, 1, 2, 3, 4

for num in range(0, 5, 2):  # 0から4までの数値を生成（この場合はスタートを省略している）
    print(f"{num}")         # 0, 2, 4

for num in range(5, -5, -1):  
    print(f"{num}")         # 5, 4, 3, 2, 1, 0, -1, -2, -3, -4