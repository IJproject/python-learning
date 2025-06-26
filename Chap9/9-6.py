# 関数内関数
# クロージャとしての使用が考えられる
# クロージャ：関数がそのスコープ外で定義された変数を「覚えている」状態

def outer_func(param):
    def inner_func():
        print(f"I'm the inner function, and my param is {param}")
    return inner_func

# クロージャ（定義時の内容を変数が保持する）
a = outer_func("Hello")
b = outer_func("World")

a()  # I'm the inner function, and my param is Hello
b()  # I'm the inner function, and my param is World

