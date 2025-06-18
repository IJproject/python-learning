# リスト
sample_list1 = [0, 1, 2, 3, 4, 5]  # 数値のリスト
sample_list2 = ["A", "B", "C"]  # 文字列の

# list関数：リスト型に変換する関数
empty_list = list()           # 空のリストを作成（初期化）
list_tuple = list((1, 2, 3))  # タプルをリストに変換

# インデックスアクセス
print(sample_list1[0])  # 1
print(sample_list1[-1]) # 5（最後の要素）

# reverse関数：配列の中身を逆順にする（値を返さないので注意）
reversed_sample_list1 = [1, 2, 3, 4, 5]
reversed_sample_list1.reverse()
print(reversed_sample_list1)  # [5, 4, 3, 2, 1]

# 要素の追加
added_list = sample_list1.copy()
add_list1 = [8, 9, 10]
add_list2 = [11, 12, 13]
added_list.append(6)         # 末尾に要素を追加
added_list.insert(2, 1.5)    # インデックス番号2を指定して要素を追加
added_list.insert(100, 7)    # インデックス番号100を指定して要素を追加（末尾に追加され、インデックス番号は8となる）
added_list.extend(add_list1) # リストを展開して末尾に追加
added_list += add_list2      # リストを展開して末尾に追加（この処理をappendで行うことはできない）
print(added_list)            # [0, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# P.124, 7.2.10~