# 浮動小数点数の表現
print(5.0 * 10)   # 50.0
print(5.)         # 5.0
print(5e2)        # 500.0
print(True + 1.)  # 2.0（Trueは1として扱われる）

# 型の変換
print(float(True))   # 1.0
print(float(5))      # 5.0
print(float("5.9"))  # 5.9