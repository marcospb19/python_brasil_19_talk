from re import findall

texto = '1' * 10

pattern = r'1{2,4}'
print(findall(pattern , texto))

pattern = r'1{3,4}'
print(findall(pattern , texto))
