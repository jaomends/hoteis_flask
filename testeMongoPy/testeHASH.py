import hashlib
import base64

# Dados de entrada
data = b"Hello, world!"  # Bytes ou string a serem hash

# Criar um objeto hash SHA-256
sha256_hash = hashlib.sha256()

# Atualizar o hash com os dados
sha256_hash.update(data)

# Visualização do hash como hexa
ratimbum = sha256_hash.hexdigest()
print(ratimbum)

# Obter o hash final como uma string hexadecimal
hashed_data = sha256_hash.digest()
print(hashed_data)

# Converter o hash para base64
base64_data = base64.b64encode(hashed_data)

# Imprimir o hash em formato base64
print(base64_data)

# Decodificar o hash base64 de volta para bytes
decoded_data = base64.b64decode(base64_data)

# Verificar se os dados decodificados correspondem ao hash original
if decoded_data == hashed_data:
    print("Os dados decodificados correspondem ao hash original.")
else:
    print("Os dados decodificados não correspondem ao hash original.")
