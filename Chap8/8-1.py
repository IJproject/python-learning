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

# P.150 8.1.6〜