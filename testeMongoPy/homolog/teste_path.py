import glob
import collections
import json


repo_path = r'C:\Users\joao mendes\Desktop\projectX\design_diplomas\**'

json_path = collections.defaultdict(dict)

pastas = []

for filename in glob.glob(repo_path, recursive=True):
    caminho = filename.split("/")[4:]
    print(caminho)
    for idx, x in enumerate(caminho):
        if idx % 2 == 0:
            caminho.insert(idx, "pastas")

    if "." in str(caminho[-1:]):

        pastas.append(caminho)
        caminho.insert(-1, "arquivos")
        caminho.pop(-3)
        novo = caminho[:-2]
        novo.append("pastas")
        pastas.append(novo)
        pastas.append(caminho)
    else:

        pastas.append(caminho)


pastas = pastas[1:]


d = {}
for path in pastas:
    current_level = d
    for part in path:
        if part not in current_level:
            current_level[part] = {}

        current_level = current_level[part]

l = {} # noqa


def myprint(d):
    for k, v in d.items():
        # print("{0} : {1}".format(k, v))
        level = l
        level[k] = v
        level = level[k]


myprint(d)
# print(l)
# estruturas(pastas)

# print(json_path)
with open('json_Path_gerenciador_design.json', 'w', encoding='utf8') as f:
    json.dump(l, f, indent=4, ensure_ascii=False)
