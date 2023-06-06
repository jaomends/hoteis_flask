import os
from git import Repo

# from resource.testeGIT import repo

repo_path = r'C:\Users\joao mendes\Desktop\projectX\teste_git'

lista_teste = []

repo = Repo(repo_path)
git = repo.git

diretorios = [name for name in os.listdir(repo_path) if os.path.isdir(
    os.path.join(repo_path, name))]

for diretorio in diretorios:
    # lista = list(diretorios)
    print(diretorio)

teste_1 = input("Digite a pasta que você quer acessar: ")

for pasta in diretorios:
    if teste_1 == pasta:
        print(f"Você escolheu o diretório: {teste_1}")

new_path = os.path.join(repo_path, teste_1)
print(new_path)

ratata = os.listdir(new_path)
print(ratata)

# select_file =

# read_file = os.readlink(ratata) -- LER O ARQUIVO APÓS SELECIONADO.

# caminho = r'C:\Users\joao mendes\Desktop\projectX\teste_git\testeMongoPy\lib'
# ratimbum = os.

working_tree_dir = repo.working_dir

for root, dirs, files in os.walk(working_tree_dir):
    for file in files:
        file_path = os.path.join(root, file)
        # print(file_path)
