# 文字列の除去（strip関数）
# 文字列先頭と末尾限定です
greeting = "  Hello, World!  "
print(greeting.strip())      # Hello, World!（両端の空白が消える）
print(greeting.lstrip())     # Hello, World!  （左側の空白が消える）
print(greeting.rstrip())     #   Hello, World!（右側の空白が消える）
print(greeting.strip('.!?')) #   Hello, World（両端の.!?が消える）