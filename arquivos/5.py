import re

# Capturar o nome próprio
texto = "Meu nome é João Marcos"

pattern = r".([A-Z][^ ]+)"

print(re.findall(pattern , texto))
