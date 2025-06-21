# 文字列のフォーマット
key = "key"
value = "value"

# format関数
print("{}は{}です。".format(key, value))                    # keyはvalueです。
print("{0}は{1}です。".format(key, value))                  # keyはvalueです。
print("{key}は{value}です。".format(key=key, value=value))  # keyはvalueです。

# f文字列
print(f"{key}は{value}です。")  # keyはvalueです。
print(f"{key =}, {value =}")   # key = 'key', value = 'value'（デバッグで便利そう）