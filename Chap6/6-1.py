# whileループ
count = 0
while count < 5:
    input = input("capitalize: ")  # コマンドからの入力を受け取る
    if input in ["exit", "quit", "q"]:
        print("bye")
        break  # ループを終了する
    if input in ["next", "n"]:
        print("ネクスト東日本")
        continue  # 次のループに進む
    count += 1
else: # breakせずにループが終了した場合の処理
    print("5回入力しました。")