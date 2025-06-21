# タプル
# ・データの集合でありながら、イミュータブルである。
# ・複数の返り値を返す際に、複数を同時に受け取ることができて便利
# ・順番が大事である場合に使用する（要らない場合は集合？）
sample_tuple1 = ("S", "A", "M",)
sample_tuple2 = ("P",)
sample_tuple3 = "L", "E",
sample_tuple4 = "!",

# タプルの結合
merged_tuple = sample_tuple1 + sample_tuple2 + sample_tuple3
print(merged_tuple)  # ('S', 'A', 'M', 'P', 'L', 'E')

# タプルのアンパック
s, a, m = sample_tuple1
print(s)  # S
print(a)  # A
print(m)  # M

# タプル型への変換
sample_array = [1, 2, 3]
tuple_array = tuple(sample_array)
print(type(tuple_array))  # <class 'tuple'>

# イミュータブル性
print(f"before: {sample_tuple1}, id: {id(sample_tuple1)}")  # before: ('S', 'A', 'M')
sample_tuple1 += sample_tuple4
print(f"after: {sample_tuple1}, id: {id(sample_tuple1)}")   # after: ('S', 'A', 'M', '!',)

# タプル同士の比較
# 1個目から要素の比較を順番に行なっていく
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
tuple3 = (1, 3, 0)
print(tuple1 < tuple2)  # True（3 < 4 の時点で比較終了）
print(tuple1 < tuple3)  # True（2 < 3 の時点で比較終了）