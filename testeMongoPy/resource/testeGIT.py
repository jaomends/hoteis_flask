import os
from git import Repo

diretorio_atual = os.getcwd()

# repo = Repo(diretorio_atual, 'hoteis_flask')

# repo_path = os.path.join(diretorio_atual, 'hoteis_flask')

repo = Repo.clone_from('http://github.com/jaomends/hoteis_flask.git',
                       os.path.join(diretorio_atual, 'teste_git'),
                       branch="master")

# repo = Repo(repo_path)

# branch_name = 'f-Config'

# branch = repo.refs[branch_name]

'''
for blob in branch.commit.tree.traverse():
    if blob.type == 'blob':
        print(blob.path)
'''
