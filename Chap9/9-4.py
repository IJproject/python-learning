def sample_docstring():
    """
    これはdocstringのサンプルです。
    """
    return "私は関数からの返り値です"

print(sample_docstring())        # 関数の返り値
print(sample_docstring.__doc__)  # 関数のdocstringを表示
print(help(sample_docstring))    # sample_docstring関数の詳細なdocstringを表示