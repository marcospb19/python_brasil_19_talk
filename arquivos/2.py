from re import findall

pattern = "[xu]"

text = "uxxuxuu"

result = findall(pattern , text)

print(result)
