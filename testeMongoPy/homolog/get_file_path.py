import os
import json

os.system('cls')
# noqa ignora os erros da linha


def get_json(directory):
    json_tree = {}
    directory_name = os.path.basename(directory)
    directory_json = json.dumps(directory_name)
    print(directory_json)

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]  # noqa
    for file in files:
        print(file)
    # files_json = json.dumps(files)

    json_tree["folder"] = directory_name
    json_tree["files"] = list(files)

    for root, directories, files in os.walk(directory):  # noqa percorre diretorio dhc e separa em caminho, diretorios e arquivos
        for diretorio in directories:  # pega apenas os diretorios
            gerar_path = os.path.join(directory, diretorio)  # noqa gera um novo caminho com diretorios dhc/css
            change_json = json.dumps(diretorio)  # noqa transforma os diretorios em json "css"
            print(diretorio)
            for _, _, file_path in os.walk(gerar_path):  # noqa percorre files do caminho criado dhc/css
                gera_json = json.dumps(file_path)  # noqa gera um json dos files percorridos "testedhc.css"
                print(file_path)

    json_data = json.dumps(json_tree)
    print(json_data)
    return json_tree


def get_bytes(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for file in files:
            print(file)
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
        # with open(file_path, "rb") as file:
        # read_file = file.read()
        # print(read_file)
