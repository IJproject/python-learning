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

# スライス
sliced_list = [10, 11, 12, 13, 14, 15]
sliced_list[1:3] = [20, 21, 22]  # インデックス1から3までを置き換え（スライス数と要素数が合ってなくてもOK）
print(sliced_list)               # [10, 20, 21, 22, 13, 14, 15]
sliced_list[2:4] = (30, 31, 32)  # タプルをスライスに代入
print(sliced_list)               # [10, 20, 30, 31, 32, 13, 14, 15]

# 要素の削除
removed_list = sample_list1.copy()
removed_list.remove(2)      # 値を指定して削除（最初に見つかった要素を削除）
print(removed_list)         # [0, 1, 3, 4, 5]
removed_list.pop(2)         # インデックス番号を指定して削除（インデックスが指定されていない場合は末尾の要素が削除）
print(removed_list)         # [0, 1, 4, 5]
removed_list.clear()        # リストの中身を全て削除
print(removed_list)         # []

# インデックスを取得
print(sample_list1.index(2))  # 2

# 要素の個数
print(sample_list1.count(2))  # 1（2の個数をカウント）

# 文字列の変換
# joinメソッドは文字列に対して定義された関数である
joined_string = ", ".join(sample_list2)
print(joined_string)   # A, B, C

# 要素の並び替え
sort_target_list = [5, 2, 3.9, 1.7, 4]
sorted_list = sorted(sort_target_list)   # 昇順に並び替えた新しいリストを返す
print(sorted_list)                       # [1.7, 2, 3.9, 4, 5]
sort_target_list.sort()                  # 元のリストを昇順に並び替え
sort_target_list.sort(reverse=True)      # 降順に並び替え
print(sort_target_list)                  # [1.7, 2, 3.9, 4, 5]

# リストの長さの取得
print(len(sample_list1))  # 6（要素数を取得）

# リストのコピー（リスト内に配列などが入っていると、その参照を渡してしまうので、その場合はdeepcopy）
copied_list1 = sample_list1.copy()             # copyメソッドを使用してコピー
copied_list2 = sample_list1[:]                 # スライスを使用してコピー
copied_list3 = list(sample_list1)              # list関数を使用してコピー
import copy                                    # copyモジュールをインポート
deepcopied_list = copy.deepcopy(sample_list1)  # DeepCopyを使用してコピー（リスト内に配列などが入っている場合に使用）

# リストの比較
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
print(list1 == list2)  # True（インデックスごとの要素が等しい）
print(list1 < list3)   # True（list1 < list3 の要素があった時点で比較終了）

# 複数のシーケンスの並列反復
list(zip(sample_list1, sample_list2))  # [(0, 'A'), (1, 'B'), (2, 'C')]（要素数が少ない方に合わせてタプルを作成）

# リスト内包表記（実行速度面でも優位なことが多い）
odd_numbers = [num for num in range(1, 10) if num % 2 == 1] # 奇数のリストを作成
print(odd_numbers)                                          # [1, 3, 5, 7, 9]