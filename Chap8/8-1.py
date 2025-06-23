# 辞書型：連想配列やハッシュなどと同じ
# キーにはイミュータブル型の値であれば何でもOK

# dict関数による生成と変更
created_dict1 = dict(name="John", age=30)
print(created_dict1)  # {'name': 'John', 'age': 30}
created_dict2 = dict([("name", "Alice"), ("age", 25)])
print(created_dict2)  # {'name': 'Alice', 'age': 25}

# 値の変更
created_dict1["age"] = 31           # 既存のキーの値を変更
created_dict1["city"] = "New York"  # 新しいキーと値の追加（存在しないキーを指定した場合、新しく作られる）
print(created_dict1)                # {'name': 'John', 'age': 31, 'city': 'New York'}

# キーから値の取得
print(created_dict1["name"])                    # John
print(created_dict1.get("age"))                 # 31
print(created_dict1.get("country", "Unknown"))  # Unknown（存在しないキーを指定した場合、第2引数が返り値になる。指定しない場合はNoneが返る）

# 辞書のキーとバリュー（リストにするにはlist関数を明示的に使用しないといけない）
sample_dict = { "name": "Bob", "age": 22, "city": "Los Angeles" }
sample_dict.keys()      # dict_keys(['name', 'age', 'city'])
sample_dict.values()    # dict_values(['Bob', 22, 'Los Angeles'])
sample_dict.items()     # dict_items([('name', 'Bob'), ('age', 22), ('city', 'Los Angeles')])
print(len(sample_dict)) # 3（キーの数を取得）

# 辞書の結合
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
merged_dict = {**dict1, **dict2}  # 辞書を結合
print(merged_dict)                # {'a': 1, 'b': 3, 'c': 4}
merged_dict.update(dict3)         # 辞書を更新
print(merged_dict)                # {'a': 1, 'b': 3, 'c': 4, 'd': 5}

# 要素の削除
del dict1["a"]  # キーを指定して削除
print(dict1)    # {'b': 2}
dict1.pop("b")  # キーを指定して削除（指定したキーのバリューを返す）
print(dict1)    # {}
dict2.clear()   # 辞書の中身を全て削除
print(dict2)    # {}

# 比較
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 2, "x": 1}
dict_c = {"x": 1, "y": 3}
print(dict_a == dict_b)  # True
print(dict_a == dict_c)  # False
print(dict_a != dict_c)  # True

# 反復処理
iteration_dict = {"name": "Charlie", "age": 28, "city": "Chicago"}
# for key in iteration_dict:               # キーで反復
# for key in iteration_dict.keys():        # 明示的にキーで反復
# for value in iteration_dict.values():    # 値で反復
for key, value in iteration_dict.items():  # キーと値で反復
    print(f"{key}: {value}")  # name: Charlie, age: 28, city: Chicago

# 代入とコピー、内包表記については、リストの時と同様
