# デコレータ：関数を受け取り、その関数をラップするようにして拡張する
def custom_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

# デコレータを使用して関数を拡張する
def add_numbers1(x, y):
    print(x + y)
    return x + y
custom_decorator_add_numbers1 = custom_decorator(add_numbers1)
custom_decorator_add_numbers1(3, 5)  
# Before the function call, 
# 8, 
# After the function call

# 別の方法
# 複数のデコレータを同時に走らせることも可能
@custom_decorator
def add_numbers2(x, y):
    print(x + y)
    return x + y
add_numbers2(3, 5)
# Before the function call,
# 8,
# After the function call