# 文字列の置換（replace関数）
# 第3引数は最大置換回数
section = "Python is a programming language."
new_section = section.replace("Python", "Ruby")
print(new_section)  # Ruby is a programming language.

new_new_section = section.replace("Python", "JavaScript", 100) 
print(new_new_section)  # JavaScript is a programming language.