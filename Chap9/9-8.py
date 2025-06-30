# ジェネレータ
# yield が実行された時点で関数の処理が一時停止し、再度実行すると次のyeildまで処理が進む
# 一回yieldされたものは、再度呼び出したとしても再度yieldされることはない
def custom_range(start, end, step):
    while start < end:
        yield start
        start += step

custom_range_gen = custom_range(0, 10, 2)
print(next(custom_range_gen))  # 0
print(next(custom_range_gen))  # 2
print(next(custom_range_gen))  # 4
print(next(custom_range_gen))  # 6
print(next(custom_range_gen))  # 8
print(next(custom_range_gen))  # エラー（範囲外に達したため）

# for文で展開することもできる
for num in custom_range(0, 10, 2):
    print(num)  # 0, 2, 4, 6, 8（範囲外に達するまで繰り返し）