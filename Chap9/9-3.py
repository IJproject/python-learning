# 引数
# 実引数；関数に渡す引数（argument）
# 仮引数：関数の中での引数（parameter）

# None
# ・明示的に返り値が設定されていない場合、関数の返り値はNoneになる
# ・NoneはFalseと同じ真偽値を示すが、そもそもないこととは違う点が有用
thing = None
if thing is None:           # is演算子でNoneと比較
    print("thing is None")
elif not thing:
    print("thing is false")
else:
    print("thing is true")

# キーワード引数とデフォルト引数
# デフォルト引数が設定されるのは、関数が呼び出された時ではなく、関数が定義されたタイミングなので、ミュータブルなデフォルト引数を渡すことはキケン
def append_to_list(item, list=[]):
    list.append(item)
    print(list)
append_to_list(item = 1)  # [1]
append_to_list(item = 2)  # [1, 2]

# 可変長引数（一度分解して接合する）
# *：タプル化
# **：辞書化
def add_numbers(*args):
    print(args)
def print_info(**kwargs):
    print(kwargs)
print(add_numbers(1, 2, 3))                        # (1, 2, 3)
print_info(name="Alice", age=30, city="New York")  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# キーワード専用引数を強制
# *以降の引数はキーワード引数である必要がある
def func_with_keyword_only(data, *, keyword_arg):
    print(keyword_arg)

# ミュータブルな値を引数として関数に渡す場合、関数内部で値が変更されてしまう可能性があるので注意