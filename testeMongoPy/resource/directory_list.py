import os
# from resource.testeGIT import repo

repo_path = r'C:\Users\joao mendes\Desktop\projectX\teste_git\projectPyX'

diretorios = [name for name in os.listdir(repo_path) if os.path.isdir(
    os.path.join(repo_path, name))]

for diretorio in diretorios:
    print(diretorio)

caminho = r'C:\Users\joao mendes\Desktop\projectX\teste_git\testeMongoPy\lib'

# ratimbum = os.
ratata = os.listdir(caminho)
print(ratata)
