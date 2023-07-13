import os
from git import Repo

repo_path = r'C:\Users\joao mendes\Desktop\projectX'
diretorio_atual = os.getcwd()


repo = Repo.clone_from('http://192.168.0.13/design/designDiplomas.git',
                       os.path.join(repo_path, 'design_diplomas'),
                       branch="main")


# repo = Repo(diretorio_atual, 'hoteis_flask')

# repo_path = os.path.join(diretorio_atual, 'hoteis_flask')

# repo = Repo(repo_path)

# branch_name = 'f-Config'

# branch = repo.refs[branch_name]

'''
for blob in branch.commit.tree.traverse():
    if blob.type == 'blob':
        print(blob.path)
'''
