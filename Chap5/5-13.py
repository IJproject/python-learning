# 探索と選択
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet.startsWith('abc'))  # True（先頭がabc）
print(alphabet.endsWith('xyz'))    # True（末尾がxyz）

# 文字列の探索
# find関数（見つからなければ例外を出す）
# index関数（見つからなければ例外を出す）
print(alphabet.find('abc'))   # 0（先頭からの位置）
print(alphabet.index('xyz'))  # 0（先頭からの位置）
print(alphabet.rfind('abc'))  # 23（末尾からの位置）
print(alphabet.rindex('xyz')) # 23（末尾からの位置）

# その他
alphabet.count('a')  # 1（aの出現回数）
alphabet.isalnum()   # True（英数字のみか）