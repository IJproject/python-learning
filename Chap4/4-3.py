# 比較演算子
value1 = 10
value2 = 20
value3 = 30
value4 = 40
print(value1 < value3 < value4)                # True（繋げて書くことができる）
print(value1 < value2 and value2 < value3)     # True（AかつBの意味のand） 
print(value1 < value2 or value3 < value4)      # True（AまたはBの意味のor）
print(value1 < value2 and not value3 < value2) # True（否定のnot） 

# 条件分岐
target = 16
if target < 10:
    print("10未満")
elif target < 20:
    print("10以上20未満")
else:
    print("20以上")

