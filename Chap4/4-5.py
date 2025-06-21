# in演算子による多重比較
# 文字列だけではなく、配列やタプル、辞書に対しても同様に使用することができる
vowels = 'aeiou'
word = "o"
if word in vowels:
    print(f"{word} is a vowel")
else:
    print(f"{word} is not a vowel")
