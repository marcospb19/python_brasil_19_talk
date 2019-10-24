from re import findall

pattern = r'[01]{2}'

texto = """
11
10
01
11
"""

print(findall(pattern , texto))

texto = """
111
110
101
100
"""

print(findall(pattern , texto))
