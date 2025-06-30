# 集合
empty_set = set()  # 空の集合を作成（初期化）
odd_numbers = {1, 3, 5, 7, 9}   # 奇数の集合を作成
even_numbers = {0, 2, 4, 6, 8}  # 偶数の集合を作成

# 集合への変換(辞書型ではキーが取れる)
sample_dict = {"name": "Alice", "age": 25, "city": "New York"}
sample_dict_set = set(sample_dict)  # 辞書のキーを集合に変換
print(sample_dict_set)              # {'name', 'age', 'city'}

# 要素の追加と削除
odd_numbers.add(11)  # 要素の追加
print(odd_numbers)   # {1, 3, 5, 7, 9, 11}
odd_numbers.remove(11)  # 要素の削除
print(odd_numbers)       # {1, 3, 5, 7, 9}

# P.164 8.2.8~