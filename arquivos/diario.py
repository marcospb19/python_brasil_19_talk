from re import findall

texto = open("diario-da-justica.txt" , "r").read()

pattern = r""

result = findall(pattern , texto)
