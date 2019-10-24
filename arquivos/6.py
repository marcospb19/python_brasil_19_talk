from re import findall

pattern = r"</(.+)>"

text = requests.get("http://example.org").text
result = findall(pattern , text)

print(result)
