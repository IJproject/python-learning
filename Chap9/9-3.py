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

# P.183 9.3.5~