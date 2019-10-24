import re

# Ver todas as funções e constantes
# print(dir(re))

from re import findall

print(re.findall("f" , "fff"))

result = re.findall("xu" , "xu")

print(type(result) , len(result))
print(result)

result = re.findall("xu" , "xuxu")

print(type(result) , len(result))
print(result)

# Como é feita a leitura?
print(re.findall("ff" , "fff"))
